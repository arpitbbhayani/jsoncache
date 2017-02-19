import unittest

from jsoncache.utils import update_dict
from jsoncache.errors import CacheUpdateError


class UpdateDictTests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.d = {
            'a': {
                '1': 1
            }
        }

    def test_unsuccessful_number_args(self):
        with self.assertRaises(CacheUpdateError):
            update_dict(self.d, ['b'])

        with self.assertRaises(CacheUpdateError):
            update_dict(self.d, [])

    def test_unsuccessful_change_item_types(self):
        with self.assertRaises(CacheUpdateError):
            update_dict(self.d, [{}, 4])

        with self.assertRaises(CacheUpdateError):
            update_dict(self.d, [(5,), 4])

        with self.assertRaises(CacheUpdateError):
            update_dict(self.d, [set([5]), 4])

        with self.assertRaises(CacheUpdateError):
            update_dict(self.d, [[5], 4])

    def test_unsuccessful_blacklisted_value_type(self):
        with self.assertRaises(CacheUpdateError):
            update_dict(self.d, ['a', '1', set([1, 2, 3])])

    def test_unsuccessful_value_exists(self):
        with self.assertRaises(CacheUpdateError):
            update_dict(self.d, ['a', '1', 'key', 'value'])

    def test_successful_value_update(self):
        update_dict(self.d, ['a', '1', 'value'])
        self.assertEqual(self.d, {
            'a': {
                '1': 'value'
            }
        })

        update_dict(self.d, ['a', '1', [1, 2, 3]])
        self.assertEqual(self.d, {
            'a': {
                '1': [1, 2, 3]
            }
        })

        update_dict(self.d, ['a', '1', (1, 2, 3,)])
        self.assertEqual(self.d, {
            'a': {
                '1': (1, 2, 3,)
            }
        })

    def test_successful_multilevel(self):
        update_dict(self.d, ['b', 'c', 'd', 10])
        self.assertEqual(self.d, {
            'a': {
                '1': 1
            },
            'b': {
                'c': {
                    'd': 10
                }
            }
        })

    def test_successful_add_new_to_level1(self):
        update_dict(self.d, ['b', 4])
        self.assertEqual(self.d, {
            'a': {
                '1': 1
            },
            'b': 4
        })

    def test_successful_add_new_dictionary(self):
        update_dict(self.d, ['b', {'c': 4}])
        self.assertEqual(self.d, {
            'a': {
                '1': 1
            },
            'b': {
                'c': 4
            }
        })

        update_dict(self.d, ['b', 'c', 5])
        self.assertEqual(self.d, {
            'a': {
                '1': 1
            },
            'b': {
                'c': 5
            }
        })


if __name__ == '__main__':
    unittest.main()
