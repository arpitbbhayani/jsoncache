import unittest

from .testbase import TestBase
from jsoncache.errors import ArgumentError


class GetTests(TestBase):
    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)

    def test_get_successfull_missing_args(self):
        with self.assertRaises(ArgumentError):
            self.json_cache.get()

    def test_get_successfull_level1(self):
        self.json_cache.put('key1', 'value1')
        self.assertEqual(self.json_cache.get('key1'), 'value1')

    def test_get_successfull_level2(self):
        self.json_cache.put('key1', 'key2', 'value1')
        self.assertEqual(self.json_cache.get('key1', 'key2'), 'value1')

    def test_get_successfull_level2_int(self):
        self.json_cache.put('key1', 'key2', 1)
        self.assertEqual(self.json_cache.get('key1', 'key2'), 1)

    def test_get_successfull_level2_float(self):
        self.json_cache.put('key1', 'key2', 1.0)
        self.assertEqual(self.json_cache.get('key1', 'key2'), 1.0)

    def test_get_successfull_level2_list(self):
        self.json_cache.put('key1', 'key2', [1,2])
        self.assertEqual(self.json_cache.get('key1', 'key2'), [1,2])

    def test_get_successfull_level2_dict(self):
        self.json_cache.put('key1', 'key2', {'a': 1})
        self.assertEqual(self.json_cache.get('key1', 'key2'), {'a': 1})

    def test_get_successfull_level2_tuple(self):
        self.json_cache.put('key1', 'key2', ('a', 1,))
        self.assertEqual(self.json_cache.get('key1', 'key2'), ['a', 1])

    def test_get_successfull_level2_non_added_key(self):
        self.json_cache.put('key1', 'key2', {'a': 1})
        self.assertEqual(self.json_cache.get('key1', 'key2', 'a'), 1)

if __name__ == '__main__':
    unittest.main()
