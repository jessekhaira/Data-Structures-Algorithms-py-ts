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

    addAtHead(val) {
        let newNode = new DoubleLinkedListNode(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            this.head.prev = newNode;
            newNode.next = this.head;
            this.head = newNode; 
        }
    }

    addAtTail(val) {
        let newNode = new DoubleLinkedListNode(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
    }
}