class DoublyLinkedListNode:
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
        while currIndex <= index:
            if currIndex == index:
                return node
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
        else:
            newNode = DoublyLinkedListNode(val)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def add_at_tail(self, val):            
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
            newNode.next = self.head 
            self.head.prev = newNode
            self.tail = self.head
            self.head = newNode
        else:
            node = self.head 
            currIndex = 0 
            while node and currIndex <= index:
                if currIndex == index:
                    savedPrev = node.prev 
                    node.prev = newNode
                    newNode.prev = savedPrev
                    newNode.next = node 
                else:
                    node = node.next 
                    currIndex += 1 
            
            if index == currIndex + 1:
                self.tail.next = node
                node.prev = self.tail 
                self.tail = node


    def delete_at_index(self, index):
        if index == 0:
            if not self.head.next:
                self.head = None 
                self.tail = None
                return 
            else:
                newHead = self.head.next 
                self.head = newHead 
        else:
            currIndex = 0
            prevNode = None
            currNode = self.head 
            while currNode and currIndex <= index:
                if index == currIndex:
                    nextNode = currNode.next 
                    prevNode.next = nextNode
                    nextNode.prev = prevNode
                    currNode = nextNode
                else:
                    prevNode = currNode
                    currNode = currNode.next
                    currIndex += 1 
            
            if index == currIndex + 1:
                prevNode.next = None
                self.tail = prevNode
            




