import unittest

from .testbase import TestBase


class SaveTests(TestBase):
    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)

    def test_save_successfull(self):
        self.json_cache.put('key', 'value')
        self.json_cache.save()


if __name__ == '__main__':
    unittest.main()
