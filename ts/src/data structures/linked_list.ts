import { DoubleLinkedListNode } from '../utils/linked_list_utility';

/**
 * This class represents a double linked list.
 */
class DoubleLinkedList<T> {
    head: DoubleLinkedListNode<T> | null;

    tail: DoubleLinkedListNode<T> | null;

    constructor(val: T) {
        this.head = new DoubleLinkedListNode(val);
        this.tail = this.head;
    }

    get(index: number): T | -1 {
        let currIdx = 0;
        let node = this.head;
        while (node && currIdx <= index) {
            if (currIdx === index) {
                return node.val;
            }

            currIdx += 1;
            node = node.next;
        }
        return -1;
    }

    addAtHead(val: T): void {
        const newNode = new DoubleLinkedListNode(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.head.prev = newNode;
            newNode.next = this.head;
            this.head = newNode;
        }
    }

    addAtTail(val: T): void {
        const newNode = new DoubleLinkedListNode(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else if (this.tail) {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
    }

    addAtIndex(index: number, val: T): void {
        if (index === 0) {
            this.addAtHead(val);
        } else {
            this._insertNode(index, val);
        }
    }

    _insertNode(index: number, val: T): void {
        let currIdx = 0;
        const newNode = new DoubleLinkedListNode(val);
        let node = this.head;
        while (node && currIdx <= index) {
            if (currIdx === index) {
                DoubleLinkedList._linkNodes(node, newNode);
                return;
            }

            currIdx += 1;
            node = node.next;
        }
        if (currIdx === index) {
            this.addAtTail(val);
        }
    }

    static _linkNodes<K>(
        node: DoubleLinkedListNode<K>,
        newNode: DoubleLinkedListNode<K>,
    ): void {
        const savedPrev = node.prev;
        if (savedPrev) {
            savedPrev.next = newNode;
            newNode.prev = savedPrev;

            newNode.next = node;
            node.prev = newNode;
        }
    }

    deleteAtIndex(index: number): void {
        if (this.head) {
            if (index === 0) {
                if (!this.head.next) {
                    this.head = null;
                    this.tail = null;
                } else {
                    const savedNext = this.head.next;
                    savedNext.prev = null;
                    this.head = savedNext;
                }
            } else {
                this._unlinkNode(index);
            }
        }
    }

    _unlinkNode(index: number): void {
        let node = this.head;
        let prev = null;
        let currIdx = 0;
        while (node && currIdx <= index) {
            if (currIdx === index && prev) {
                if (!node.next) {
                    prev.next = null;
                    this.tail = prev;
                } else {
                    const savedNext = node.next;
                    prev.next = savedNext;
                    savedNext.prev = prev;
                }
            }

            prev = node;
            node = node.next;
            currIdx += 1;
        }
    }
}

export default DoubleLinkedList;
