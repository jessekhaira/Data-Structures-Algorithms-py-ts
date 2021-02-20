class DequeNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Deque:
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
        pass

    def pop_last(self):
        pass

    def __len__(self):
        pass 