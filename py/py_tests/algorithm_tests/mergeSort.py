import unittest
from py.algorithms.mergesort import mergesort


class tests(unittest.TestCase):
    def test1(self):
        array = [-9,2,1,2,3,4,5,6,9,18]
        self.assertEqual([-9,1,2,2,3,4,5,6,9,18], mergesort(array))

    def test2(self):
        array = []
        self.assertEqual([], mergesort(array))

    def test3(self):
        array = [-1000,21,2,5,9,-2000,21]
        self.assertEqual([-2000,-1000,2,5,9,21,21], mergesort(array))


if __name__ == "__main__":
    unittest.main()



