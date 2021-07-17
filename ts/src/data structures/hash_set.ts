import { SingleLinkedListNode } from '../utils/linked_list_utility';
/**
 * This class represents a Hash Set designed specifically to accept asdjkasdjkasjkdaskjdnjsakdknjsadknjas
 * integer values. Hash collisons are dealt with through chaining with
 * linked lists.
 *
 * A HashSet is a data structure built on static arrays which is meant
 * to hold a collection of unique items.
 */
class HashSet {
    _buckets: (null | SingleLinkedListNode<number>)[];

    _designLoadFactor: number;

    _currItemsHashed: number;

    constructor(initCapacity = 1000, loadFactor = 0.75) {
        this._buckets = HashSet.fillBuckets(initCapacity);
        this._designLoadFactor = loadFactor;
        this._currItemsHashed = 0;
    }

    /**
     * Inserts the input argument, expected to be an integer, into
     * the hash set. If by adding the element, the design load
     * factor is exceeded, rehashing is done.
     *
     * Time:
     * - O(1) best/avg
     * - O(N) worst
     *
     * Space:
     * - O(1) best/avg/worst
     *
     * N - length of hash set
     * @param {number} key Argument to hash into hashset
     */
    add(key: number): void {
        const hashVal = this._hashingAlgorithm(key);
        const newNode = new SingleLinkedListNode(key);
        if (!this._buckets[hashVal]) {
            this._buckets[hashVal] = newNode;
        } else {
            let node = this._buckets[hashVal];
            let prev = null;
            while (node) {
                if (node.val === key) {
                    return;
                }
                prev = node;
                node = node.next;
            }
            if (prev) prev.next = newNode;
        }

        this._currItemsHashed += 1;
        const currLoadFactor = this._currItemsHashed / this._buckets.length;
        if (currLoadFactor >= this._designLoadFactor) {
            this.rehash();
        }
    }

    static fillBuckets<T>(length: number): (null | T)[] {
        const buckets: (null | T)[] = [];
        for (let i = 0; i < length; i += 1) {
            buckets.push(null);
        }
        return buckets;
    }

    /**
     * This method is used to dynamically resize the array underlying the
     * hashset in order to keep all operations efficient. This method is
     * invoked by the add method, when adding a key to the hashset causes
     * the current load factor to exceed the design load factor.
     */
    rehash(): void {
        const savedBuckets = this._buckets;
        this._currItemsHashed = 0;
        this._buckets = HashSet.fillBuckets(savedBuckets.length * 2);
        for (let i = 0; i < this._buckets.length; i += 1) {
            let node = this._buckets[i];
            while (node) {
                this.add(node.val);
                node = node.next;
            }
        }
    }

    /**
     * Removes the Number input from the hashset if it is stored in the hashset.
     *
     * Time:
     * - O(1) best/avg
     * - O(N) worst
     *
     * Space:
     * - O(1) best/avg/worst
     *
     * N - length of hashset
     * @param {Number} key Number to remove from the hashset
     * @returns {undefined}
     */
    remove(key: number): void {
        const hashVal = this._hashingAlgorithm(key);
        let node = this._buckets[hashVal];
        let prev = null;
        while (node) {
            if (node.val === key) {
                if (!prev) {
                    this._buckets[hashVal] = node.next;
                } else {
                    prev.next = node.next;
                }
                return;
            }

            prev = node;
            node = node.next;
        }
    }

    /**
     * Returns a boolean indicating whether or not the hash set contains the
     * integer input argument.

     *Time:
     * - O(1) best/avg
     * - O(N) worst
     * 
     * Space:
     * - O(1) best/avg/worst  
     * 
     * N - length of hash set 
     * @param {number} key Integer input argument  
     * @returns {boolean} Boolean indicating whether the hash set contains
     * the integer input
     */
    contains(key: number): boolean {
        const hashVal = this._hashingAlgorithm(key);
        let node = this._buckets[hashVal];
        while (node) {
            if (node.val === key) {
                return true;
            }

            node = node.next;
        }
        return false;
    }

    /**
     * This is a hashing algorithm that generates hash codes for integer keys.
     * @param {Number} key Integer representing number to generate
     * a hash code for
     * @returns {Number} Integer representing the index in the hashset
     * to hash the key into
     */
    _hashingAlgorithm(key: number): number {
        return key % this._buckets.length;
    }
}

export default HashSet;
