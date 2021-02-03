class DoublyLinkedListNode:
    """
    This class represents a doubly linked list node, where every single node has two pointers.
    """ 
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None 

    

class DoublyLinkedList:
    """
    This class represents a doubly linked list. 
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
            newNode = DoublyLinkedListNode(val)
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
        newNode = DoublyLinkedListNode(val)
        if index == 0:
            if self.head:
                newNode.next = self.head 
                self.head.prev = newNode
                self.tail = self.head
                self.head = newNode
            else:
                self.head = newNode
                self.tail = newNode
        else:
            node = self.head 
            currIndex = 0 
            while node and currIndex <= index:
                if currIndex == index:
                    savedPrev = node.prev 
                    node.prev = newNode
                    newNode.prev = savedPrev
                    newNode.next = node 
                    savedPrev.next = newNode
                    newNode.next = node 
                    return 
                else:
                    node = node.next 
                    currIndex += 1 
            
            if index == currIndex:
                self.tail.next = newNode
                newNode.prev = self.tail 
                self.tail = newNode

    
                
    def delete_at_index(self, index):
        # have to deal with edge cases first of there not being any head node at all
        # and deleted the head node before we can go to unlinking code 
        if not self.head:
            return 
        elif index == 0:
            # edge case - linked list with only one node in it which is the head node 
            if not self.head.next:
                self.head = None 
                self.tail = None
                return 
            else:
                newHead = self.head.next 
                newHead.prev = None 
                self.head = newHead 
        else:
            self._unlink(index) 
            
    def _unlink(self, index):
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
        
            



    
            





