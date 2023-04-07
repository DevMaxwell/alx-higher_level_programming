#!/usr/bin/pyhton3
"""
unittests for the function def max_integer(list=[]) using unitest module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def setUP(self):
        pass

    def tearDown(self):
        pass

    # tests for strings
    def test_string(self):
        self.assertEqual(max_integer(["a", "z"]), "z")

    # test for negative floats
    def test_neg_float(self):
        self.assertEqual(max_integer([-5.55, -66.66, -111.1]), -5.55)

    # regular tests
    def test_simple(self):
        self.assertEqual(max_integer([0, 1, 7, 4]), 7)
        self.assertEqual(max_integer([-1, -3, 0, 3, 6]), 6)
        self.assertEqual(max_integer([6, 96]), 96)
        self.assertEqual(max_integer([2]), 12)

    # test for doc string
    def test_docstring(self):
        self.assertIsNotNone(max_integer.__doc__)

    # test for type error when none is passed
    def test_empty(self):
        self.assertEqual(max_integer([]), None)
        with self.assertRaises(TypeError):
            max_integer(None)

    # test for matrix list
    def test_list_list(self):
        self.assertEqual(max_integer([[1, 2], [3, 2]]), [3, 2])

    # test for type error when string and int are passed
    def test_diff_datatypes(self):
        with self.assertRaises(TypeError):
            max_integer([1, "1"])


if __name__ == "__main__":
    unittest.main()
