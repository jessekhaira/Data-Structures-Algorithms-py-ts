""" This module contains code for the tests for the disjoint set
class """
import unittest
from py.data_structures.disjoint_set import DisjointSet


class DisjointSetTests(unittest.TestCase):
    """ This class contains unit tests for the disjoint set
    data structure """

    def test1(self):
        obj1 = DisjointSet(20)
        self.assertEqual([-1] * 20, obj1.forest)

    def test2(self):
        obj1 = DisjointSet(20)
        obj1.union(4, 5)
        obj1.union(4, 9)
        obj1.union(4, 15)
        obj1.union(4, 19)

        self.assertEqual(4, obj1.find(4))
        self.assertEqual(4, obj1.find(9))
        self.assertEqual(4, obj1.find(15))
        self.assertEqual(4, obj1.find(19))

    def test3(self):
        obj1 = DisjointSet(20)
        obj1.union(4, 5)
        obj1.union(4, 9)
        obj1.union(4, 15)
        obj1.union(4, 19)
        obj1.union(1, 19)
        obj1.union(3, 19)

        self.assertEqual(4, obj1.find(4))
        self.assertEqual(4, obj1.find(3))


if __name__ == "__main__":
    unittest.main()
