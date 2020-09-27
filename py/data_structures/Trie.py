class Trie:
    """
    This class represents a prefix Trie data structure. The Trie is an ordered tree data
    structure used to store strings. 

    Costs b/a/w:
    - insert: O(k)
    - lookup: O(k)
    - deletion: O(k)
    - startsWith: O(k)
    - Space: O(n*k)

    Where k is the length of a word, and n is the total number of words stored in the trie.

    Used for autocomplete, spell checking, IP routing, etc. 
    """
    def __init__(self):
        self.endSymbol = "*"
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the Trie in O(k) time, O(1) space b/a/w.

        Input:
        - word(str)
        Returns:
        - None 
        """ 
        node = self.root
        self._insertHelper(node, word)
    
    def _insertHelper(self, node, word):
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        
        node[self.endSymbol] = True
    
    def lookup(self, word):
        """
        Looks up a word in the Trie in O(k) time, O(1) space b/a/w.

        Input:
        - word(str)
        Returns:
        - Boolean: Represents if word is in Trie   
        """
        node = self.root
        return self._lookupHelper(node, word)
    
    def _lookupHelper(self, node, word):
        for char in word:
            if char not in node:
                return False
            node = node[char]
        # Word is only in trie if the last node has the end symbol
        # in it 
        return self.endSymbol in node 
    
    def startsWith(self, prefix):
        """
        Checks if the prefix pattern is present in the trie in O(k) time, O(1) space b/a/w.

        Input:
        - prefix(str)

        Returns:
        - Boolean: Represents if the prefix pattern is in Trie 
        """
        node = self.root
        return self._startsWithHelper(node, prefix)

    def _startsWithHelper(self, node, prefix):
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True

    def delete(self, word):
        """
        Deletes a word from the trie if the word exists in the trie in O(k) time, O(1) space b/a/w.

        Input:
        - word(str)

        Returns:
        - None 
        """ 
        # confirm word is even in the trie before attempting to delete it
        if not self.lookup(word):
            return 
        node = self.root
        self._deleteHelper(node, word, 0)

    def _deleteHelper(self, node, word, idx):
        if idx == len(word):
            node.pop(self.endSymbol)
            return
        newNode = node[word[idx]]
        self._deleteHelper(newNode, word, idx+1)

        # if there are no chars in the new node then we can safely
        # delete it
        if not newNode:
            node.pop(word[idx])
        
    
    
