""" This module contains code representing tests for the quicksort
algorithm """
import unittest
from py.algorithms.quick_sort import quick_sort
import random


class QuickSortTests(unittest.TestCase):
    """ This class contains code representing tests for the quicksort
    algorithm """

    def test1(self):
        self.assertEqual([1, 2, 3, 4], quick_sort([4, 3, 2, 1]))

    def test2(self):
        self.assertEqual([-300, -250, -221, 200, 2900, 30012],
                         quick_sort([30012, -221, -250, -300, 200, 2900]))

    def test3(self):
        random.seed(9)
        input_random = [random.randint(-10000, 10000) for i in range(120)]
        self.assertEqual(sorted(input_random), quick_sort(input_random))


if __name__ == "__main__":
    unittest.main()
