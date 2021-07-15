/**
 * This class represents a singly linked node, where every node has one
 * pointer.
 * @class @public
 */
class SingleLinkedListNode<T> {
    next: null | SingleLinkedListNode<T>;
    val: T;
    constructor(val: T) {
        this.val = val;
        this.next = null;
    }
}
/**
 * This class represents a doubly linked node, where every node has two
 * pointers.
 * @class @public
 */
class DoubleLinkedListNode<T> {
    prev: null | DoubleLinkedListNode<T>;
    next: null | DoubleLinkedListNode<T>;
    val: T;
    constructor(val: T) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

export { DoubleLinkedListNode, SingleLinkedListNode };
