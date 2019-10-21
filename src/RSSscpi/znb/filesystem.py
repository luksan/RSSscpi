import ntpath
import os.path

from memoized_property import memoized_property

from ..SCPI_response import make_ieee_data_block
from . import ZNB_gen


class Filesystem(ZNB_gen.MMEMory):
    def __init__(self, instrument):
        super(Filesystem, self).__init__(parent=instrument)
        self.instrument = instrument

    def getcwd(self):
        """
        :return: a string representing the current working directory on the instrument.
        :rtype: str
        """
        return str(self.CDIRectory.q())

    def chdir(self, path):
        """
        Change the current working directory on the instrument to path.
        """
        self.CDIRectory.w(path)

    @memoized_property
    def default_dir(self):
        cdir = self.getcwd()
        self.CDIRectory.w("DEFault")
        def_dir = self.getcwd()
        self.chdir(cdir)
        return def_dir

    @memoized_property
    def calpool_dir(self):
        return ntpath.join(self.default_dir, 'Calibration', 'Data')

    def file(self, filename, path=None):
        """
        Create a File instance

        :param filename:
        :param path: Set to getcwd() if None
        :return: File(filename, path)
        :rtype: File
        """
        if path is None:
            path = self.getcwd()
        return File(filename=filename, path=path, instrument=self.instrument)

    def listdir(self, path=None):
        if path is None:
            path = self.getcwd()
        return Directory(path=path, instrument=self.instrument).listdir()


class Path(object):
    def __init__(self, path, filename):
        if filename and ntpath.isabs(filename):
            self.path, self.filename = ntpath.split(filename)
        else:
            self.filename = filename
            self.path = path

    def __str__(self):
        return ntpath.join(self.path, self.filename)

    def __repr__(self):
        return str(self)


class Directory(Path):
    def __init__(self, path, instrument):
        super(Directory, self).__init__(path=path, filename=None)
        self.instrument = instrument

    def __str__(self):
        return self.path

    def file(self, filename):
        return self.instrument.File(filename=filename, instrument=self.instrument, path=self.path)

    def listdir(self):
        def mk_list(match):
            if match.group(2) == "<DIR>":
                return self.__class__(path=match.group(1), instrument=self.instrument)
            else:
                return self.instrument.filesystem.file(filename=match.group(1), path=self.path)

        import re
        x = self.instrument.MMEMory.CATalog.q(self.path)
        # <used_size>,<free_disk_space> {,<file_name>,,<file_size>}
        try:
            used_size, free_disk, files = str(x).split(",", 2)
        except ValueError:
            raise RuntimeError("Bad instrument response from MMEM:CAT? %s -> %s" % (self.path, str(x)))
        # We can't split files on comma alone, since a comma might be contained in a filename
        r = re.finditer(r' (.*?),(?:( <DIR>),|, (\d+)),', files)
        return list(map(mk_list, r))

    @staticmethod
    def isdir():
        return True

    @staticmethod
    def isfile():
        return False


class File(Path):
    """
    An object representing a file on the instrument.
    """

    def __init__(self, instrument, filename, path=None):
        """

        :param instrument:
        :type instrument: ZNB
        :param filename:
        :param path:
        """
        super(File, self).__init__(filename=filename, path=path)
        self.instrument = instrument
        if self.path is None:
            self.path = instrument.filesystem.getcwd()

    @staticmethod
    def isdir():
        return False

    @staticmethod
    def isfile():
        return True

    @property
    def full_path(self):
        return ntpath.join(self.path, self.filename)

    def read(self):
        return self.instrument.MMEMory.DATA.q(self.full_path).block_data()

    def write(self, data):
        # FIXME: rename to reflect that the method overwrites the existing file
        self.instrument.MMEMory.DATA.w(self.full_path, make_ieee_data_block(data))

    def get(self, local_target):
        """
        Retrieve a file from the VNA.

        :param local_target: The target file on the controller. If local_target is a directory the file will be stored with the same name as on the instrument.
        """
        if os.path.isdir(local_target):
            local_target = os.path.join(local_target, self.filename)
        with open(local_target, "wb") as fd:
            fd.write(self.read())

    def put(self, local_file):
        """
        Copy a file from the controller to the instrument.

        :param local_file:
        :return:
        """
        with open(local_file, "rb") as fd:
            self.write(fd.read())

    def copy(self, target):
        """
        Copy the file to a new location on the instrument

        :param target: The location of the copy
        """
        self.instrument.MMEMory.COPY.w(self.full_path, str(target))
