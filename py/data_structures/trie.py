""" This module contains code for a class that represents a (simplified)
prefix trie data structure """
from typing import Dict


class Trie:
    """ This class represents a (simple) prefix Trie data structure.

    The trie is an ordered tree data structure used to store strings.
    Anytime you have a dataset of strings and you'd like to query the
    dataset, you can consider using a Trie.

    Where k is the length of the longest word stored in the trie, and n
    is the total number of words stored in the trie.

    Used for autocomplete, spell checking, IP routing, etc.

    Attributes:
        end_sumbol:
            A string that is equivalent to "*" that represents the end symbol
            for a word in the trie

        root:
            Dictionary containing mapping between string keys, with dictionary
            values, representing all the words stored at the root of the trie
    """

    def __init__(self):
        self.end_symbol = "*"
        self.root = {}

    def insert(self, word: str) -> None:
        """ Inserts a word into the Trie.

        Time:
            O(k) best/average/worst

        Space:
            O(k) best/average/worst

        Where k is the length of the word being inserted into
        the trie

        Args:
            word:
                String representing word to insert into the Trie.
        """
        node = self.root
        self._insert_helper(node, word)

    def _insert_helper(self, node: Dict[str, Dict], word: str) -> None:
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]

        node[self.end_symbol] = True

    def lookup(self, word: str) -> bool:
        """ This method takes a string as input and returns a boolean
        indicating whether or not it is currently stored in the Trie.

        Time:
            O(k) best/average/worst

        Space:
            O(1) best/average/worst

        Where k is the length of the input string

        Args:
            word:
                String representing word to lookup in the Trie.

        Returns:
            Boolean value representing whether the string is stored in the Trie
        """
        node = self.root
        return self._lookup_helper(node, word)

    def _lookup_helper(self, node: Dict[str, Dict], word: str) -> bool:
        for char in word:
            if char not in node:
                return False
            node = node[char]
        # Word is only in trie if the last node has the end symbol in it
        return self.end_symbol in node

    def starts_with(self, prefix: str) -> bool:
        """ This method recieves a string as an input which is assumed to be
        a prefix pattern, and then returns a boolean indicating whether or not
        the prefix pattern is present in the trie.

        Time:
            O(k) best/average/worst

        Space:
            O(1) best/average/worst

        Where k is the length of the input string

        Input:
            prefix:
                String representing the prefix pattern to look up in the Trie

        Returns:
            Boolean value representing whether the prefix pattern is stored in
            the Trie
        """
        node = self.root
        return self._starts_with_helper(node, prefix)

    def _starts_with_helper(self, node: Dict[str, Dict], prefix: str) -> bool:
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True

    def delete(self, word: str) -> None:
        """ This method recieves a string as input and deletes the string if
        it is currently stored in the Trie.

        Time:
            O(k) best/average/worst

        Space:
            O(1) best/average/worst

        Where k is the length of the input string

        Args:
            word:
                String representing the word to delete in the Trie
        """
        # confirm word is even in the trie before attempting to delete it
        if not self.lookup(word):
            return
        node = self.root
        self._delete_helper(node, word, 0)

    def _delete_helper(self, node: Dict[str, Dict], word: str,
                       idx: int) -> None:
        if idx == len(word):
            node.pop(self.end_symbol)
            return
        new_node = node[word[idx]]
        self._delete_helper(new_node, word, idx + 1)

        # if there are no chars in the new node then we can safely
        # delete it
        if not new_node:
            node.pop(word[idx])
