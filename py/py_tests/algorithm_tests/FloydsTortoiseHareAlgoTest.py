from py.algorithms.FloydsTortoiseHareAlgo import floydsTortoiseHareAlgo
from py.data_structures.utils.LinkedList import SinglyLinkedListNode
import unittest

class TestFloydsAlgo(unittest.TestCase):
    def test1(self):
        self.assertEqual(floydsTortoiseHareAlgo(None), None)

    def test2(self):
        node = SinglyLinkedListNode(5)
        self.assertEqual(floydsTortoiseHareAlgo(node), None) 

    def test3(self):
        node = SinglyLinkedListNode(5)
        node.next = SinglyLinkedListNode(3)
        node.next.next = SinglyLinkedListNode(10)
        self.assertEqual(floydsTortoiseHareAlgo(node), None)

    def test4(self):
        node = SinglyLinkedListNode(5)
        node.next = SinglyLinkedListNode(3)
        node.next.next = SinglyLinkedListNode(10)
        node.next.next.next = node 
        self.assertEqual(floydsTortoiseHareAlgo(node), node)

    def test5(self):
        node = SinglyLinkedListNode(5)
        node.next = SinglyLinkedListNode(3)
        node.next.next = SinglyLinkedListNode(10)
        node.next.next.next = SinglyLinkedListNode(15)
        node.next.next.next.next = node.next.next 
        self.assertEqual(floydsTortoiseHareAlgo(node), node.next.next)


if __name__ == "__main__":
    unittest.main() 
