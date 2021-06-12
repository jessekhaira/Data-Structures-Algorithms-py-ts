import unittest
from py.data_structures.linked_list import DoublyLinkedList

class DoublyLinkedListTests(unittest.TestCase):
    """
    This class contains unit tests for the doubly linked
    list data structure
    """
    def test1(self):
        linkedList = DoublyLinkedList(5)
        linkedList.add_at_head(9)
        linkedList.add_at_head(10)

        self.assertEqual(linkedList.get(0), 10)
        self.assertEqual(linkedList.get(2), 5)
        self.assertEqual(linkedList.get(3), -1)

    def test2(self):
        linkedList = DoublyLinkedList(5)
        linkedList.add_at_tail(9)
        linkedList.add_at_tail(10)
        linkedList.add_at_tail(123)

        
        self.assertEqual(linkedList.get(0), 5)
        self.assertEqual(linkedList.get(1), 9)
        self.assertEqual(linkedList.get(2), 10)
        self.assertEqual(linkedList.get(3), 123)
        self.assertEqual(linkedList.get(4), -1)

    def test3(self):
        
        linkedList = DoublyLinkedList(5)
        linkedList.add_at_index(1,9)
        linkedList.add_at_index(2,90)
        linkedList.add_at_index(0, -10)
        linkedList.add_at_head(21)
        linkedList.add_at_tail(9)
        
        self.assertEqual(linkedList.get(0), 21)
        self.assertEqual(linkedList.get(1), -10)
        self.assertEqual(linkedList.get(2), 5)
        self.assertEqual(linkedList.get(3), 9)
        self.assertEqual(linkedList.get(4), 90)

    
    def test4(self):
        linkedList = DoublyLinkedList(5)
        linkedList.add_at_index(1,9)
        linkedList.add_at_index(2,90)
        linkedList.add_at_index(0, -10)
        linkedList.add_at_head(21)
        linkedList.add_at_tail(9)
        linkedList.add_at_index(4,25)
        linkedList.add_at_index(2,32)
        self.assertEqual(linkedList.get(0), 21)
        self.assertEqual(linkedList.get(2), 32)
        linkedList.delete_at_index(2)
        self.assertEqual(linkedList.get(2), 5)
        linkedList.delete_at_index(0)

        self.assertEqual(linkedList.head.val, -10)


if __name__ == "__main__":
    unittest.main() 
