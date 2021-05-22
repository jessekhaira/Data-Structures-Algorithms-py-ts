""" This module contains code representing tests for the recursive quickselect
algorithm """
from py.algorithms.quick_select import recursive_quickselect, iterative_quickselect
import unittest


class TestRecursiveQuickselect(unittest.TestCase):
    """ This class contains unit tests for the recursive quickselect
    algorithm """

    def test1(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(-12, recursive_quickselect(array, 0))

    def test2(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(3, recursive_quickselect(array, 5))

    def test3(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(2, recursive_quickselect(array, 4))

    def test4(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(1, recursive_quickselect(array, 3))

    def test5(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(-2, recursive_quickselect(array, 2))

    def test6(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(None, recursive_quickselect(array, 221))

    def test7(self):
        array = [
            3, 4, 9, 2, 1, -9, -4, 3, 8, -9, 10, 12, 400, 123213, 85, 4, 3, 1,
            2, 3
        ]
        self.assertEqual(-9, recursive_quickselect(array, 1))

    def test8(self):
        array = [
            3, 4, 9, 2, 1, -9, -4, 3, 8, -9, 10, 12, 400, 123213, 85, 4, 3, 1,
            2, 3
        ]
        self.assertEqual(-9, recursive_quickselect(array, 0))

    def test9(self):
        array = [
            3, 4, 9, 2, 1, -9, -4, 3, 8, -9, 10, 12, 400, 123213, 85, 4, 3, 1,
            2, 3
        ]
        self.assertEqual(-4, recursive_quickselect(array, 2))


class TestIterativeQuickselect(unittest.TestCase):
    """ This class contains unit tests for the iterative quickselect
    algorithm """

    def test1(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(-12, iterative_quickselect(array, 0))

    def test2(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(3, iterative_quickselect(array, 5))

    def test3(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(2, iterative_quickselect(array, 4))

    def test4(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(1, iterative_quickselect(array, 3))

    def test5(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(-2, iterative_quickselect(array, 2))

    def test6(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(None, iterative_quickselect(array, 221))

    def test7(self):
        array = [
            3, 4, 9, 2, 1, -9, -4, 3, 8, -9, 10, 12, 400, 123213, 85, 4, 3, 1,
            2, 3
        ]
        self.assertEqual(-9, iterative_quickselect(array, 1))

    def test8(self):
        array = [
            3, 4, 9, 2, 1, -9, -4, 3, 8, -9, 10, 12, 400, 123213, 85, 4, 3, 1,
            2, 3
        ]
        self.assertEqual(-9, iterative_quickselect(array, 0))

    def test9(self):
        array = [
            3, 4, 9, 2, 1, -9, -4, 3, 8, -9, 10, 12, 400, 123213, 85, 4, 3, 1,
            2, 3
        ]
        self.assertEqual(-4, iterative_quickselect(array, 2))


if __name__ == "__main__":
    unittest.main()
