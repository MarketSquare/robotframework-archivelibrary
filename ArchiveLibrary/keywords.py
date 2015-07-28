import os
import zipfile
import tarfile

from robot.libraries.BuiltIn import BuiltIn

from robot.libraries.Collections import Collections
from robot.libraries.OperatingSystem import OperatingSystem

from utils import Unzip, Untar


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

        `dest` optional destination folder. It will be created if It doesn't exist.
        '''

        if dest:
            self.oslib.create_directory(dest)
            self.oslib.directory_should_exist(dest)

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

        `dest` optional destination folder. It will be created if It doesn't exist.
        '''
        if dest:
            self.oslib.create_directory(dest)

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
		
    def create_zip_from_files_in_directory(self, directory, filename):
        ''' Take all files in a directory and create a zip package from them

        `directory` Path to the directory that holds our files

        `filename` Path to our destination ZIP package.
        '''
        if not directory.endswith("/"):
            directory = directory + "/"
        zip = zipfile.ZipFile(filename, "w")
        files = os.listdir(directory)
        for name in files:
            zip.write(directory + name, arcname=name)
        zip.close()

if __name__ == '__main__':
    al = ArchiveKeywords()
    al.extract('test.zip')
