# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import threading
import timeit
import traceback

import visa

from RSSscpi.SCPI_gen_support import SCPINodeBase
from RSSscpi.SCPI_response import SCPIResponse, make_ieee_data_block
from RSSscpi.scpi_registers import StatusByteRegister, EventStatusRegister

try:
    import Queue  # Use Queue.Queue, not multiprocessing.Queue, to avoid unnecessary pickling
except ImportError:
    import queue as Queue

from collections import OrderedDict
try:
    from itertools import izip
except ImportError:
    izip = zip
import re, string

import logging
import warnings


class LimitedCapacityDict(OrderedDict):
    def __init__(self, max_len=None):
        """
        Creates a LimitedCapacity dict, which will hold a maximum of max_len entries.
        Setting max_len to None or 0 will make the capacity unlimited.

        :param int or None max_len: The maximum number of entries in the dict.
        """
        self._max_len = max_len
        super(LimitedCapacityDict, self).__init__()

    @property
    def max_len(self):
        return self._max_len

    @max_len.setter
    def max_len(self, value):
        self._max_len = value
        self._check_len()

    def _check_len(self):
        if self._max_len and self._max_len < len(self):
            excess = len(self) - self._max_len
            keys = [key for n, key in izip(range(excess), self)]  # Create a list contaioning overflowing keys
            for key in keys:  # Don't iterate over self while deleting
                del self[key]

    def __setitem__(self, key, value):
        if key in self:  # Move the element to the end, if already inserted
            del self[key]
        super(LimitedCapacityDict, self).__setitem__(key, value)
        self._check_len()


class VISAEvent(object):
    def __init__(self, duration, stb, esr):
        self.duration = duration
        self.stb = stb
        self.esr = esr


class SCPICmdFormatter(string.Formatter):
    def __init__(self):
        self.last_number = 0
        super(SCPICmdFormatter, self).__init__()

    def vformat(self, format_string, args, kwargs):
        ret = super(SCPICmdFormatter, self).vformat(format_string, args, kwargs)
        self.last_number = 0
        return ret

    def get_value(self, key, args, kwargs):
        if key == '':
            key = self.last_number
            self.last_number += 1
        return super(SCPICmdFormatter, self).get_value(key, args, kwargs)

    def format_field(self, value, format_spec):
        if not format_spec:  # check for empty string
            pass
        elif format_spec[-1] == "*":  # code for list unpack
            return ", ".join(map(lambda x: self.format_field(x, format_spec[:-1]), value))
        elif format_spec[-1] == "q":  # code for single quoted string
            format_spec = format_spec[:-1] + "s"
            value = str(value)
            if not value or value[0] not in ["'", '"'] or value[0] != value[-1]:  # The arg isn't quoted
                value = "'%s'" % (value, )
        elif format_spec[-1] == "s":  # coerce everything with str() for convenience
            value = str(value)

        return super(SCPICmdFormatter, self).format_field(value, format_spec)


# http://stackoverflow.com/questions/16244923/how-to-make-a-custom-exception-class-with-multiple-init-args-pickleable
# http://bugs.python.org/issue1692335
class InstrumentError(BaseException):
    def __init__(self, err_no=0, err_str="", stack=None):
        super(InstrumentError, self).__init__()
        self.err_no = err_no
        self.err_str = err_str
        self.stack = stack

    def __str__(self):
        ret = "SCPI error: {:d},{}\n".format(self.err_no, self.err_str)
        if self.stack:
            ret += "".join(traceback.format_list(self.stack))
        return ret


class Instrument:

    MAX_RESPONSE_LOG_LENGTH = 50

    def __get__(self, instance, owner):
        # We can't delete __get__ from the class, so this overrides
        # the SCPINodeBase __get__ method, essentially making it a no-op.
        return self

    Error = InstrumentError

    def __init__(self, visa_res):
        """
        :type visa_res: pyvisa.resources.messagebased.MessageBasedResource
        :param visa_res:
        """

        super().__init__()

        self._visa_res = visa_res
        self.command_cnt = 0
        """
        The number of writes/queries performed in total
        """

        self.visa_logger = logging.getLogger(__name__ + ".VISA")
        """
        A logging.Logger instance for all VISA interactions
        """

        self._log_time_start = timeit.default_timer()
        """
        This is T0 for the log.
        """

        self._service_request_callback_handle = None
        self._last_cmd_time = 0

        self._visa_lock = threading.Lock()
        self._in_callback = threading.Lock()
        """Locks used to synchronize VISA operations."""

        self.event_queue = Queue.Queue()
        """
        Events generated by the VISA library are queued here.
        """

        self.error_queue = Queue.Queue()
        """
        Errors fetched from the instrument are queued here.
        """

        self.exception_on_error = True
        self._cmd_debug = LimitedCapacityDict(max_len=500)
        """
        _call_visa(...) stores the stack trace here for each command.
        """

    def init(self):
        """
        Setup the Service Request handling and turn on event reporting in the instrument.
        """
        # Clear the status register
        # Enable Operation Complete reporting with *OPC
        # Generate a Service Request when the event status register changes, or the error queue is non-empty
        self._write("*CLS;*ESE 127;*SRE 36")

        self._service_request_callback_handle = self._visa_res.install_handler(
            visa.constants.EventType.service_request, self._service_request_handler, 0)
        self._visa_res.enable_event(visa.constants.EventType.service_request, visa.constants.VI_HNDLR)

    @property
    def _log_time(self):
        return (timeit.default_timer() - self._log_time_start) * 1e3

    def log_debug(self, fmt_string, *args, duration=None, **kwargs):
        time = "%5.1f ms" % self._log_time
        time += " %.2f ms\t" % duration if duration else "\t"
        self.visa_logger.debug(time + fmt_string, *args, **kwargs)

    # noinspection PyUnusedLocal
    def _service_request_handler(self, session, event_type, context, user_handle):
        """
        This function is invoked as a callback from the VISA library.

        :param session:
        :param event_type:
        :param context:
        :param user_handle:
        :return:
        """
        duration = timeit.default_timer() - self._last_cmd_time
        self.visa_logger.debug("Handling service request")
        with self._in_callback:
            with self._visa_lock:
                stb = StatusByteRegister(self._visa_res.read_stb())  # Read out the SRQ status byte
                esr = None
                if stb.event_status_summary:
                    # read and reset the event status register
                    esr = EventStatusRegister(int(self._call_visa(self._visa_res.query, "*ESR?")))
                self.visa_logger.info("{:5.1f} ms Callback VISA event: STB: {:}, ESR: {:}, duration {:.2f} ms"
                                      .format(self._log_time,
                                              stb.short_status(),
                                              esr.short_status() if esr is not None else "-",
                                              duration * 1e3))
                self.event_queue.put_nowait(VISAEvent(duration, stb, esr))

                if stb.error_queue_not_empty:
                    self._get_error_queue()
        return visa.constants.VI_SUCCESS

    def _get_error_queue(self):
        err = self._query("SYSTem:ERRor:ALL?")
        cnt = 0
        # -222,"Data out of range;SOURce1:POWer1:ATTenuation 80\n"
        # -151,"Invalid string data;CALCulate1:PARameter:SDEFine '...",-114,"Header suffix out of range;DISPlay:WINDow1:TRACe:EFEed 'A..."
        for r in re.finditer(r'(-?\d+),"(.*?([A-Z]{3}\S*).*?(?:\n.*?)?)"', str(err)):
            cnt += 1
            x = (int(r.group(1)), r.group(2).replace("\n", " "))
            bad_cmd = r.group(3)
            tb = self._cmd_debug.get(bad_cmd)
            if not tb:
                self.visa_logger.debug("No stack for <%s> <%s>", str(err), str(r.groups()))
            self.error_queue.put_nowait(InstrumentError(x[0], x[1], tb))
            self.visa_logger.error("%d %s", *x)
        if not cnt:
            self.error_queue.put_nowait(InstrumentError(-1, str(err), None))

    def check_error_queue(self):
        if not self.error_queue.empty() and self.exception_on_error and self._in_callback.acquire(False):
            # http://blog.bstpierre.org/python-exception-handling-cleanup-and-reraise
            self._in_callback.release()  # Don't raise the exception from the VISA library callback thread
            # TODO: raise with original stack trace instead?
            raise self.error_queue.get(block=False)

    def _begin_visa_call(self, data):
        if isinstance(data, bytes):
            node_bytes, _, args = data.partition(b" ")
            node_str = node_bytes.decode(self._visa_res.encoding)
            args = args[:self.MAX_RESPONSE_LOG_LENGTH]
            try:
                args_str = " " + args.decode(self._visa_res.encoding) if args else ""
            except UnicodeDecodeError:
                args_str = repr(args[:int(len(args) / 3)])
        else:
            node_str, _, args_str = data.partition(" ")
            args_str = args_str[:self.MAX_RESPONSE_LOG_LENGTH]
        node_str = node_str.strip()

        self.check_error_queue()
        self.command_cnt += 1
        self._cmd_debug[node_str] = traceback.extract_stack()[:-2]  # Store the current stack for later debugging
        self._call_time_start = timeit.default_timer()
        return node_str + args_str

    def _call_visa(self, func, *args, **kwargs):
        self.check_error_queue()

        try:
            ret = func(*args, **kwargs)
        except visa.Error as e:
            err = "Resource error: " + str(e) + ", " + func.__name__
            self.visa_logger.exception(err)
            raise
        return ret

    def _end_visa_call(self, cmd_str, response):
        self._last_cmd_time = timeit.default_timer()
        elapsed = (self._last_cmd_time - self._call_time_start) * 1e3
        log_time = (self._last_cmd_time - self._log_time_start) * 1e3

        if hasattr(response, "strip"):
            if isinstance(response, bytes):
                try:
                    response = response.decode(self._visa_res.encoding)
                except UnicodeDecodeError:
                    response = repr(response)
            logged_response = response.strip()
            if len(logged_response) > self.MAX_RESPONSE_LOG_LENGTH:  # Add "..." to show that the response is truncated
                r = " -> '%s'..." % (logged_response[:self.MAX_RESPONSE_LOG_LENGTH])
            else:
                r = " -> '%s'" % (logged_response)
        else:
            r = ""
        self.visa_logger.info("%5.1f ms %.2f ms\t%s%s",
                              log_time, elapsed, cmd_str.strip(), r,
                              extra={"duration": elapsed, "response": response})

    def _build_arg_str(self, cmd, args, kwargs, query):
        """

        :param SCPINode cmd: The SCPINode which the arguments belong to
        :param tuple args: *args from query()/write()
        :param dict kwargs: **kwargs from query()/write()
        :return: The formatted command arguments
        """
        encoding = self._visa_res.encoding
        termination = self._visa_res.write_termination

        ret = [ bytes(cmd.build_cmd(), encoding=encoding) ]
        if query:
            ret.append(b"?")

        arg_bytes = None

        if "fmt" in kwargs and "param_enc" in kwargs:
            raise ValueError("fmt and param_enc cannot be used at the same time")

        if "param_enc" in kwargs:
            arg_bytes = self._build_arg_str_enc(*args, **kwargs)
        elif "fmt" in kwargs:
            arg_bytes = self._build_arg_str_fmt(*args, **kwargs)
        elif args:
            # No format string specified, so try to guess something reasonable
            # Assume that all positional arguments are to be sent comma separated, with the same formatting.
            if "quote" in kwargs:
                if kwargs["quote"]:
                    fmt = "{:q*}"
                else:
                    fmt = "{:s*}"
            elif "'string'" in cmd.args and str(args[0]).lower() not in (x.lower() for x in cmd.args):
                fmt = "{:q*}"
            elif cmd.args and all(x[0] == "'" and x[-1] == "'" for x in cmd.args if x):
                # Quote the argument if all alternatives are quoted
                # See TRIGger:SEQuence:LINK
                fmt = "{:q*}"
            else:
                fmt = "{:s*}"
            if not cmd.args:
                warnings.warn("Command %s does not specify any arguments. Supply fmt= kwarg to suppress this warning." % cmd.build_cmd())
            arg_bytes = self._build_arg_str_fmt(args, fmt=fmt, **kwargs)

        if arg_bytes:
            ret.append(b" ")  # Separator between command and arguments
            ret.append(arg_bytes)

        if termination:
            ret.append(termination.encode(encoding))
        return b"".join(ret)

    def _build_arg_str_fmt(self, *args, fmt, **kwargs):
        assert isinstance(fmt, str)

        str_args = SCPICmdFormatter().vformat(fmt, args, kwargs)
        return str_args.encode(self._visa_res.encoding)

    def _build_arg_str_enc(self, *args, param_enc, **kwargs):
        if isinstance(param_enc, str):
            param_enc = (param_enc, )
        assert len(args) == len(param_enc)

        arg_list = []
        for param, param_fmt in zip(args, param_enc):
            if param_fmt == "b":
                arg_list.append(param)
            elif param_fmt == "ieee":
                arg_list.append(make_ieee_data_block(param))
            else:
                arg_list.append(SCPICmdFormatter().format("{:%s}" % param_fmt, param).encode(self._visa_res.encoding))
        return b", ".join(arg_list)

    def _write(self, cmd_str):
        c = self._begin_visa_call(cmd_str)
        try:
            self._call_visa(self._visa_res.write, cmd_str)
        finally:
            self._end_visa_call(c, None)

    def _write_raw(self, data):
        cmd_str = self._begin_visa_call(data)
        try:
            self._call_visa(self._visa_res.write_raw, data)
        finally:
            self._end_visa_call(cmd_str, None)

    def write(self, cmd, *args, **kwargs):
        """
        Send a string to the instrument, without reading a response.

        :param cmd: The SCPI command
        :type cmd: SCPINodeBase
        :param args: Any number of arguments for the command, will be converted with str()
        :rtype: None
        """
        x = self._build_arg_str(cmd, args, kwargs, query=False)

        self._in_callback.acquire()  # We wait on the callback lock so that the callback handler gets priority on the visa lock
        with self._visa_lock:
            self._in_callback.release()
            self._write_raw(x)

    def _query(self, cmd_str):
        c = self._begin_visa_call(cmd_str)
        x = None
        try:
            x = self._call_visa(self._visa_res.query, cmd_str)
            return SCPIResponse(x)
        finally:
            self._end_visa_call(c, x)

    def _query_raw(self, data):
        cmd_str = self._begin_visa_call(data)
        x = None
        try:
            self._call_visa(self._visa_res.write_raw, data)
            x = self._call_visa(self._visa_res.read_raw)
            return SCPIResponse(x, encoding=self._visa_res.encoding)
        finally:
            self._end_visa_call(cmd_str, x)

    def query(self, cmd, *args, **kwargs):
        """
        Execute a SCPI query

        :param cmd: The SCPI command
        :type cmd: SCPINodeBase
        :param args: A list of arguments for the command, will be converted with str() and joined with ", "
        :return: The response from the pyvisa query
        :rtype: SCPIResponse
        """
        # TODO: add function to read back result later
        x = self._build_arg_str(cmd, args, kwargs, query=True)
        try:
            self._in_callback.acquire()  # We wait on the callback lock so that the callback handler gets priority on the visa lock
            with self._visa_lock:
                self._in_callback.release()
                return self._query_raw(x)
        except visa.VisaIOError as e:
            if e.error_code == visa.constants.VI_ERROR_TMO:  # timeout
                if self.exception_on_error:
                    try:
                        raise self.error_queue.get(timeout=1)  # Wait for up to 1 s for the error callback to be processed
                    except Queue.Empty:
                        pass
            raise e

    def update_display(self, state=True, once=False):
        if state:
            if once:
                cmd = "ONCE"
            else:
                cmd = "ON"
        else:
            cmd = "OFF"
        self.SYSTem.DISPlay.UPDate.w(cmd)

    def preset(self):
        """
        Send `*RST` to the instrument, and set up the event registers again.
        """
        self.RST.w()
        self.query_OPC()
        self._write("*CLS;*ESE 127;*SRE 36")

    def query_OPC(self):
        """
        Send `*OPC?` to the instrument and wait for the response.
        """
        return str(self.OPC.q())

    def send_OPC(self):
        """
        Send `*OPC` to the instrument.
        """
        self.OPC.w()

    def send_TRG(self):
        """
        Send `*TRG` to the instrument.
        """
        self.TRG.w()
