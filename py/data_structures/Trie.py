""" This module contains code for a class that represents a (simplified)
prefix trie data structure """


class Trie:
    """ This class represents a (simple) prefix Trie data structure.

    The trie is an ordered tree data structure used to store strings.
    Anytime you have a dataset of strings and you'd like to query the
    dataset, you can consider using a Trie.

    Where k is the length of the longest word stored in the trie, and n
    is the total number of words stored in the trie.

    Used for autocomplete, spell checking, IP routing, etc.
    """

    def __init__(self):
        self.endSymbol = "*"
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the Trie.
        
        Time:
            - O(k) best/avg/worst
        Space:
            - O(k) best/avg/worst

        k - length of the word being inserted into the trie 

        Input:
            - word(String): String representing word to insert into the Trie. 
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
        This method takes a string as input and returns a boolean indicating whether or not it is currently stored in the 
        Trie. 
    
        Time:
            - O(k) best/avg/worst
        Space:
            - O(1) best/avg/worst

        k - length of input string
        
        Input:
            - word(String): String representing word to lookup in the Trie. 
        Returns:
            - Boolean representing whether the string is stored in the Trie 
        """
        node = self.root
        return self._lookupHelper(node, word)

    def _lookupHelper(self, node, word):
        for char in word:
            if char not in node:
                return False
            node = node[char]
        # Word is only in trie if the last node has the end symbol in it
        return self.endSymbol in node

    def startsWith(self, prefix):
        """
        This method recieves a string as an input which is assumed to be a prefix pattern, and then returns a boolean
        indicating whether or not the prefix pattern is present in the trie. 

        Time:
            - O(k) best/avg/worst
        
        Space:
            - O(1) best/avg/worst

        k - length of input string 
        Input:
            - prefix(String): String representing the prefix pattern to look up in the Trie

        Returns:
            - Boolean representing whether the prefix pattern is stored in the Trie 
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
        This method recieves a string as input and deletes the string if it is currently stored in the Trie. 

        Time:
            - O(k) best/avg/worst
        Space:
            - O(1) best/avg/worst

        Input:
            - word(String): String representing the word to delete in the Trie 

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
        self._deleteHelper(newNode, word, idx + 1)

        # if there are no chars in the new node then we can safely
        # delete it
        if not newNode:
            node.pop(word[idx])
