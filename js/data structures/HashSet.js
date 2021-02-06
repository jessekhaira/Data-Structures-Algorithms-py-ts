class ChainingNode{
    constructor(value){
        this.val = value;
        this.next = null; 
    }
}

/**
 * This class represents a Hash Set designed specifically to accept integer values. Hash collisons are dealt with 
 * through chaining with linked lists. 
*/
class HashSet{
    constructor(init_capacity = 1000, load_factor = 0.75){
        this._buckets = Array(init_capacity).fill(null);
        this._design_load_factor = load_factor;
        this._curr_items_hashed = 0;
    }

    /**
     * Inserts the input argument, expected to be an integer, into the hash set. If by adding the element, the
     * design load factor is exceeded, rehashing is done. 
     * @param {number} key Argument to hash into hashset 
     */
    add(key) {
        const hashVal = this._hashing_algorithm(key);
        const newNode = new ChainingNode(key);
        if(!this._buckets[hashVal]) {
            this._buckets[hashVal] = newNode;
        }
        else {
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
        const currLoadFactor = (this._curr_items_hashed/this._buckets.length);
        if (currLoadFactor >= this._design_load_factor) {
            this.rehash();
        }
    }

    rehash() {
        const savedBuckets = this._buckets;
        this._curr_items_hashed = 0; 
        this._buckets = Array(savedBuckets.length *2).fill(null); 
        for (let node of savedBuckets) {
            while (node) {
                this.add(node.val);
                node = node.next; 
            }
        }
    }

    remove(key) {
        const hashVal = this._hashing_algorithm(key);
        let node = this._buckets[hashVal];
        let prev = null; 
        while (node) {
            if (node.val === key) {
                if (!prev) {
                    this._buckets[hashVal] = node.next; 
                }
                else {
                    prev.next = node.next; 
                }
                return;
            }
            else {
                prev = node; 
                node = node.next; 
            }
        }
    }

    /**
     * Returns a boolean indicating whether or not the hash set contains the integer input argument 
     * @param {number} key Integer input argument  
     */
    contains(key) {
        const hashVal = this._hashing_algorithm(key);
        let node = this._buckets[hashVal];
        while (node) {
            if (node.val === key) {
                return true; 
            }
            else {
                node = node.next; 
            }
        }
        return false; 
    }

    _hashing_algorithm(key) {
        return key%this._buckets.length; 
    }
}

export {HashSet}; 