import { DoubleLinkedListNode } from '../utils/linked_list_utility';
/**
 * This class represents the data structure known as a Deque,
 * implemented using doubly linked list
 * nodes.
 * @class @public
 */
class Deque<T> {
    head: null | DoubleLinkedListNode<T>;

    tail: null | DoubleLinkedListNode<T>;

    constructor() {
        this.head = null;
        this.tail = null;
    }

    /**
     * This method is used to return the first value stored inside of the
     * deque
     * @returns {T} Argument of type T, representing the first value inside
     * of the deque
     */
    peekFirst(): T {
        if (this.head) {
            return this.head.val;
        }

        throw Error('peek in empty deque');
    }

    /**
     * This method is used to return the last value stored inside of the
     * deque
     * @returns {T} Argument of type T, representing the last value inside
     * of the deque
     */
    peekLast(): T {
        if (this.tail) {
            return this.tail.val;
        }

        throw Error('peek in empty deque');
    }

    /**
     * This method is used to remove and return the first value stored
     * inside of the deque
     * @returns {T} Argument of type T, representing the first value inside
     * of the deque
     */
    popFirst(): T {
        if (this.head) {
            const retvalue = this.head.val;
            const newHead = this.head.next;
            if (newHead) {
                newHead.prev = null;
                this.head.next = null;
                this.head = newHead;
            } else {
                this.head = null;
                this.tail = null;
            }
            return retvalue;
        }

        throw Error('pop from empty deque');
    }

    popLast(): T {
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

    addFirst(value: T): void {
        const newHead = new DoubleLinkedListNode(value);
        if (this.head) {
            newHead.next = this.head;
            this.head.prev = newHead;
            this.head = newHead;
        } else {
            this.head = newHead;
            this.tail = newHead;
        }
    }

    addLast(value: T): void {
        const newTail = new DoubleLinkedListNode(value);
        if (this.tail) {
            newTail.prev = this.tail;
            this.tail.next = newTail;
            this.tail = newTail;
        } else {
            this.head = newTail;
            this.tail = newTail;
        }
    }

    length(): number {
        let length = 0;
        let node = this.head;
        while (node) {
            length += 1;
            node = node.next;
        }
        return length;
    }
}

export default Deque;
