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

    addAtIndex(index, val) {
        if (index === 0) {
            this.addAtHead(val);
        }
        else {
            this._insertNode(index, val);
        }
    }

    _insertNode(index, val) {
        let currIdx = 0;
        let newNode = new DoubleLinkedListNode(val);
        let node = this.head;
        while (node && currIdx <= index) {
            if (currIdx === index) {
                this._linkNodes(node, newNode);
                return; 
            }
            else {
                currIdx++;
                node = node.next; 
            }
        }
        if (currIdx === index) {
            this.addAtTail(val); 
        }
    }

    _linkNodes(node, newNode) {
        let savedPrev = node.prev;
        savedPrev.next = newNode;
        newNode.prev = savedPrev;

        newNode.next = node;
        node.prev = newNode;
    }

    deleteAtIndex(index) {
        if (!this.head) {
            return;
        }
        else if (index === 0) {
            if (!this.head.next) {
                this.head = null;
                this.tail = null; 
            }
            else {
                let savedNext = this.head.next;
                savedNext.prev = null;
                this.head = savedNext; 
            }
        }
        else {
            this._unlinkNode(index);
        }
    }

    _unlinkNode(index) {
        let node = this.head;
        let prev = null; 
        let currIdx = 0; 
        while (node && currIdx <= index) {
            if (currIdx === index) {
                if (!node.next) {
                    prev.next = null;
                    this.tail = prev;
                }
                else {
                    let savedNext = node.next;
                    prev.next = savedNext;
                    savedNext.prev = prev; 
                }
                return; 
            }
            else {
                prev = node; 
                node = node.next;
                currIdx++; 
            }
        }
    }
}