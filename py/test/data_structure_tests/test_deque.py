import unittest
from py.data_structures.deque import Deque


class DequeTests(unittest.TestCase):

    def test1(self):
        obj1 = Deque()
        self.assertRaises(IndexError, obj1.pop_first)
        self.assertRaises(IndexError, obj1.pop_last)
        self.assertRaises(IndexError, obj1.peek_first)
        self.assertRaises(IndexError, obj1.peek_last)

    def test2(self):
        obj2 = Deque()
        for i in range(150):
            obj2.add_first(i)
            self.assertEqual(obj2.peek_first(), i)
            self.assertEqual(obj2.peek_last(), 0)

    def test3(self):
        obj3 = Deque()
        for i in range(150):
            obj3.add_last(i)
            self.assertEqual(obj3.peek_first(), 0)
            self.assertEqual(obj3.peek_last(), i)
            self.assertEqual(len(obj3), i + 1)

    def test4(self):
        obj4 = Deque()
        for i in range(150):
            obj4.add_last(i)

        head = 0
        length = 150
        while obj4:
            self.assertEqual(obj4.pop_first(), head)
            head += 1
            self.assertEqual(len(obj4), length - head)

    def test5(self):
        obj5 = Deque()
        obj5.add_first(21)

        self.assertEqual(obj5.pop_first(), 21)
        self.assertRaises(IndexError, obj5.pop_last)


if __name__ == "__main__":
    unittest.main()
