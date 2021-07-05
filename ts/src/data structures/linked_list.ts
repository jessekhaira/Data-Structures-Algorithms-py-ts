import { DoubleLinkedListNode } from '../utils/linked_list_utility';

/**
 * This class represents a double linked list.
 */
class DoubleLinkedList<T> {
    head: DoubleLinkedListNode<T>;

    tail: DoubleLinkedListNode<T>;

    constructor(val: T) {
        this.head = new DoubleLinkedListNode(val);
        this.tail = this.head;
    }

    get(index) {
        let currIdx = 0;
        let node = this.head;
        while (node && currIdx <= index) {
            if (currIdx === index) {
                return node.val;
            }

            currIdx++;
            node = node.next;
        }
        return -1;
    }

    addAtHead(val) {
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

    addAtTail(val) {
        const newNode = new DoubleLinkedListNode(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
    }

    addAtIndex(index, val) {
        if (index === 0) {
            this.addAtHead(val);
        } else {
            this._insertNode(index, val);
        }
    }

    _insertNode(index, val) {
        let currIdx = 0;
        const newNode = new DoubleLinkedListNode(val);
        let node = this.head;
        while (node && currIdx <= index) {
            if (currIdx === index) {
                this._linkNodes(node, newNode);
                return;
            }

            currIdx++;
            node = node.next;
        }
        if (currIdx === index) {
            this.addAtTail(val);
        }
    }

    _linkNodes(node, newNode) {
        const savedPrev = node.prev;
        savedPrev.next = newNode;
        newNode.prev = savedPrev;

        newNode.next = node;
        node.prev = newNode;
    }

    deleteAtIndex(index) {
        if (!this.head) {
        } else if (index === 0) {
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

    _unlinkNode(index) {
        let node = this.head;
        let prev = null;
        let currIdx = 0;
        while (node && currIdx <= index) {
            if (currIdx === index) {
                if (!node.next) {
                    prev.next = null;
                    this.tail = prev;
                } else {
                    const savedNext = node.next;
                    prev.next = savedNext;
                    savedNext.prev = prev;
                }
                return;
            }

            prev = node;
            node = node.next;
            currIdx++;
        }
    }
}

export { DoubleLinkedList };
