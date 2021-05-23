import unittest
import zipfile
from unittest import mock

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
