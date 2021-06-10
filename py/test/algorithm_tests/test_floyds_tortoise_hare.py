""" This module contains code testing the python implementation of floyds
tortoise hare algorithm """
from py.algorithms.floyds_tortoise_hare import floyds_tortoise_hare
from py.utils.LinkedList import SinglyLinkedListNode, DoublyLinkedListNode
import unittest


class TestFloydsAlgo(unittest.TestCase):

    def test1(self):
        self.assertEqual(floyds_tortoise_hare(None), None)

    def test2(self):
        node = SinglyLinkedListNode(5)
        self.assertEqual(floyds_tortoise_hare(node), None)

    def test3(self):
        node = SinglyLinkedListNode(5)
        node.next = SinglyLinkedListNode(3)
        node.next.next = SinglyLinkedListNode(10)
        self.assertEqual(floyds_tortoise_hare(node), None)

    def test4(self):
        node = SinglyLinkedListNode(5)
        node.next = SinglyLinkedListNode(3)
        node.next.next = SinglyLinkedListNode(10)
        node.next.next.next = node
        self.assertEqual(floyds_tortoise_hare(node), node)

    def test5(self):
        node = SinglyLinkedListNode(5)
        node.next = SinglyLinkedListNode(3)
        node.next.next = SinglyLinkedListNode(10)
        node.next.next.next = SinglyLinkedListNode(15)
        node.next.next.next.next = node.next.next
        self.assertEqual(floyds_tortoise_hare(node), node.next.next)

    def test6(self):
        node = DoublyLinkedListNode(6)
        node.next = DoublyLinkedListNode(8)
        node.next.next = DoublyLinkedListNode(9)
        node.next.next.next = node
        self.assertEqual(floyds_tortoise_hare(node), node)


if __name__ == "__main__":
    unittest.main()
