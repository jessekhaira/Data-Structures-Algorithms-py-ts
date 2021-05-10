/**
 * This class represents a doubly linked node, where every node has two pointers. Meant to be used within
 * a doubly linked list. 
 * @class @public 
 */
class DoubleLinkedListNode {
    constructor(val) {
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}
/**
 * This class represents a singly linked node, where every node has one pointer. Meant to be used within a
 * singly linked list. 
 * @class @public 
 */
 class SingleLinkedListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

export {DoubleLinkedListNode, SingleLinkedListNode}; 