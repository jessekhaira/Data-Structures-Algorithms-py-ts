import unittest
from py.data_structures.Deque import Deque

class DequeTests(unittest.TestCase):
    def test1(self):
        obj1 = Deque()
        self.assertRaises(IndexError, obj1.pop_first)
        self.assertRaises(IndexError, obj1.pop_last)
        self.assertRaises(IndexError, obj1.peek_first)
        self.assertRaises(IndexError, obj1.peek_last)


    

if __name__ == "__main__":
    unittest.main()



