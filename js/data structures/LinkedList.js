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

    get(index) {
        let currIdx = 0;
        let node = this.head;
        while (node && currIdx <= index) {
            if (currIdx === index) {
                return node.val;
            }
            else {
                currIdx++;
                node = node.next; 
            }
        }
        return -1; 
    }
}