import { SingleLinkedListNode } from '../utils/linked_list_utility';

/**
 *  This class represents the Queue data structure implemented using
 *  singly linked nodes.
 *
 *  A queue consists of a sequence of entities managed using the First In
 *  First Out (FIFO) principle, where the first elements added are
 *  the first ones removed.
 *
 *  The queue has a variety of applications, including being used to traverse
 *  trees and graphs in a breadth first manner, in operating systems to maintain
 *  a queue of processes ready to execute, within computer systems, and so on.
 *
 *  Real world queues function in a conceptually similar way to digital queues.
 *  For example, we wait in queues any time we wait in a line, that most likely
 *  also follow the FIFO principle.
 */
class Queue<T> {
    head: null | SingleLinkedListNode<T>;

    tail: null | SingleLinkedListNode<T>;

    constructor() {
        /**
         * @param {SingleLinkedListNode | null} head Object of type null or
         * SingleLinkedListNode representing the first object in the queue
         * */
        this.head = null;
        /**
         * @param {SingleLinkedListNode| null} tail Object of type null or
         * SingleLinkedListNode representing the last object in the queue
         * */
        this.tail = null;
    }

    /**
     * This method pushes a node onto the queue with the input value.
     * @param {any} val Number to be stored in the queue
     */
    push(val: T): void {
        const newNode = new SingleLinkedListNode(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            if (this.tail) this.tail.next = newNode;
            this.tail = newNode;
        }
    }

    /**
     * This method returns the first element stored in the queue
     * @returns {any} First element stored in the queue
     */
    top(): T | void {
        if (this.head) {
            return this.head.val;
        }

        throw Error('empty queue');
    }

    pop(): T {
        if (this.head) {
            const returnVal = this.head.val;
            const newHead = this.head.next;
            this.head = newHead;
            return returnVal;
        }

        throw Error('pop from empty queue');
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

export default Queue;
