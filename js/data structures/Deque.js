class DequeNode() {
    construtor(val) {
        this.val = val;
        this.next = null;
        this.prev = null; 
    }
}

class Deque {
    constructor() {
        this.head = null;
        this.tail = null; 
    }

    peekFirst() {
        if (this.head) {
            return this.head.val;
        }
        else {
            throw Error("peek in empty deque")
        }
    }

    peekLast() {
        if (this.tail) {
            return this.tail.val;
        }
        else {
            throw Error("peek in empty deque")
        }
    }

    popFirst() {
        if (this.head) {
            const retVal = this.head.val;
            this.head = this.head.next; 
            this.head.prev = null; 
            return retVal;
        }
        else {
            throw Error("pop from empty deque"); 
        }
    }
    
    popLast() {
        if (this.tail) {
            const retVal = this.tail.val;
            this.tail = this.tail.prev;
            this.tail.next = null;
            return retVal;
        }
        else {
            throw Error("pop from empty deque");
        }

    }

    addFirst(val) {
        const new_head = new DequeNode(val); 
        if (this.head) {
            new_head.next = this.head;
            this.head.prev = new_head;
            this.head = new_head;
        }
        else {
            this.head = new_head;
            this.tail = new_head; 
        }
    }

    addLast(val) {
        const new_tail = new DequeNode(val);
        if (!this.tail) {
            new_tail.prev = this.tail;
            this.tail.next = new_tail;
            this.tail = new_tail;
        }
        else {
            this.head = new_tail;
            this.tail = new_tail;
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

export {Deque} 