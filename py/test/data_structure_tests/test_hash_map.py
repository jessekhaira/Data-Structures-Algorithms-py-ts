""" This module contains code for the tests for the hash map
class """
import unittest
from py.data_structures.hash_map import HashMap


class HashMapTests(unittest.TestCase):
    """ This class contains unit tests for the hash map
    data structure """

    def test1(self):
        obj1 = HashMap()
        obj1.put(3, 5)
        obj1.put(9, 6)
        obj1.put(10, 5)
        self.assertEqual(obj1.get(3), 5)
        self.assertEqual(obj1.get(9), 6)
        self.assertEqual(obj1.get(10), 5)

    def test2(self):
        obj1 = HashMap()
        obj1.put(3, 5)
        obj1.put(9, 6)
        obj1.put(10, 5)
        obj1.remove(3)
        obj1.remove(9)
        self.assertEqual(None, obj1.get(3))
        self.assertEqual(None, obj1.get(9))

    def test3(self):
        obj1 = HashMap()
        obj1.put(3, 5)
        obj1.put(3, 9)
        obj1.put(3, 1231)
        self.assertEqual(obj1.get(3), 1231)


if __name__ == "__main__":
    unittest.main()
