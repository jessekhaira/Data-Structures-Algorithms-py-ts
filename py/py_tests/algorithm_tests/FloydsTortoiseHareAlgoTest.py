from py.algorithms.FloydsTortoiseHareAlgo import floydsTortoiseHareAlgo
from py.data_structures.LinkedList import DoublyLinkedList
import unittest

class TestFloydsAlgo(unittest.TestCase):
    def test1(self):
        self.assertEqual(floydsTortoiseHareAlgo(None), None)

    def test2(self):
        node = DoublyLinkedList(5).head
        self.assertEqual(floydsTortoiseHareAlgo(node), None) 


if __name__ == "__main__":
    unittest.main() 
