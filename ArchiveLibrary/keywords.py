#!/usr/bin/env python

from robot.libraries.Collections import Collections
from robot.libraries.OperatingSystem import OperatingSystem
from .utils import Unzip, Untar
import os
import tarfile
import zipfile


class ArchiveKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    tars = ['.tar', '.tar.bz2', '.tar.gz', '.tgz', '.tz2']

    zips = ['.docx', '.egg', '.jar', '.odg', '.odp', '.ods', '.xlsx', '.odt',
            '.pptx', 'zip']

    def __init__(self):
        self.oslib = OperatingSystem()
        self.collections = Collections()

    def extract_zip_file(self, zfile, dest=None):
        ''' Extract a ZIP file

        `zfile` the path to the ZIP file

        `dest` optional destination folder. Assumes current working directory if it is none
               It will be created if It doesn't exist.
        '''
        
        if dest:
            self.oslib.create_directory(dest)
            self.oslib.directory_should_exist(dest)
        else:
            dest = os.getcwd()
       
        cwd = os.getcwd()

        unzipper = Unzip()

        # Dont know why I a have `gotta catch em all` exception handler here
        try:
            unzipper.extract(zfile, dest)
        except:
            raise
        finally:
            os.chdir(cwd)

    def extract_tar_file(self, tfile, dest=None):
        ''' Extract a TAR file

        `tfile` the path to the TAR file

        `dest` optional destination folder. Assumes current working directory if it is none
               It will be created if It doesn't exist.
        '''
        if dest:
            self.oslib.create_directory(dest)
        else:
            dest = os.getcwd()
            
        self.oslib.file_should_exist(tfile)

        untarrer = Untar()
        untarrer.extract(tfile, dest)

    def archive_should_contain_file(self, zfile, filename):
        ''' Check if a file exists in the ZIP file without extracting it

        `zfile` the path to the ZIP file

        `filename` name of the file to search for in `zfile`
        '''
        self.oslib.file_should_exist(zfile)

        files = []
        if zipfile.is_zipfile(zfile):
            files = zipfile.ZipFile(zfile).namelist()
        else:
            files = tarfile.open(name=zfile).getnames()
        files = [os.path.normpath(item) for item in files]

        self.collections.list_should_contain_value(files, filename)

    def create_tar_from_files_in_directory(self, directory, filename):
        ''' Take all files in a directory and create a tar package from them

        `directory` Path to the directory that holds our files

        `filename` Path to our destination TAR package.
        '''
        if not directory.endswith("/"):
            directory = directory + "/"
        tar = tarfile.open(filename, "w")
        files = os.listdir(directory)
        for name in files:
            tar.add(directory + name, arcname=name)
        tar.close()

    def create_zip_from_files_in_directory(self, directory, filename, sub_directories=False):
        ''' Take all files in a directory and create a zip package from them

        `directory` Path to the directory that holds our files

        `filename` Path to our destination ZIP package.

        `sub_directories` Shall files in sub-directories be included - False by default.
        '''
        if not directory.endswith("/"):
            directory = directory + "/"
        zip = zipfile.ZipFile(filename, "w")

        if not sub_directories:
            files = os.listdir(directory)
            for name in files:
                zip.write(directory + name, arcname=name)
        else:
            for path, _, files in os.walk(directory):
                for target_file in files:
                    file_to_archive = os.path.join(path, target_file)
                    # generate the "relative" path by getting rid of the starting directory
                    file_name = path.replace(directory, '')
                    # the final filename is the relative path plus the file's name
                    file_name = os.path.join(file_name, target_file)

                    zip.write(file_to_archive, arcname=file_name)

        zip.close()

if __name__ == '__main__':
    al = ArchiveKeywords()
    al.extract('test.zip')
