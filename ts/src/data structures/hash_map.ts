/**
 * @fileoverview This module contains code for a class that represents the
 * HashMap data structure
 * @package
 */

/**
 *  This class represents a node used to resolve collisons in a HashMap.
 * @public
 * @constructor
 */
class ChainingNode<K, V> {
    key: K;

    val: V;

    next: null | ChainingNode<K, V>;

    /**
     *
     * @param {number} key Value of any type representing the key being
     * hashed into the HashMap
     * @param {number } val Value of any type representing the value being
     * hashed into the HashMap
     */
    constructor(key: K, val: V) {
        this.key = key;
        this.val = val;

        /**
         * @type {null|ChainingNode} Node the current node is linked to
         */
        this.next = null;
    }
}

/**
 *  This class represents a HashMap class that accepts number inputs. All
 *  methods of a HashMap are supported by this class -> put, remove, get, with
 *  dynamic array resizing.
 * 
 *  HashMaps are built on top of static arrays. This class assumes an initial
 *  capacity of a static array of 1000, with a load factor equal to 0.75. When
 *  the load factor is exceeded, dynamic array resizing is done to ensure O(1)
 *  TS lookups, removals, and additions.
 * @public
 * @constructor

 */
class HashMap<V> {
    buckets: (null | ChainingNode<number, V>)[];

    loadFactor: number;

    capacity: number;

    /**
     * @param {number} k Initial capacity of the static array. Default is 3000.
     * @param {number} loadFactor Target load factor for the HashMap. Goal is
     *      to keep below 0.75.
     */
    constructor(k = 3000, loadFactor = 0.75) {
        this.buckets = [];
        for (let i = 0; i < k; i += 1) {
            this.buckets.push(null);
        }
        this.loadFactor = loadFactor;
        this.capacity = 0;
    }

    /**
     *  This method puts a value within the hash table according to its hash
     *  value, with the keys assumed to be integers. 
        
     * Time:
     * - O(1) best/avg
     * - O(N) worst
     * 
     * Space:
     * - O(1) best/avg/worst  
     * 
     * N - number of items hashed into HashMap 
     * @param {Number} key Number representing the key to hash into
     * the hash table
     * @param {any} val Value of any type associated with the key being
     * hashed into the hash table
     */
    put(key: number, val: V): void {
        /*
        get the hash value and look at the bucket in the hash table where this
        key should be inserted if the bucket is empty, then insert the key-value
        pair directly into the bucket by inserting node of new linkedlist.
        Otherwise, add the key-value pair to the end of the linkedlist that 
        exists in the bucket 
        */
        const hashVal = this.hashFunc(key);
        if (this.buckets[hashVal] === null) {
            this.buckets[hashVal] = new ChainingNode(key, val);
        } else {
            let currNode = this.buckets[hashVal];
            if (currNode) {
                while (currNode.next && currNode.key !== key) {
                    currNode = currNode.next;
                }
                if (currNode.key !== key) {
                    currNode.next = new ChainingNode(key, val);
                    this.capacity += 1;
                    if (
                        Math.floor(this.capacity / this.buckets.length) >=
                        this.loadFactor
                    ) {
                        this._rehash();
                    }
                } else {
                    currNode.val = val;
                }
            }
        }
    }

    /**
     * Method used to double the size of the array underlying the
     * HashMap when the load factor of the HashMap is exceeded.
     */
    _rehash(): void {
        const savedArr = this.buckets;
        this.buckets = [];
        for (let i = 0; i < savedArr.length * 2; i += 1) {
            this.buckets.push(null);
        }
        savedArr.forEach((pointer) => {
            if (pointer) {
                let currNode = pointer as ChainingNode<number, V> | null;
                while (currNode) {
                    const currK = currNode.key;
                    const currV = currNode.val;
                    currNode = currNode.next;
                    this.put(currK, currV);
                }
            }
        });
    }

    /**
     * This function retrieves the value associated with the given input key,
     * if it exists within the hashtable. 

     * Time:
     * - O(1) best/avg
     * - O(N) worst
     * 
     * Space:
     * - O(1) best/avg/worst  
     * 
     * N - number of items hashed into HashMap 
     * @param {number} key Integer representing the key to lookup in the
     * hashtable.
     * @returns {any} The value associated with the key in the hashtable. If
     * the key doesn't exist in the table, then null will be returned. 
     */
    get(key: number): V | null {
        /*
            look up the bucket in the hashtable the key should be residing in 
            and if nothing exists in that bucket, return none. Otherwise,
            traverse the linked list that exists in that bucket until there
            is nothing left or the appropriate key is found.
        */
        const hashVal = this.hashFunc(key);
        if (this.buckets[hashVal] === null) {
            return null;
        }

        let currNode = this.buckets[hashVal];
        while (currNode && currNode.key !== key) {
            currNode = currNode.next;
        }
        if (!currNode) {
            return null;
        }
        return currNode.val;
    }

    /**
     * If the input key is within the hashtable, this method removes the
     * key-value pair from the hashtable.
     *
     * Time:
     * - O(1) best/avg
     * - O(N) worst
     *
     * Space:
     * - O(1) best/avg/worst
     *
     * N - number of items hashed into HashMap
     * @param {Number} key Number representing a key that may be present in
     * the hashtable
     * @returns {null}
     */
    remove(key: number): null {
        const hashVal = this.hashFunc(key);
        if (this.buckets[hashVal] === null) {
            return null;
        }

        let currNode = this.buckets[hashVal];
        let prevNode = null;
        while (currNode && currNode.key !== key) {
            prevNode = currNode;
            currNode = currNode.next;
        }
        if (!currNode) {
            return null;
        }
        this.capacity -= 1;
        if (!prevNode) {
            this.buckets[hashVal] = currNode.next;
            return null;
        }
        prevNode.next = currNode.next;
        return null;
    }

    /**
     *  This function represents the hashing algorithm being used for
     *  the hashmap. This function takes integers as inputs and produces
     *  the bucket within the hashmap the integer falls into. 

     *Time:
     *- O(1) best/avg/worst
        
     * Space:
     *- O(1) best/avg/worst
            
     * @param {number} key Integer input to be hashed into the hashmap
     * @returns {number} Integer representing the index within the hashmap
     * the key falls into
     */
    hashFunc(key: number): number {
        return key % this.buckets.length;
    }
}

export default HashMap;
