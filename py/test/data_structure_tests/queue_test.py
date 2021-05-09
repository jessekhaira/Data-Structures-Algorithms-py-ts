""" Testing module for the Queue data structure """
import unittest
from py.data_structures.queue import Queue


class QueueTests(unittest.TestCase):
    def test1(self):
        queue_test = Queue()
        self.assertRaises(IndexError, queue_test.poll)
        self.assertRaises(IndexError, queue_test.top)

    def test2(self):
        queue_test = Queue()
        for i in range(150):
            queue_test.push(i)
        for i in range(150):
            self.assertEqual(len(queue_test), 150-i)
            self.assertEqual(queue_test.top(), i)
            self.assertEqual(queue_test.poll(), i)

if __name__ == "__main__":
    unittest.main()
