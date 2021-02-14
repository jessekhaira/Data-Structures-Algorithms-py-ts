import unittest
from py.data_structures.Stack import Stack


class tests(unittest.TestCase):
    def test1(self):
        new_stack = Stack()
        self.assertEqual(new_stack.top(), None)
        self.assertRaises(IndexError, new_stack.pop)
        

if __name__ == "__main__":
    unittest.main() 