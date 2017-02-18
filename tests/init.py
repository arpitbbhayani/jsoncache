import os
import shutil
import unittest

from jsoncache import JSONCache
from jsoncache.errors import CacheError
from .testbase import TestBase


class InitTests(TestBase):
    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)

    def test_successful_init(self):
        filepath = os.path.join(self.TEST_DIR, self.CACHE_NAME)
        JSONCache(filepath)

    def test_unsuccessful_init_existing_folder_instead_of_file(self):
        filepath = os.path.join(self.TEST_DIR)
        with self.assertRaises(CacheError):
            JSONCache(filepath)

    def test_unsuccessful_init_existing_file_with_no_permissions(self):
        filepath = os.path.join(self.NO_PERMISSION_DIR, "ls")
        with self.assertRaises(CacheError):
            JSONCache(filepath)

    def test_unsuccessful_init_existing_folder_with_no_permissions(self):
        filepath = os.path.join(self.NO_PERMISSION_DIR)
        with self.assertRaises(CacheError):
            JSONCache(filepath)

    def test_unsuccessful_init_filepath_but_folder_with_no_permissions(self):
        filepath = os.path.join(self.NO_PERMISSION_DIR, self.CACHE_NAME)
        with self.assertRaises(CacheError):
            JSONCache(filepath)


if __name__ == '__main__':
    unittest.main()
