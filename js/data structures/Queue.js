
/**
 * This class represents an object meant to be stored in the queue data structure.
 */
class QueueNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

/**
 * This class represents the queue data structure.
 */
class Queue {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    /**
     * This method pushes a node onto the queue with the input value. 
     * @param {any} val Number to be stored in the queue
     */
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

    /**
     * This method returns the first element stored in the queue
     * @returns {any} First element stored in the queue 
     */
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

    length() {
        let length = 0;
        let node = this.head;
        while (node) {
            length++;
            node = node.next; 
        }
        return length; 
    }
}

export {Queue}; 