import unittest
import more_fun_with_collections.set_membership as set_membership


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        self.assertTrue(set_membership.in_set('a'))     # Looks for 'a' in testSet, ('a' is in set), expects true

    def test_in_set_false(self):
        self.assertFalse(set_membership.in_set(0))      # Looks for 0 in testSet, (no 0 in set), expects false


if __name__ == '__main__':
    unittest.main()
