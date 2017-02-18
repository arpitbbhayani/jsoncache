import os
import shutil
import unittest

from jsoncache import JSONCache


class TestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.CACHE_NAME = 'sample_cache'
        self.NO_PERMISSION_DIR = '/usr/bin'
        self.TEST_DIR = '/tmp/json-cache-tests'

    def setUp(self):
        if not os.path.exists(self.TEST_DIR):
            os.makedirs(self.TEST_DIR)
        self.json_cache = JSONCache(os.path.join('/tmp/json-cache-tests', self.CACHE_NAME))

    def tearDown(self):
        shutil.rmtree(self.TEST_DIR)


if __name__ == '__main__':
    unittest.main()
