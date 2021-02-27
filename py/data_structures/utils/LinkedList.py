class DoublyLinkedListNode:
    """
    This class represents a node meant to be used within doubly linked lists.
    """ 
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None 

class SinglyLinkedListNode:
    """
    This class represents a node meant to be used within singly linked lists.
    """ 
    def __init__(self, val):
        self.val = val
        self.next = None