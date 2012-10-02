import os
import zipfile
import tarfile

from robot.libraries.BuiltIn import BuiltIn

from robot.libraries.Collections import Collections

from utils import Unzip, Untar


class ArchiveKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    tars = ['.tar', '.tar.bz2', '.tar.gz', '.tgz', '.tz2']

    zips = ['.docx', '.egg', '.jar', '.odg', '.odp', '.ods', '.xlsx', '.odt',
            '.pptx', 'zip']

    def __init__(self):
        self.oslib = BuiltIn().get_library_instance("OperatingSystem")
        self.collections = Collections()

    def extract_zip_file(self, zfile, dest=None):
        if dest:
            self.oslib.create_directory(dest)
            self.oslib.directory_should_exist(dest)

        cwd = os.getcwd()
        #os.chdir(dest)

        unzipper = Unzip()

        try:
            unzipper.extract(zfile, dest)
        except:
            raise
        finally:
            os.chdir(cwd)

    def extract_tar_file(self, tfile, dest=None):
        if dest:
            self.oslib.create_directory(dest)

        self.oslib.file_should_exist(tfile)

        untarrer = Untar()
        untarrer.extract(tfile, dest)

    def archive_should_contain_file(self, zfile, filename):
        self.oslib.file_should_exist(zfile)

        files = []
        if zipfile.is_zipfile(zfile):
            files = zipfile.ZipFile(zfile).namelist()
        else:
            files = tarfile.open(name=zfile).getnames()

        self.collections.list_should_contain_value(files, filename)


if __name__ == '__main__':
    al = ArchiveKeywords()
    al.extract('test.zip')
