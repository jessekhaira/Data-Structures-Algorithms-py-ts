""" This module contains code for a class that represents the
doubly linked list data structure """
from typing import Any
from py.utils.linked_list import DoublyLinkedListNode


class DoublyLinkedList:
    """ This class represents the doubly linked list data
    structure.

    Attributes:
        val:
            Value of any type representing the data initially stored at
            the head node of the doubly linked list data structure
            
        head:
            Object of type DoublyLinkedListNode representing
            the head node of the data structure
        
        tail:
            Object of type DoublyLinkedListNode representing the
            tail node of the data structure, which on construction is
            equivalent to the tail node
    """

    def __init__(self, val: Any):
        self.head = DoublyLinkedListNode(val)
        self.tail = self.head

    def get(self, index: int) -> Any:
        curr_index = 0
        node = self.head
        while node and curr_index <= index:
            if curr_index == index:
                return node.val
            else:
                curr_index += 1
                node = node.next
        return -1

    def add_at_head(self, val: Any) -> None:
        """
        This function creates a doubly linked list node with the
        value given as input, and inserts the node to be the new
        head of the linked list.
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
        curr_index = 0
        while node and curr_index <= index:
            if curr_index == index:
                self._change_node_pointers_insertion(node.prev, node, val)
                return
            else:
                node = node.next
                curr_index += 1
        # edge case -- inserting node at the end of the linked list means we have a new tail node
        # so pointers have to be change appropriately for that
        if index == curr_index:
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
        curr_index = 0
        prevNode = None
        currNode = self.head
        while currNode and curr_index <= index:
            if index == curr_index:
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
                curr_index += 1
