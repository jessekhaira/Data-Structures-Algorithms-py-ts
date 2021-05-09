""" This module contains code for testing the bubble sort algorithm
python implementation """
import unittest
from py.algorithms.bubble_sort import bubble_sort


class BubbleSortTests(unittest.TestCase):

    def test1(self):
        array = [-9, 2, 1, 2, 3, 4, 5, 6, 9, 18]
        self.assertEqual([-9, 1, 2, 2, 3, 4, 5, 6, 9, 18], bubble_sort(array))

    def test2(self):
        array = []
        self.assertEqual([], bubble_sort(array))

    def test3(self):
        array = [-1000, 21, 2, 5, 9, -2000, 21]
        self.assertEqual([-2000, -1000, 2, 5, 9, 21, 21], bubble_sort(array))


if __name__ == "__main__":
    unittest.main()
