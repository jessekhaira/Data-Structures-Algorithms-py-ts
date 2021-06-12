import unittest
from py.data_structures.stack import Stack


class StackTests(unittest.TestCase):

    def test1(self):
        new_stack = Stack()
        self.assertRaises(IndexError, new_stack.pop)
        self.assertRaises(IndexError, new_stack.top)

    def test2(self):
        new_stack = Stack()
        for i in range(150):
            new_stack.push(i)

        for i in reversed(range(150)):
            self.assertEqual(len(new_stack), i + 1)
            self.assertEqual(new_stack.top(), i)
            self.assertEqual(new_stack.pop(), i)


if __name__ == "__main__":
    unittest.main()
