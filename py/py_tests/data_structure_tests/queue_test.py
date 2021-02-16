import unittest
from py.data_structures.Queue import Queue


class queue(unittest.TestCase):
    def test1(self):
        queue = Queue()
        self.assertRaises(IndexError, queue.poll)
        self.assertRaises(IndexError, queue.top) 

    def test2(self):
        pass 
    

if __name__ == "__main__":
    unittest.main() 