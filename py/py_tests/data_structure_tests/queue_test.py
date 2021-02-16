import unittest
from py.data_structures.Queue import Queue


class queue(unittest.TestCase):
    def test1(self):
        queue = Queue()
        self.assertRaises(IndexError, queue.poll)
        self.assertRaises(IndexError, queue.top) 

    def test2(self):
        queue = Queue()
        for i in range(150):
            queue.push(i)
        
        for i in range(150):
            self.assertEqual(len(queue), 150-i)
            self.assertEqual(queue.top(), i)
            self.assertEqual(queue.poll(), i)

    

if __name__ == "__main__":
    unittest.main() 