import os
import zipfile

from robot.libraries.BuiltIn import BuiltIn

from robot.libraries.Collections import Collections

from utils import Unzip


class ArchiveKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self):
        self.oslib = BuiltIn().get_library_instance("OperatingSystem")
        self.collections = Collections()

    def extract_zip_file(self, zfile, dest=None):
        if dest:
            self.oslib.create_directory(dest)
            self.oslib.directory_should_exist(dest)

        cwd = os.getcwd()
        os.chdir(dest)

        unzipper = Unzip()

        try:
            unzipper.extract(zfile, dest)
        except:
            raise
        finally:
            os.chdir(cwd)

    def archive_should_contain_file(self, zfile, filename):
        self.oslib.file_should_exist(zfile)

        z = zipfile.ZipFile(zfile)
        self.collections.list_should_contain_value(z.namelist(), filename)


if __name__ == '__main__':
    al = ArchiveKeywords()
    al.extract('test.zip')
