import { DoubleLinkedListNode } from '../utils/linked_list_utility';

/**
 * This class represents the data structure known as a Stack,
 * implemented using doubly linked list nodes.
 */
class Stack<T> {
    tail: null | DoubleLinkedListNode<T>;

    constructor() {
        this.tail = null;
    }

    /**
     * This method wraps the input value into a DoubleLinkedListNode
     * and pushes it on top of the stack.
     * @param {T} val Value of type T, specified when the stack is created
     */
    push(val: T): void {
        const node = new DoubleLinkedListNode(val);
        if (this.tail) {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node;
        } else {
            this.tail = node;
        }
    }

    /**
     * This method unwraps the value inside the DoubleLinkedListNode
     * on top of the stack and returns it.
     * @returns {T} Value of type T, specified when the stack is created
     */
    pop(): T {
        if (this.tail) {
            const oldTailVal = this.tail.val;
            if (this.tail.prev) {
                const newTail = this.tail.prev;
                newTail.next = null;
                this.tail = newTail;
            } else {
                this.tail = null;
            }
            return oldTailVal;
        }

        throw Error('pop from empty stack');
    }

    top(): T {
        if (this.tail) {
            return this.tail.val;
        }

        throw Error('empty stack');
    }

    length(): number {
        let size = 0;
        let node = this.tail;
        while (node) {
            size += 1;
            node = node.prev;
        }
        return size;
    }
}

export default Stack;
