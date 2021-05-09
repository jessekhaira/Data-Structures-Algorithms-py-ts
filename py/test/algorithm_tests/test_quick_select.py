from py.algorithms.quickselect import quickselect
import unittest


class tests(unittest.TestCase):

    def test1(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(-12, quickselect(array, 0))

    def test2(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(3, quickselect(array, 5))

    def test3(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(2, quickselect(array, 4))

    def test4(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(1, quickselect(array, 3))

    def test5(self):
        array = [-2, -9, -12, 3, 2, 1]
        self.assertEqual(-2, quickselect(array, 2))


if __name__ == "__main__":
    unittest.main()
