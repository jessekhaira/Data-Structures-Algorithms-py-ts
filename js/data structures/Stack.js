class StackNode{
    constructor(val) {
        this.val = val;
        this.prev = null;
        this.next = null; 
    }
}

class Stack {
    constructor() {
        this.tail = null; 
    }

    push(val) {
        let node = new StackNode(val);
        if (this.tail) {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node; 
        }
        else {
            this.tail = node; 
        }
    }

    
}