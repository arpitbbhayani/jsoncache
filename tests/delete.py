import unittest

from .testbase import TestBase
from jsoncache.errors import ArgumentError, NotInCacheError


class GetTests(TestBase):
    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)

    def test_delete_successfull_missing_args(self):
        with self.assertRaises(ArgumentError):
            self.json_cache.get()

    def test_delete_successfull_level1(self):
        self.json_cache.put('key1', 'value1')
        self.json_cache.delete('key1')
        with self.assertRaises(NotInCacheError):
            self.json_cache.get('key1')

    def test_delete_successfull_level2(self):
        self.json_cache.put('key1', 'key2', 'value1')
        self.json_cache.put('key1', 'key3', 'value2')
        self.json_cache.delete('key1', 'key2')
        with self.assertRaises(NotInCacheError):
            self.json_cache.get('key1', 'key2')
        self.assertEqual(self.json_cache.get('key1', 'key3'), 'value2')

    def test_delete_successfull_tuple(self):
        self.json_cache.put('key1', 'key2', (1, 2, 3))
        self.json_cache.put('key1', 'key3', [1, 2, 3, 4])
        self.json_cache.delete('key1', 'key2')
        with self.assertRaises(NotInCacheError):
            self.json_cache.get('key1', 'key2')
        self.assertEqual(self.json_cache.get('key1', 'key3'), [1, 2, 3, 4])

    def test_delete_unsuccessfull_non_existing_key_level1(self):
        with self.assertRaises(NotInCacheError):
            self.json_cache.delete('key1')

    def test_delete_unsuccessfull_non_existing_key_level2(self):
        self.json_cache.put('key1', 'key3', 'value2')
        with self.assertRaises(NotInCacheError):
            self.json_cache.delete('key1', 'key2')

    def test_delete_unsuccessfull_non_existing_key_with_value(self):
        self.json_cache.put('key1', 'key2', 'value1')
        with self.assertRaises(NotInCacheError):
            self.json_cache.delete('key1', 'key2', 'value1')

if __name__ == '__main__':
    unittest.main()
