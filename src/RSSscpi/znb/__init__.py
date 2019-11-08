# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

from typing import List, Union

from ..gen import ZNB_gen
from ..instrument import Instrument
from ..scpi.class_property import SCPIPropertyMapping
import RSSscpi.network as net

import logging

from memoized_property import memoized_property

from .channel import Channel, ChannelCal, ChannelVNAPort, Sweep, SweepSegments, SweepSegment
from .diagram import Diagram
from .filesystem import File, Filesystem
from .trace import Trace, Marker, Limit

__all__ = ["Channel", "ChannelCal", "ChannelVNAPort", "Sweep", "SweepSegments", "SweepSegment"]
__all__ += ["Trace", "Marker", "Limit"]


def connect_ethernet(ip_address: str) -> "ZNB":
    """
    Helper to connect to a ZNB VNA via Ethernet / TCPIP / VISA.
    Creates an ZNB instance and calls init() on it before returning.

    :param ip_address: The ip address in string format
    :return: An initialized ZNB instance.
    :rtype: ZNB
    """
    return net.connect_ethernet(ZNB, ip_address, "hislip0")


class ZNBZeroconf(net.ZeroconfInfo):
    def __init__(self, zeroconf_info):
        self.fw = ""
        self.serial = ""
        super(ZNBZeroconf, self).__init__(zeroconf_info)

    def parse_zc_info(self, i):
        self.name = i.properties['fqdn'].split(".")[0]
        self.fw = i.properties['FirmwareVersion']
        self.serial = i.properties['SerialNumber']

    def __str__(self):
        return "%s, %s, %s" % (self.name, self.fw, self.ip_address)


class ZCListener(net.ZeroconfListener):
    info_class = ZNBZeroconf
    service_name = "_vxi-11._tcp.local."

    def filter_zc_info(self, zc_info):
        return "ZNB" in zc_info.name


def find_znb(max_time=2, max_devices=None):
    """
    Use zeroconf to scan the local network for ZNB VNAs

    :param float max_time: The maximum time we will wait, in seconds
    :param int max_devices: Stop the search after this many devices have been found
    :return: A list of ZNBZeroconf objects describing the found devices.
    :rtype: list[ZNBZeroconf]
    """

    return net.zeroconf_scan(ZCListener(), max_time, max_devices)


class ZNB(Instrument):
    _scpi = ZNB_gen()  # type: ZNB_gen

    @property
    def scpi(self) -> ZNB_gen:
        return self._scpi

    def __getattr__(self, item):
        if item[:3].isupper():  # Only allow SCPI node access
            return getattr(self.scpi, item)
        raise AttributeError

    def __init__(self, visa_res):
        super().__init__(visa_res)
        self.logger = logging.getLogger(__name__)
        self.visa_logger = self.logger.getChild("VISA")
        self._port_count = None

    @memoized_property
    def filesystem(self):
        """
        A Filsystem instance which enables filesystem operations on the instrument.

        :rtype: RSSscpi.znb.filesystem.Filesystem
        """
        return Filesystem(self)

    @property
    def cal_manager(self):
        return CalibrationManager(self)

    def init(self):
        super().init()

        self._set_codec()
        self.reset_remote_emulation()

    def _set_codec(self):
        self._visa_res.encoding = "utf-8"
        self.scpi.SYSTem.COMMunicate.CODec.w("UTF8")  # Set the character encoding

    def reset_remote_emulation(self):
        # type: () -> str
        """
        Restores the SYSTem:LANGuage setting to SCPI, disabling emulation of other VNA types.

        :return: The original SYSTem:LANGuage setting
        """
        orig_lang = str(self.SYSTem.LANGuage.q())
        if orig_lang != "SCPI":
            self.visa_logger.warning("Changing remote language from '%s' to 'SCPI' (default)", orig_lang)
            self.SYSTem.LANGuage.w("SCPI")
        return orig_lang

    use_binary_data_transfer = SCPIPropertyMapping(ZNB_gen.FORMat.DATA,
                                                   str,
                                                   {"REAL": True, "ASCii": False},
                                                   get_root_node=lambda x: x.scpi)

    @property
    def active_channel(self):
        """
        Get/set the active channel, INSTrument:NSELect?
        """
        return self.get_channel(int(self.INSTrument.NSELect.q()))

    @active_channel.setter
    def active_channel(self, n):
        if hasattr(n, "n"):
            n = n.n
        self.INSTrument.NSELect.w(n)

    def get_channel(self, n):
        # type: (int) -> Channel
        """
        :param n: The number of the channel
        :return: A Channel object
        """
        return Channel(n, self)

    def query_channel_list(self):
        """
        Returns a list of tuples representing all the channels in the active recall set.
        CONFigure:CHANnel:CATalog?

        The first element of each tuple is a :class:`Channel` instance,
        the second element is the name of the channel as a string.
        """
        x = self.CONFigure.CHANnel.CATalog.q().comma_list_pairs()
        return [(self.get_channel(int(n)), str(name)) for n, name in x]

    def get_diagram(self, n):
        """
        Returns a :class:`RSSscpi.znb.Diagram` instance, linked to the instrument.

        :param int n: The diagram id, Wnd
        :rtype: RSSscpi.znb.diagram.Diagram
        """
        return Diagram(n, self)

    def query_number_of_ports(self):
        # type: () -> int
        """
        Query the instrument about how many physical ports there are on the instrument.
        This can be different from the number of test ports, i.e if a switch matrix is connected
        to the instrument.

        :return: The number of physical ports on the instrument
        """
        if self._port_count:
            return self._port_count
        x = int(self.INSTrument.PORT.COUNt.q())
        self._port_count = x
        return x

    def save_recall_set(self, filename: Union[str, File]) -> File:
        """
        Saves the instrument state to `filename`. The standard file ending is .znx.
        SCPI node: MMEMory:STORe:STATe

        :param filename: The path/file that the instrument state should be stored at.
        :return: A File object referring to the saved state
        """
        self.scpi.MMEMory.STORe.STATe.w(str(filename), fmt="1,{:q}")
        return self.filesystem.file(str(filename))

    def load_recall_set(self, filename: Union[str, File]):
        """
        Loads instrument state from the file filename on the VNA.

        :param filename: The file on the VNA from which the state will be loadied
        """
        self.scpi.MMEMory.LOAD.STATe.w(str(filename), fmt="1,{:q}")

    # noinspection PyShadowingNames
    def save_screenshot(self, filename, diagram=None):
        """
        Take a screenshot containing only this diagram. The file type is inferred from the filename extension,
        valid options are BMP, EMF, EWMF, JPG, PDF, PNG, SVG, WMF.

        :param str filename: The filename under which the screenshot will be saved on the instrument.
        :param Diagram diagram: The diagram to be captured. The whole screen will be captured if None.
        :return: a File object representing the captured screenshot
        :rtype: RSSscpi.znb.filesystem.File
        """
        import ntpath
        _, filetype = ntpath.splitext(filename)
        filetype = filetype[1:].upper()
        if filetype not in self.HCOPy.DEVice.LANGuage.args:
            raise ValueError("Invalid file extension for screenshot: " + filetype)
        self.MMEMory.NAME.w(filename)  # Define the filename
        self.HCOPy.DESTination.w("MMEM")  # Print to mass storage
        self.HCOPy.DEVice.LANGuage.w(filetype)  # Define the file type
        if diagram is not None:
            diagram.select_diagram()
            self.HCOPy.PAGE.WINDow.w("ACTive")  # Print only the active diagram
        else:
            self.HCOPy.PAGE.WINDow.w("HARDcopy")
        self.HCOPy.IMMediate.w()  # Perform the screen capture
        return self.filesystem.file(filename)

    def update_display(self, state=True, once=False):
        if state:
            if once:
                cmd = "ONCE"
            else:
                cmd = "ON"
        else:
            cmd = "OFF"
        self.scpi.SYSTem.DISPlay.UPDate.w(cmd)

    def preset(self):
        """
        Send `*RST` to the instrument, and set up the event registers again.
        """
        self.scpi.RST.w()
        self.query_OPC()
        self._write("*CLS;*ESE 127;*SRE 36")

    def query_OPC(self):
        """
        Send `*OPC?` to the instrument and wait for the response.
        """
        return str(self.scpi.OPC.q())

    def send_OPC(self):
        """
        Send `*OPC` to the instrument.
        """
        self.scpi.OPC.w()

    def send_TRG(self):
        """
        Send `*TRG` to the instrument.
        """
        self.scpi.TRG.w()


class CalibrationManager(object):
    """
    Methods for handling the calibration pool, calkits, etc.
    """

    def __init__(self, instrument):
        self._instr = instrument

    @property
    def instrument(self) -> ZNB:
        return self._instr

    def query_calpool_list(self) -> List[str]:
        """
        Returns a list of all the calgroups in the calpool
        """
        cal_files = self.instrument.filesystem.listdir(self.instrument.filesystem.calpool_dir)
        return [c.filename for c in cal_files]

    def delete_calgroup(self, name):
        """
        Remove a calgroup file from the calpool

        :param name: The name of the calgroup to be removed
        """
        self.instrument.MMEMory.DELete.CORRection.w(name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    devices = find_znb(max_devices=10, max_time=1)
    print([str(_dev) for _dev in devices])
    znb = connect_ethernet(devices[0].ip_address)
    print(znb.IDN.q())
