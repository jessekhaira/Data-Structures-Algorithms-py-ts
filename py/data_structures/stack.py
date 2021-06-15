""" This module contains code for a class that represents the
stack data structure """
from py.utils.linked_list import DoublyLinkedListNode
from typing import Any


class Stack:
    """ This class represents the stack data structure, built using
    pythons doubly linked list nodes. The basic principle of the stack is
    Last In First Out (LIFO), where the last element added will be
    the first one removed (like a stack of plates).

    Stacks are very useful in cases where you want to process a nested
    data structure, or for functions that call other functions, even
    themselves. It follows that common use cases for stacks are for
    implementing backtracking algorithms, parsers, and so on.

    Attributes:
        tail:
            The doubly linked list node on top of the stack
    """

    def __init__(self):
        self.tail = None

    def push(self, val: Any) -> None:
        """ This method wraps the input value, which can be of any type,
        inside of a doubly linked list node and pushes it on top of
        the stack.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Args:
            val:
                Value of any type to be pushed on top of the stack
        """
        new_node = DoublyLinkedListNode(val)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.tail = new_node

    def pop(self) -> Any:
        """ This method removes the node on top of the stack and returns
        the value contained within it.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Returns:
            Value of any type representing the value stored inside of the node
            on top of the stack

        Raises:
            IndexError:
                If there is no node within the stack, the method will raise an
                error that the operation cannot be done
        """
        if self.tail:
            # have to deal with edge case of deleting stack with one node in it
            old_tail_val = self.tail.val
            if self.tail.prev:
                new_tail = self.tail.prev
                new_tail.next = None
                self.tail = new_tail
            else:
                self.tail = None
            return old_tail_val
        else:
            raise IndexError("pop from empty stack")

    def top(self) -> Any:
        """ This method returns the value contained within the node
        on top of the stack

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Returns:
            Value of any type representing the value stored inside of the node
            on top of the stack

        Raises:
            IndexError:
                If there is no node within the stack, the method will raise an
                error that the operation cannot be done
        """
        if self.tail:
            return self.tail.val
        else:
            raise IndexError("empty stack")

    def __len__(self):
        """ This method returns the number of nodes inside of the stack.

        Time:
            O(N) best/average/worst

        Space:
            O(1) best/average/worst

        Where N is the number of nodes stored inside the stack currently

        Returns:
            Integer representing the number of nodes stored inside the stack
        """
        length = 0
        node = self.tail
        while node:
            length += 1
            node = node.prev
        return length
