import unittest
from py.algorithms.binary_search import iterative_binary_search
from py.algorithms.binary_search import recursiveBinarySearch


class tests(unittest.TestCase):

    def test1(self):
        arr = [-100, -2, 3, 5]
        self.assertEqual(3, iterative_binary_search(arr, 5))

        self.assertEqual(0, iterative_binary_search(arr, -100))

        self.assertEqual(1, iterative_binary_search(arr, -2))

        self.assertEqual(-1, iterative_binary_search(arr, -122))

    def test2(self):
        arr = [-100, -2, 3, 5]
        self.assertEqual(3, recursiveBinarySearch(arr, 5))

        self.assertEqual(0, recursiveBinarySearch(arr, -100))

        self.assertEqual(1, recursiveBinarySearch(arr, -2))

        self.assertEqual(-1, recursiveBinarySearch(arr, -122))


if __name__ == "__main__":
    unittest.main()
