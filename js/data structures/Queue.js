
/**
 * This class represents an object meant to be stored in the Queue data structure.
 */
class QueueNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

/**
 * This class represents the Queue data structure.
 */
class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    push(val) {
        const newNode = new QueueNode(val);
        if(!this.head) {
            this.head = newNode;
            this.tail = newNode;
        }
        else {
            this.tail.next = newNode;
            this.tail = newNode;
        }
    }
    
    top() {
        if (this.head) {
            return this.head.val;
        }
        
        else {
            throw Error('empty queue');
        }
    }

    pop() {
        if (this.head) {
            let newHead = this.head.next;
            this.head = newHead;
        }
        else {
            throw Error('pop from empty queue');
        }
    }
}