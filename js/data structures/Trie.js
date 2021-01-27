/**
 *  This class represents a (simple) prefix Trie data structure. The Trie is an ordered tree 
    data structure used to store strings. Anytime you have a dataset of strings and you'd like
    to query the dataset, you can consider using a Trie. 

 * Time: all best/avg/worst
 *- insert: O(k) 
 *- lookup: O(k)
 *- deletion: O(k)
 *- startsWith: O(k)

 * Space: 
 *- O(n*k)


 * Where k is the length of a word, and n is the total number of words stored in the trie.
 * Used for autocomplete, spell checking, IP routing, etc. 
 */
class Trie {
    constructor() {
        /** Attribute symbolizing the end of a word in the trie 
         * @param {string}
        */
        this.endSymbol = "*";

        /** Root node of the tree
         * @param {object}
         */
        this.root = {}; 
    }

    /**
     * Inserts a word into the Trie. 
     * 
     * Time:
     *- O(k) best/avg/worst
        
     * Space:
     *- O(k) best/avg/worst

     * k - length of the word being inserted into the trie 

     * @param {string} word String representing word to insert into the Trie.

     * @returns {undefined}
     */
    insert(word) {
        let node = this.root;
        return this._insertHelper(node, word);
    }

    _insertHelper(node, word) {
        for (const char of word) {
            if (!(char in node)) {
                node[char] = {};
            }
            node = node[char];
        }
        node[this.endSymbol] = true; 
    }

    /**
     *  This method takes a string as input and returns a boolean indicating whether or not it is currently stored in the 
        Trie. 

     *Time:
     *- O(k) best/avg/worst
    
     *Space:
     *- O(1) best/avg/worst

     * @param {string} word String representing word to lookup in the Trie
     * @returns {boolean} Boolean representing whether the string is stored in the Trie 
     */
    lookup(word) {
        let node = this.root;
        return this._lookupHelper(word, node);
    }


    _lookupHelper(word, node) {
        for (const char of word) {
            if (!(char in node)) {
                return false;
            }
            node = node[char];
        }
        return this.endSymbol in node; 
    }

    /**  
     * This method recieves a string as an input which is assumed to be a prefix pattern, and then returns a boolean
        indicating whether or not the prefix pattern is present in the trie. 

     * Time:
     *- O(k) best/avg/worst
        
     * Space:
     *- O(1) best/avg/worst
     *
     * k - length of input string 
     * @param {string} prefix String representing the prefix pattern to look up in the Trie
     * @returns {boolean} Boolean representing whether the prefix pattern is stored in the Trie 
     */
    startsWith(prefix) {
        let node = this.root;
        return this._startsWithHelper(prefix, node);
    }

    _startsWithHelper(prefix, node) {
        for (const char of prefix) {
            if (!(char in node)) {
                return false;
            }
            node = node[char];
        }
        return true; 
    }


    /**
     * Deletes a word from the trie if the word exists in the trie in O(k) time, O(1) space b/a/w.

     * @param {string} word 
     * @returns {null} 
     */
    delete(word) {
        if (!(this.lookup(word))) {
            return null;
        }
        let node = this.root;
        this._deleteHelper(node, word, 0);
    }


    _deleteHelper(node, word, idx) {
        if (idx === word.length) {
            delete node[this.endSymbol];
            return null;
        }
        const newNode = node[word[idx]];
        this._deleteHelper(newNode, word, idx+1);

        if (Object.keys(newNode).length === 0) {
            delete node[word[idx]];
            return null; 
        }
    }
}


export {Trie}; 