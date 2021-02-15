class QueueNode:
    def __init__(self, val):
        self.val = val
        self.next = None 

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None 
    
    def push(self, val):
        new_node = QueueNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def poll(self):
        if self.head:
            return_val = self.head.val
            self.head = self.head.next 
        else:
            raise IndexError("poll from empty queue")