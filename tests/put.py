import unittest

from .testbase import TestBase
from jsoncache.errors import ArgumentError


class PutTests(TestBase):
    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)

    def test_put_successfull_missing_key(self):
        with self.assertRaises(ArgumentError):
            self.json_cache.put()

    def test_put_successfull_missing_value(self):
        with self.assertRaises(ArgumentError):
            self.json_cache.put('key1')

    def test_put_successfull_level1(self):
        self.json_cache.put('key1', 'value1')
        self.assertEqual(self.json_cache.get('key1'), 'value1')

    def test_put_successfull_level2(self):
        self.json_cache.put('key1', 'key2', 'value1')
        self.assertEqual(self.json_cache.get('key1', 'key2'), 'value1')

    def test_put_successfull_level2_multiple(self):
        self.json_cache.put('key1', 'key2', 'value1')
        self.json_cache.put('key1', 'key3', 'value2')
        self.json_cache.put('key1', 'key4', 'value3')
        self.assertEqual(self.json_cache.get('key1', 'key4'), 'value3')
        self.assertEqual(self.json_cache.get('key1', 'key2'), 'value1')
        self.assertEqual(self.json_cache.get('key1', 'key3'), 'value2')


if __name__ == '__main__':
    unittest.main()
