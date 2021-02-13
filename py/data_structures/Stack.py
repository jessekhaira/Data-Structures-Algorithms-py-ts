class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None 
        self.prev = None 

class Stack:
    def __init__(self, val):
        self.head = StackNode(val)
        self.tail = self.head 
    
    def push(self,val):
        pass 