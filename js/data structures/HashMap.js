/**
 *  This class represents a Linked List node used to resolve
    collisons in a HashMap.

 * @public
 * @constructor
 */
class ChainingNode {
    /**
     * 
     * @param {number} key Integer representing the key being hashed into the HashMap
     * @param {number } val Integer representing the value being hashed into the HashMap
     */
    constructor(key,val) {
        this.key = key;
        this.val =val;

        /**
         * @type {null|ChainingNode} Node the current node is linked to 
         */
        this.next = null;
    }
}


/**
 *  This class represents a HashMap class that accepts integer inputs. All methods
    of a HashMap are supported by this class -> put, remove, get, with dynamic array 
    resizing. 

    HashMaps are built on top of static arrays. This class assumes an initial capacity
    of a static array of 1000, with a load factor equal to 0.75. When the load factor
    is exceeded, dynamic array resizing is done to ensure O(1) TS lookups, removals, and
    additions. Hash collisons are handled through chaining with Linked Lists. 

 * @public
 * @constructor

 */
class HashMap {
    /**
     * @param {number} k Initial capacity of the static array. Default is 3000.
     * @param {number} loadFactor Target load factor for the HashMap. Goal is to keep below 0.75. 
     */
    constructor(k=3000, loadFactor=0.75) {
        this.buckets = Array(k).fill(null);
        this.loadFactor = loadFactor;
        this.capacity = 0; 
    }

    /**
     *  This method puts a value within the hash table according to its hash value, with the keys
        assumed to be integers. 

        Time:
            - O(1) best/avg
            - O(N) worst 
        Space:
            - O(1) best/avg
            - O(N) worst

     * @param {Number} key Integer representing the key to hash into the hash table
     * @param {any} val Value associated with the key being hashed into the hash table
     * @returns {undefined} 
     */
    put (key, val) {
        /*
        get the hash value and look at the bucket in the hash table where this key should be inserted
        if the bucket is empty, then insert the key-value pair directly into the bucket by inserting
        node of new linkedlist. Otherwise, add the key-value pair to the end of the linkedlist that 
        exists in the bucket 
        */ 
        let hashVal = this.hashFunc(key);
        if (this.buckets[hashVal] === null) {
            this.buckets[hashVal] = new ChainingNode(key, val);
        }
        else {
            let currNode = this.buckets[hashVal];
            while (currNode.next && currNode.key !== key) {
                currNode = currNode.next;
            }
            if (currNode.key !== key) {
                currNode.next = new ChainingNode(key, val);
                this.capacity++;
                if (Math.floor(this.capacity/this.buckets.length) >= this.loadFactor) {
                    this._rehash();
                }
            }
            else {
                currNode.val = val; 
                return; 
            }
        }
    }

    /**
     * Method used to double the size of the array underlying the HashMap when the load factor of the 
     * HashMap is exceeded. 
     */
    _rehash() {
        let savedArr = this.buckets;
        this.buckets = Array(this.buckets.length*2).fill(null);
        for (let pointer of savedArr) {
            if (pointer) {
                while (pointer) {
                    let currK = pointer.key;
                    let currV = pointer.val;
                    pointer = pointer.next; 
                    this.put(currK, currV); 
                }
            }
        }
    }

    /**
     * This function retrieves the value associated with the given input key, if it exists within the 
        hashtable. 

        Time:
            - O(1) best/avg
            - O(N) worst
        Space:
            - O(1) best/avg/worst  

     * @param {number} key Integer representing the key to lookup in the hashtable.
     * @returns {any} The value associated with the key in the hashtable. If the key doesn't exist 
                in the table, then null will be returned. 
     */
    get (key) {
        /*
            look up the bucket in the hashtable the key should be residing and if nothing exists in that
            bucket, return none. Otherwise, traverse the linked list that exists in that bucket until there
            is nothing left or the appropriate key is found.
        */  
        let hashVal = this.hashFunc(key);
        if (this.buckets[hashVal] === null) {
            return null;
        }
        else {
            let currNode = this.buckets[hashVal];
            while(currNode && currNode.key !== key) {
                currNode =currNode.next; 
            }
            if (!currNode) {
                return null;
            }
            return currNode.val;
        }
    }

    remove(key) {
        let hashVal = this.hashFunc(key);
        if (this.buckets[hashVal] === null) {
            return null; 
        }
        else {
            let currNode = this.buckets[hashVal];
            let prevNode = null; 
            while (currNode && currNode.key !== key) {
                prevNode = currNode; 
                currNode = currNode.next;
            }
            if (!currNode) {
                return null; 
            }
            this.capacity--;
            if (!prevNode) {
                this.buckets[hashVal] = currNode.next; 
                return;
            }
            prevNode.next = currNode.next;
            return; 
        }
    }

    hashFunc(key) {
        return key % this.buckets.length;
    }
}

export {HashMap};