class QueueNode:
    def __init__(self, val):
        self.val = val
        self.next = None 

class Queue:
    def __init__(self):
        self.head = None
    