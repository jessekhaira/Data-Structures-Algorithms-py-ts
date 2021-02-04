class DoubleLinkedListNode {
    constructor(val) {
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}


/**
 * This class represents a double linked list. 
 */
class DoubleLinkedList {
    constructor(val) {
        this.head = new DoubleLinkedListNode(val);
        this.tail = this.head; 
    }
}