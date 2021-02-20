class DequeNode:
    """
    This class represents a node based off a doubly linked list node, meant to be used
    within the Deque data structure.
    """ 
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque:
    """
    This class represents the deque data structure. 
    """ 
    def __init__(self):
        self.head = None
        self.tail = None
    
    def peek_first(self):
        if self.head:
            return self.head.val
        else:
            raise IndexError("peek first in empty deque")
    
    def peek_last(self):
        if self.tail:
            return self.tail.val
        else:
            raise IndexError("peek last in empty deque")

    def add_first(self, val):
        new_head = DequeNode(val)
        if self.head:
            self.head.prev = new_head
            new_head.next = self.head
            self.head = new_head
        else:
            self.head = new_head
            self.tail = new_head
    
    def add_last(self, val):
        new_tail = DequeNode(val)
        if self.tail:
            self.tail.next = new_tail
            new_tail.prev = self.tail 
            self.tail = new_tail
        else:
            self.head = new_tail
            self.tail = new_tail

    def pop_first(self):
        if self.head:
            saved_val = self.head.val
            new_head = self.head.next 
            new_head.prev = None
            self.head = new_head
            return saved_val
        else:
            raise IndexError("pop from empty deque")

    def pop_last(self):
        if self.tail:
            saved_val = self.tail.val
            new_tail = self.tail.prev
            new_tail.next = None 
            self.tail = new_tail
            return saved_val
        else:
            raise IndexError("pop form empty deque")

    def __len__(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next 
        return length 