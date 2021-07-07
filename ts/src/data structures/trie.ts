class TrieNode {
    children: Record<string, TrieNode>;

    containsEndOfWord: boolean;

    constructor() {
        this.children = {};
        this.containsEndOfWord = false;
    }
}
/**
 *  This class represents a (simple) prefix Trie data structure.
 *  The Trie is an ordered tree data structure used to store strings.
 *  Anytime you have a dataset of strings and you'd like to query the
 *  dataset, you can consider using a Trie.

 * Where k is the length of a word, and n is the total number of words
 * stored in the trie. Used for autocomplete, spell checking, IP routing, etc. 
 */
class Trie {
    root: TrieNode;

    constructor() {
        /** Root node of the tree
         * @param {object}
         */
        this.root = new TrieNode();
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
    insert(word: string): void {
        const node = this.root;
        Trie._insertHelper(node, word);
    }

    static _insertHelper(node: TrieNode, word: string): void {
        let currNode = node;
        for (let i = 0; i < word.length; i += 1) {
            const char = word[i];
            if (!(char in currNode.children)) {
                currNode.children[char] = new TrieNode();
            }
            currNode = currNode.children[char];
        }
        currNode.containsEndOfWord = true;
    }

    /**
     *  This method takes a string as input and returns a boolean indicating 
     *  whether or not it is currently stored in the Trie. 

     * Time:
     *- O(k) best/avg/worst
    
     * Space:
     *- O(1) best/avg/worst

     * k - length of input string 
     * @param {string} word String representing word to lookup in the Trie
     * @returns {boolean} Boolean representing whether the string is stored
     * in the Trie 
     */
    lookup(word: string): boolean {
        const node = this.root;
        return Trie._lookupHelper(word, node);
    }

    static _lookupHelper(word: string, node: TrieNode): boolean {
        let currNode = node;
        for (let i = 0; i < word.length; i += 1) {
            const char = word[i];
            if (!(char in currNode)) {
                return false;
            }
            currNode = currNode.children[char];
        }
        return node.containsEndOfWord;
    }

    /**  
     * This method recieves a string as an input which is assumed to be a prefix
     *  pattern, and then returns a boolean indicating whether or not the prefix
     *  pattern is present in the trie. 

     * Time:
     *- O(k) best/avg/worst
        
     * Space:
     *- O(1) best/avg/worst
     *
     * k - length of input string 
     * @param {string} prefix String representing the prefix pattern to look up
     * in the Trie
     * @returns {boolean} Boolean representing whether the prefix pattern is
     * stored in the Trie 
     */
    startsWith(prefix) {
        const node = this.root;
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
     * This method recieves a string as input and deletes the string if it is currently stored in the Trie.
     * 
     * Time:
     *- O(k) best/avg/worst
      
     * Space:
     *- O(1) best/avg/worst 

     * k - length of input string
     * @param {string} word String representing the word to delete in the Trie 
     * @returns {null} 
     */
    delete(word) {
        if (!this.lookup(word)) {
            return null;
        }
        const node = this.root;
        this._deleteHelper(node, word, 0);
    }

    _deleteHelper(node, word, idx) {
        if (idx === word.length) {
            delete node[this.endSymbol];
            return null;
        }
        const newNode = node[word[idx]];
        this._deleteHelper(newNode, word, idx + 1);

        if (Object.keys(newNode).length === 0) {
            delete node[word[idx]];
            return null;
        }
    }
}

export default Trie;
