# -*- coding: utf-8 -*-
"""

@author: Lukas Sandström
"""

import logging
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
    def __init__(self, res):
        self.raw = res

    def __nonzero__(self):
        """
        Converts the instrument response to a boolean value

        :return: bool
        """
        return str(self) in ["1", "ON"]

    def __str__(self):
        x = self.raw.replace("\r", "\n")
        return x.strip().strip("'")

    def __int__(self):
        x = str(self).split()[0]  # Remove the unit string
        return int(x)

    def __float__(self):
        x = str(self).split()[0]  # Remove the unit string
        return float(x)

    def comma_list_pairs(self):
        """
        Split the comma separated response into a list of tuples,
        with each tuple containing two consecutive response elements.

        :return: [ (str1, str2), ..]
        """
        x = self.split_comma()
        return zip(*[iter(x)] * 2)

    def split_comma(self):
        """
        Split the response into a list, separated by commas.
        Each list element is stripped of leading and trailing whitespace.

        :return: a string list
        :rtype: list of str
        """
        return [x.strip() for x in self.raw.split(",")]

    def numpy_array(self, dtype=numpy.float64):
        return numpy.fromstring(self.raw, sep=",", dtype=dtype)

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
        return SCPIBlockData.parse(self.raw)


class SCPIBlockData(object):
    def __init__(self, data=None):
        self.data = data

    @staticmethod
    def parse(blk):
        if blk[0] != "#":
            logging.getLogger(__name__).error("Invalid block data header: '%s[...]", str(blk[0:5]))
            # FIXME: raise exception here?
        n = int(blk[1])  # The number of digits in the data length specifier
        l = int(blk[2:n + 2])  # data length
        return blk[n + 2:l + n + 2]

    @staticmethod
    def format(data):
        l = str(len(data))
        return "#" + str(len(l)) + l + data

    def __str__(self):
        return self.format(self.data)
