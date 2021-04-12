""" This module represents a module intended to test our binary seach
algorithms """
import unittest
from py.algorithms.binary_search import iterative_binary_search
from py.algorithms.binary_search import recursive_binary_search


class BinarySearchTest(unittest.TestCase):

    def test1(self):
        arr = [-100, -2, 3, 5]
        self.assertEqual(3, iterative_binary_search(arr, 5))

        self.assertEqual(0, iterative_binary_search(arr, -100))

        self.assertEqual(1, iterative_binary_search(arr, -2))

        self.assertEqual(-1, iterative_binary_search(arr, -122))

    def test2(self):
        arr = [-100, -2, 3, 5]
        self.assertEqual(3, recursive_binary_search(arr, 5))

        self.assertEqual(0, recursive_binary_search(arr, -100))

        self.assertEqual(1, recursive_binary_search(arr, -2))

        self.assertEqual(-1, recursive_binary_search(arr, -122))


if __name__ == "__main__":
    unittest.main()
