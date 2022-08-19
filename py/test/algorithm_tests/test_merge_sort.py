""" This module contains tests for the merge sort algorithm """
import unittest
from py.algorithms.merge_sort import merge_sort


class MergeSortTests(unittest.TestCase):
    """ This class contains unit tests for the merge sort algorithm"""

    def test1(self):
        array = [-9, 2, 1, 2, 3, 4, 5, 6, 9, 18]
        self.assertEqual(sorted(array), merge_sort(array))

    def test2(self):
        array = []
        self.assertEqual([], merge_sort(array))

    def test3(self):
        array = [-1000, 21, 2, 5, 9, -2000, 21]
        self.assertEqual(sorted(array), merge_sort(array))

    def test4(self):
        array = [
            -1000, 21, 2, 5, 9, -2000, 21, 500, 23, 123, 5921, 123, 81239,
            12309123, 12039950, -12318, -213123123, -1232193, 192.232, 2521.324,
            129838912391
        ]
        self.assertEqual(sorted(array), merge_sort(array))


if __name__ == "__main__":
    unittest.main()
