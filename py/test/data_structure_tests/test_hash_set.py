import unittest
from py.data_structures.hash_set import HashSet


class TestHashSet(unittest.TestCase):

    def test1(self):
        obj1 = HashSet()
        obj1.add(5)
        obj1.add(9)
        obj1.add(5)

        self.assertEqual(obj1.contains(5), True)
        self.assertEqual(obj1.contains(12), False)
        self.assertEqual(obj1.contains(9), True)

    def test2(self):
        obj1 = HashSet()
        obj1.add(0)
        obj1.add(-123)
        obj1.add(1231)
        obj1.add(14123)

        self.assertEqual(obj1.contains(14123), True)
        obj1.remove(14123)

        self.assertEqual(obj1.contains(14123), False)

        obj1.remove(-123)
        self.assertEqual(obj1.contains(-123), False)

    def test3(self):
        obj1 = HashSet()
        for i in range(1000):
            obj1.add(1000)

        self.assertEqual(obj1._curr_items_hashed, 1)


if __name__ == "__main__":
    unittest.main()