# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import warnings

try:
    import numpy
except ImportError:
    warnings.warn("numpy import failed. Some functionality will be missing.")

    class numpy:
        float64 = None


class SCPIResponse(object):
    """
    Class used for containing and parsing responses from SCPI queries.
    """
    def __init__(self, res, encoding='ascii'):
        if isinstance(res, str):
            res = res.encode(encoding)
        self.raw = res
        self.encoding = encoding

    def __nonzero__(self):
        """
        Converts the instrument response to a boolean value

        :return: bool
        """
        if not str(self).upper() in ["1", "ON", "0", "OFF"]:
            raise ValueError("Can't convert '%s' to bool.", str(self))
        return str(self).upper() in ["1", "ON"]

    __bool__ = __nonzero__

    def __str__(self):
        x = self.raw.decode(self.encoding).replace("\r", "\n")
        return x.strip().strip("'")

    def __int__(self):
        x = str(self).split()[0]  # Remove the unit string
        return int(x)

    def __float__(self):
        x = str(self).split()[0]  # Remove the unit string
        return float(x)

    def __eq__(self, other):
        return str(self) == other

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(str(self))

    def comma_list_pairs(self, convert=lambda x: x):
        """
        Split the comma separated response into a list of tuples,
        with each tuple containing two consecutive response elements.

        :param convert: A callable that takes two-tuple as input and returns a converted two-tuple
        :return: [ (str1, str2), ..]
        """
        x = self.split_comma()
        return list(convert(t) for t in zip(*[iter(x)]*2))

    def split_comma(self, convert=lambda x: x):
        """
        Split the response at commas, and return the result as a list.

        Each list element is stripped of leading and trailing whitespace and quotes,
        and passed to the callable `convert`.

        :param convert: A callable that will be applied to each element in the list
        :return: [ convert(x) for x in self.split(",") ]
        """
        return [convert(x.decode(self.encoding).strip(" '\n\r")) for x in self.raw.split(b",")]

    def numpy_array(self, dtype=numpy.float64):
        return numpy.fromstring(str(self), sep=",", dtype=dtype)

    def numpy_complex(self):
        x = self.numpy_array(dtype=numpy.float64)
        # http://stackoverflow.com/questions/15244327/python-unpacking-string-of-floats-to-complex-numbers
        x.dtype = numpy.complex128
        return x

    def block_data(self):
        """
        Interpret the response as a SCPI block data transfer

        :return: the data from the block transfer
        """
        try:
            if self.raw[0:1] != b"#":
                raise ValueError("Missing # at start of data block.")
            hdr_len = int(self.raw[1:2].decode('ascii'))  # The number of digits in the data length specifier
            data_len = int(self.raw[2:2+hdr_len].decode('ascii'))  # data length
            data = self.raw[2+hdr_len:2+hdr_len+data_len]
            if len(data) != data_len:
                raise ValueError("Not enugh data in IEEE data block.")
            return data
        except Exception as e:
            raise ValueError("Invalid block data header: '%s'. %s" % (str(self.raw[0:5]), str(e)))


def make_ieee_data_block(data):
    """
    Adds a SCPI block data header to the input string.

    :param bytes data: Binary data
    :return: The input data with a SCPI block data header prepended
    :rtype: bytes
    """

    if not isinstance(data, bytes):
        raise ValueError("data argument must be a bytes instance")
    data_len = str(len(data))
    hdr_len = str(len(data_len))
    hdr = bytes("#" + hdr_len + data_len, 'ascii')
    return hdr + data


