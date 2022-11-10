#!/usr/bin/env python

import os
import tarfile
import zipfile

from robot.libraries.Collections import Collections
from robot.libraries.OperatingSystem import OperatingSystem

from .utils import Unzip, Untar, return_files_lists


class ArchiveKeywords:
    ROBOT_LIBRARY_SCOPE = 'Global'

    compressions = {
        "stored": zipfile.ZIP_STORED,
        "deflated": zipfile.ZIP_DEFLATED,
        "bzip2": zipfile.ZIP_BZIP2,
        "lzma": zipfile.ZIP_LZMA
    }

    tars = ['.tar', '.tar.bz2', '.tar.gz', '.tgz', '.tz2']

    zips = ['.docx', '.egg', '.jar', '.odg', '.odp', '.ods', '.xlsx', '.odt',
            '.pptx', 'zip']

    def __init__(self):
        self.oslib = OperatingSystem()
        self.collections = Collections()

    def extract_zip_file(self, zip_file, dest=None):
        """ Extract a ZIP file

        `zip_file` the path to the ZIP file

        `dest` optional destination folder. Assumes current working directory if it is none
               It will be created if It doesn't exist.
        """

        if dest:
            self.oslib.create_directory(dest)
            self.oslib.directory_should_exist(dest)
        else:
            dest = os.getcwd()

        cwd = os.getcwd()

        # Dont know why I a have `gotta catch em all` exception handler here
        try:
            Unzip().extract(zip_file, dest)
        except:
            raise
        finally:
            os.chdir(cwd)

    def extract_tar_file(self, tar_file, dest=None):
        """ Extract a TAR file

        `tar_file` the path to the TAR file

        `dest` optional destination folder. Assumes current working directory if it is none
               It will be created if It doesn't exist.
        """
        if dest:
            self.oslib.create_directory(dest)
        else:
            dest = os.getcwd()

        self.oslib.file_should_exist(tar_file)

        Untar().extract(tar_file, dest)

    def archive_should_contain_file(self, zip_file, filename):
        """ Check if a file exists in the ZIP file without extracting it

        `zip_file` the path to the ZIP file

        `filename` name of the file to search for in `zip_file`
        """
        self.oslib.file_should_exist(zip_file)

        files = zipfile.ZipFile(zip_file).namelist() if zipfile.is_zipfile(zip_file) else tarfile.open(
            zip_file).getnames()

        files = [os.path.normpath(item) for item in files]

        self.collections.list_should_contain_value(files, filename)

    def create_tar_from_files_in_directory(self, directory, filename, sub_directories=True, tgz=False):
        """ Take all files in a directory and create a tar package from them

        `directory` Path to the directory that holds our files

        `filename` Path to our destination TAR package.

        `sub_directories` Shall files in sub-directories be included - True by default.

        `tgz` Creates a .tgz / .tar.gz archive (compressed tar package) instead of a regular tar - False by default.
        """
        if tgz:
            tar = tarfile.open(filename, "w:gz")
        else:
            tar = tarfile.open(filename, "w")

        files = return_files_lists(directory, sub_directories)
        for filepath, name in files:
            tar.add(filepath, arcname=name)

        tar.close()

    @classmethod
    def create_zip_from_files_in_directory(cls, directory, filename, sub_directories=False, compression="stored"):
        """ Take all files in a directory and create a zip package from them

        `directory` Path to the directory that holds our files

        `filename` Path to our destination ZIP package.

        `sub_directories` Shall files in sub-directories be included - False by default.

        `compression` stored (default; no compression), deflated, bzip2 (with python >= 3.3), lzma (with python >= 3.3)
        """

        if cls.compressions.get(compression) is None:
            raise ValueError("Unknown compression method")
        comp_method = cls.compressions.get(compression)

        the_zip = zipfile.ZipFile(filename, "w", comp_method)

        files = return_files_lists(directory, sub_directories)
        for filepath, name in files:
            the_zip.write(filepath, arcname=name)

        the_zip.close()


if __name__ == '__main__':
    al = ArchiveKeywords()
    al.extract('test.zip')
