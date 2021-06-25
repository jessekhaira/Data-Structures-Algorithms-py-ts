import { DoubleLinkedListNode } from './utils/LinkedList';
/**
 * This class represents the data structure known as a Deque, implemented using doubly linked list
 * nodes.
 * @class @public
 */
class Deque<T> {
    head: null | DoubleLinkedListNode;

    tail: null | DoubleLinkedListNode;

    constructor() {
        this.head = null;
        this.tail = null;
    }

    peekFirst(): T {
        if (this.head) {
            return this.head.val;
        }

        throw Error('peek in empty deque');
    }

    peekLast() {
        if (this.tail) {
            return this.tail.val;
        }

        throw Error('peek in empty deque');
    }

    popFirst() {
        if (this.head) {
            const retvalue = this.head.val;
            const new_head = this.head.next;
            if (new_head) {
                new_head.prev = null;
                this.head.next = null;
                this.head = new_head;
            } else {
                this.head = null;
                this.tail = null;
            }
            return retvalue;
        }

        throw Error('pop from empty deque');
    }

    popLast() {
        if (this.tail) {
            const retvalue = this.tail.val;
            const newTail = this.tail.prev;
            if (newTail) {
                newTail.next = null;
                this.tail.prev = null;
                this.tail = newTail;
            } else {
                this.head = null;
                this.tail = null;
            }
            return retvalue;
        }

        throw Error('pop from empty deque');
    }

    addFirst(value) {
        const new_head = new DoubleLinkedListNode(value);
        if (this.head) {
            new_head.next = this.head;
            this.head.prev = new_head;
            this.head = new_head;
        } else {
            this.head = new_head;
            this.tail = new_head;
        }
    }

    addLast(value) {
        const new_tail = new DoubleLinkedListNode(value);
        if (this.tail) {
            new_tail.prev = this.tail;
            this.tail.next = new_tail;
            this.tail = new_tail;
        } else {
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

export { Deque };
