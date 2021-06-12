""" This module contains code for a class that represents the
doubly linked list data structure """
from py.utils.linked_list import DoublyLinkedListNode


class DoublyLinkedList:
    """ This class represents the doubly linked list data
    structure.
    """

    def __init__(self, val):
        self.head = DoublyLinkedListNode(val)
        self.tail = self.head

    def get(self, index):
        currIndex = 0
        node = self.head
        while node and currIndex <= index:
            if currIndex == index:
                return node.val
            else:
                currIndex += 1
                node = node.next
        return -1

    def add_at_head(self, val):
        """
        This function creates a doubly linked list node with the value given as input, and inserts the node
        to be the new head of the linked list.
        """
        newNode = DoublyLinkedListNode(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def add_at_tail(self, val):
        """
        This function creates a doubly linked list node with the value given as input, and inserts the node
        to be the new tail of the linked list. 
        """
        newNode = DoublyLinkedListNode(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def add_at_index(self, index, val):
        if index == 0:
            self.add_at_head(val)
        else:
            self._insert_node(val, index)

    def _insert_node(self, val, index):
        node = self.head
        currIndex = 0
        while node and currIndex <= index:
            if currIndex == index:
                self._change_node_pointers_insertion(node.prev, node, val)
                return
            else:
                node = node.next
                currIndex += 1
        # edge case -- inserting node at the end of the linked list means we have a new tail node
        # so pointers have to be change appropriately for that
        if index == currIndex:
            self.add_at_tail(val)

    def _change_node_pointers_insertion(self, savedPrev, node, val):
        newNode = DoublyLinkedListNode(val)
        savedPrev = node.prev
        node.prev = newNode
        newNode.prev = savedPrev
        newNode.next = node
        savedPrev.next = newNode
        newNode.next = node

    def delete_at_index(self, index):
        if not self.head:
            return
        elif index == 0:
            if not self.head.next:
                self.head = None
                self.tail = None
                return
            else:
                newHead = self.head.next
                newHead.prev = None
                self.head = newHead
        else:
            self._unlink_node(index)

    def _unlink_node(self, index):
        currIndex = 0
        prevNode = None
        currNode = self.head
        while currNode and currIndex <= index:
            if index == currIndex:
                if not currNode.next:
                    prevNode.next = None
                    self.tail = prevNode
                else:
                    nextNode = currNode.next
                    prevNode.next = nextNode
                    nextNode.prev = prevNode
                return
            else:
                prevNode = currNode
                currNode = currNode.next
                currIndex += 1
