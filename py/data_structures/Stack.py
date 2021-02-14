class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None 
        self.prev = None 

class Stack:
    def __init__(self):
        self.tail = None

    def push(self,val):
        new_node = StackNode(val)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
        else:
            self.tail = new_node

    def pop(self):
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
    
    def top(self):
        if self.tail:
            return self.tail.val
        else:
            raise IndexError("empty stack")

    def __len__(self):
        length = 0
        node = self.tail 
        while node:
            length += 1
            node = node.prev
        return length 

 