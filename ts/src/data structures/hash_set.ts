import { SingleLinkedListNode } from '../utils/linked_list_utility';
/**
 * This class represents a Hash Set designed specifically to accept
 * integer values. Hash collisons are dealt with through chaining with
 * linked lists.
 *
 * A HashSet is a data structure built on static arrays which is meant
 * to hold a collection of unique items.
 */
class HashSet {
    constructor(init_capacity = 1000, load_factor = 0.75) {
        this._buckets = Array(init_capacity).fill(null);
        this._design_load_factor = load_factor;
        this._curr_items_hashed = 0;
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
    add(key) {
        const hashVal = this._hashing_algorithm(key);
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
            prev.next = newNode;
        }

        this._curr_items_hashed++;
        const currLoadFactor = this._curr_items_hashed / this._buckets.length;
        if (currLoadFactor >= this._design_load_factor) {
            this.rehash();
        }
    }

    /**
     * This method is used to dynamically resize the array underlying the hashset in order to keep all operations efficient.
     * This method is invoked by the add method, when adding a key to the hashset causes the current load factor to exceed
     * the design load factor.
     */
    rehash() {
        const savedBuckets = this._buckets;
        this._curr_items_hashed = 0;
        this._buckets = Array(savedBuckets.length * 2).fill(null);
        for (let node of savedBuckets) {
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
    remove(key) {
        const hashVal = this._hashing_algorithm(key);
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
     * Returns a boolean indicating whether or not the hash set contains the integer input argument.

     *Time:
     * - O(1) best/avg
     * - O(N) worst
     * 
     * Space:
     * - O(1) best/avg/worst  
     * 
     * N - length of hash set 
     * @param {number} key Integer input argument  
     * @returns {boolean} Boolean indicating whether the hash set contains the integer input
     */
    contains(key) {
        const hashVal = this._hashing_algorithm(key);
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
     * @param {Number} key Integer representing number to generate a hash code for
     * @returns {Number} Integer representing the index in the hashset to hash the key into
     */
    _hashing_algorithm(key) {
        return key % this._buckets.length;
    }
}

export { HashSet };
