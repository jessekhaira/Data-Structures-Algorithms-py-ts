class ChainingNode {
    /*
    This class represents a Linked List node used for chaining to resolve
    collisons in a HashMap class.

    Inputs:
        -> key (int): Integer representing the key being hashed into the HashMap
        -> value (int): Integer representing the value being hashed into the HashMap
    */
    constructor(key,val) {
        this.key = key;
        this.val =val;
        this.next = null;
    }
}

class HashMap {
    /*
    This class represents a HashMap class that accepts integer inputs. All methods
    of a HashMap are supported by this class -> put, remove, get, with dynamic array 
    resizing. 

    HashMaps are built on top of static arrays. This class assumes an initial capacity
    of a static array of 1000, with a load factor equal to 0.75. When the load factor
    is exceeded, dynamic array resizing is done to ensure O(1) TS lookups, removals, and
    additions. Hash collisons are handled through chaining with Linked Lists. 

    Inputs:
        -> k (int): Initial capacity of the static array. Default is 3000.
        -> load_factor (int): Target load factor for the HashMap. Goal is to keep below 0.75. 
    */
    constructor(k=3000, loadFactor=0.75) {
        this.buckets = Array(k).fill(null);
        this.loadFactor = loadFactor;
        this.capacity = 0; 
    }

    put (key, val) {
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

    get (key) {
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