""" This module contains code intended to test the binary seach
algorithms implemented in the library """
import unittest
from py.algorithms.binary_search import iterative_low_bound_binary_search, iterative_high_bound_binary_search
from py.algorithms.binary_search import recursive_binary_search


class TestIterativeLowBoundBinarySearch(unittest.TestCase):
    """ This class holds unit tests for the binary search algorithm """

    def test1(self):
        arr = [-100, -2, 3, 5]
        self.assertEqual(3, iterative_low_bound_binary_search(arr, 5))

        self.assertEqual(0, iterative_low_bound_binary_search(arr, -100))

        self.assertEqual(1, iterative_low_bound_binary_search(arr, -2))

        self.assertEqual(-1, iterative_low_bound_binary_search(arr, -122))

    def test2(self):
        arr = [-1000, -100, -100, -100, -100, -2, 5, 8, 9, 15, 25, 45, 100]
        self.assertEqual(iterative_low_bound_binary_search(arr, -100), 1)

    def test3(self):
        arr = [
            -1000, -100, -100, -100, -100, -2, 5, 5, 5, 5, 5, 8, 9, 15, 25, 45,
            100
        ]
        self.assertEqual(iterative_low_bound_binary_search(arr, 5), 6)

    def test4(self):
        arr = [
            -1000, -100, -100, -100, -100, -2, 5, 5, 5, 5, 5, 8, 9, 15, 25, 45,
            100, 100, 100, 100, 500, 500, 525, 525, 525, 525
        ]
        self.assertEqual(iterative_low_bound_binary_search(arr, 525),
                         len(arr) - 4)


class TestIterativeHighBoundBinarySearch(unittest.TestCase):

    def test1(self):
        arr = [-1000, -100, -100, -100, -100, -2, 5, 8, 9, 15, 25, 45, 100]
        self.assertEqual(iterative_high_bound_binary_search(arr, -100), 4)

    def test2(self):
        arr = [-1000, -100, -100, -100, -100, -2, 5, 8, 9, 15, 25, 45, 100]
        self.assertEqual(iterative_high_bound_binary_search(arr, 5), 6)


class TestRecursiveBinarySearch(unittest.TestCase):

    def test1(self):
        arr = [-100, -2, 3, 5]
        self.assertEqual(3, recursive_binary_search(arr, 5))

        self.assertEqual(0, recursive_binary_search(arr, -100))

        self.assertEqual(1, recursive_binary_search(arr, -2))

        self.assertEqual(-1, recursive_binary_search(arr, -122))


if __name__ == "__main__":
    unittest.main()
