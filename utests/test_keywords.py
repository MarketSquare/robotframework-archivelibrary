import unittest
import zipfile
from unittest import mock
from unittest.mock import Mock

from ArchiveLibrary import ArchiveKeywords


class TestArchiveKeywords(unittest.TestCase):

    @mock.patch('ArchiveLibrary.keywords.zipfile')
    @mock.patch('ArchiveLibrary.utils.os.walk')
    def test_create_zip_with_default_compression(self, mock_walk, mock_zipfile):
        mock_walk.return_value = [('/foo', 'ignore', ['file1.txt'])]

        archive_keywords = ArchiveKeywords()
        archive_keywords.create_zip_from_files_in_directory('/foo', 'ignore')

        mock_zipfile.ZipFile().write.assert_called_once_with('/foo/file1.txt', arcname='file1.txt')

    @mock.patch('ArchiveLibrary.keywords.zipfile')
    @mock.patch('ArchiveLibrary.utils.os.walk')
    def test_create_zip_with_no_default_compression(self, mock_walk, mock_zipfile):
        mock_walk.return_value = [('/foo', 'ignore', ['file1.txt'])]

        archive_keywords = ArchiveKeywords()
        archive_keywords.create_zip_from_files_in_directory('/foo', 'filename.zip', False, 'lzma')

        mock_zipfile.ZipFile.assert_called_once_with('filename.zip', 'w', zipfile.ZIP_LZMA)
        mock_zipfile.ZipFile().write.assert_called_once_with('/foo/file1.txt', arcname='file1.txt')

    @mock.patch('ArchiveLibrary.utils.os.walk')
    def test_create_zip_raise_unknown_compression(self, mock_walk):
        mock_walk.return_value = [('/foo', 'ignore', ['file1.txt'])]

        archive_keywords = ArchiveKeywords()
        with self.assertRaises(ValueError):
            archive_keywords.create_zip_from_files_in_directory('/foo', 'filename.zip', False, 'ignore')

    @mock.patch('ArchiveLibrary.keywords.tarfile')
    @mock.patch('ArchiveLibrary.utils.os.walk')
    def test_create_tar_from_files_in_directory(self, mock_walk, mock_tarfile):
        mock_walk.return_value = [('/foo', 'ignore', ['file1.txt'])]

        archive_keywords = ArchiveKeywords()
        archive_keywords.create_tar_from_files_in_directory('/foo', 'filename.zip')

        mock_tarfile.open.assert_called_once_with('filename.zip', 'w')
        mock_tarfile.open().add.assert_called_once_with('/foo/file1.txt', arcname='file1.txt')

    @mock.patch('ArchiveLibrary.keywords.Collections')
    @mock.patch('ArchiveLibrary.keywords.zipfile')
    @mock.patch('ArchiveLibrary.keywords.OperatingSystem')
    def test_zip_archive_should_contain_file(self, mock_oslib, mock_zipfile, mock_collections):
        mock_oslib.file_should_exist = Mock()
        mock_zipfile.is_zipfile.return_value = True
        mock_zipfile.ZipFile().namelist.return_value = ['file1.txt', 'file2.txt']

        archive_keywords = ArchiveKeywords()
        archive_keywords.archive_should_contain_file('/foo', 'filename.zip')

        mock_collections().list_should_contain_value.assert_called_once_with(['file1.txt', 'file2.txt'], 'filename.zip')

    @mock.patch('ArchiveLibrary.keywords.Collections')
    @mock.patch('ArchiveLibrary.keywords.tarfile')
    @mock.patch('ArchiveLibrary.keywords.zipfile')
    @mock.patch('ArchiveLibrary.keywords.OperatingSystem')
    def test_no_zip_archive_should_contain_file(self, mock_oslib, mock_zipfile, mock_tarfile, mock_collections):
        mock_oslib.file_should_exist = Mock()
        mock_oslib.file_should_exist = Mock()
        mock_zipfile.is_zipfile.return_value = False
        mock_tarfile.open().getnames.return_value = ['file1.txt', 'file2.txt']

        archive_keywords = ArchiveKeywords()
        archive_keywords.archive_should_contain_file('/foo', 'filename.zip')

        mock_collections().list_should_contain_value.assert_called_once_with(['file1.txt', 'file2.txt'], 'filename.zip')
