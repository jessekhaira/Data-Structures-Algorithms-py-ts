""" This module contains code for a class that represents the hash map
data structure, resolving collisons using chaining """
from typing import Any


class ChainingNode:
    """ This class represents a Linked List node used for chaining to resolve
    collisons in a HashMap class.

    Attributes:
        key:
            Any type representing the key being hashed into the HashMap

        val:
            Any type representing the value being hashed into the HashMap

        next:
            ChainingNode object or None representing the connection between
            this node and the next node
    """

    def __init__(self, key: Any, val: Any):
        self.key = key
        self.val = val
        self.next = None


class HashMap:
    """ This class represents a HashMap class that accepts integer inputs. All
    methods of a HashMap are supported by this class -> put, remove, get, with
    dynamic array resizing.

    HashMaps are built on top of static arrays. This class assumes an initial
    capacity of a static array of 1000, with a load factor equal to 0.75. When
    the load factor is exceeded, dynamic array resizing is done to ensure O(1)
    TS lookups, removals, and additions.

    Attributes:
        k:
            Integer representing the initial capacity of the static array.
            Default is 3000.

        load_factor:
            Floating point value representing the target load factor for the
            HashMap. By default, is set to 0.75.

        static_arr:
            Array that is the underlying data structure of a hash map. Filled up
            with None values to start, but will contain ChainingNode objects
            afterwards.

        curr_capacity:
            Integer representing the number of objects hashed into the hash map.
    """

    def __init__(self, k: int = 3000, load_factor: float = 0.75):
        self.load_factor = load_factor
        self.static_arr = [None] * k
        self.curr_capacity = 0

    def put(self, key: int, value: Any) -> None:
        """ This method puts a value within the hash table according to its hash
        value, with the keys assumed to be integers and values assumed to be
        any type.

        Time:
            O(1) best/average
            O(N) worst

        Space:
            O(1) best/average
            O(N) worst

        Where N is the number of items hashed into HashMap

        Args:
            key:
                Integer representing the key to hash into the hash table

            value:
                Value of any type, associated with the key being hashed into the
                hash table
        """
        # get the hash value and look at the bucket in the hash table where this
        # key should be inserted if the bucket is empty, then insert the
        # key-value pair directly into the bucket by inserting node of new
        # linkedlist. Otherwise, add the key-value pair to the end of the
        # linkedlist in the bucket.
        hash_value = self._hash_function(key)
        if self.static_arr[hash_value] is None:
            self.static_arr[hash_value] = ChainingNode(key, value)
        else:
            curr_node = self.static_arr[hash_value]
            while curr_node.next and curr_node.key != key:
                curr_node = curr_node.next
            if curr_node.key != key:
                curr_node.next = ChainingNode(key, value)
                self.curr_capacity += 1
                if self.curr_capacity / len(
                        self.static_arr) >= self.load_factor:
                    self._dynamic_array_resizing()
            else:
                curr_node.val = value

    def get(self, key: int) -> Any:
        """ This function retrieves the value associated with the given input
        key, if it exists within the hashtable.

        Time:
            O(1) best/average
            O(N) worst

        Space:
            O(1) best/average
            O(N) worst

        Where N is the number of items hashed into HashMap

        Args:
            key:
                Integer representing the key to lookup in the hashtable.

        Returns:
            A value of any type, representing the value associated with the
            key in the hashtable. If the key doesn't exist in the table, then
            None will be returned.
        """
        # look up the bucket in the hashtable the key should be residing and
        # if nothing exists in that bucket, return none. Otherwise, traverse the
        # linked list that exists in that bucket until there is nothing left or
        # the appropriate key is found.
        hash_value = self._hash_function(key)
        if self.static_arr is None:
            return
        else:
            curr_node = self.static_arr[hash_value]
            while curr_node and curr_node.key != key:
                curr_node = curr_node.next
            if not curr_node:
                return
            return curr_node.val

    def _dynamic_array_resizing(self):
        """ Method used to double the size of the array underlying the
        HashMap when the load factor of the HashMap is exceeded.
        """
        saved_arr = self.static_arr
        self.static_arr = [None] * len(self.static_arr) * 2
        for pointer in saved_arr:
            if pointer:
                while pointer:
                    curr_key = pointer.key
                    curr_val = pointer.val
                    pointer = pointer.next
                    self.put(curr_key, curr_val)

    def remove(self, key: int) -> None:
        """ If the input key is within the hashtable, this method removes the
        key-value pair from the hashtable.

        Time:
            O(1) best/average
            O(N) worst

        Space:
            O(1) best/average
            O(N) worst

        Where N is the number of items hashed into HashMap

        Args:
            key:
                Integer representing the key to lookup in the hashtable.
        """
        hash_value = self._hash_function(key)
        if self.static_arr is None:
            return
        else:
            curr_node = self.static_arr[hash_value]
            prev_node = None
            while curr_node and curr_node.key != key:
                prev_node = curr_node
                curr_node = curr_node.next
            if not curr_node:
                return
            self.curr_capacity -= 1
            if not prev_node:
                # you can't just assume that theres nothing else hashed here
                # so we have to set hash_value to curr_node.next rather than
                # None outright
                self.static_arr[hash_value] = curr_node.next
                return
            else:
                prev_node.next = curr_node.next
                curr_node = None
                return

    def _hash_function(self, key: int) -> int:
        """ This function represents the hashing algorithm being used for the
        hashmap. This function takes integers as inputs and produces the bucket
        within the hashmap the integer falls into.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Args:
            key:
                Integer representing the key to hash into the hashtable

        Returns:
            Integer representing the index within the hashmap the key falls into
        """
        # abs() to be able to hash in positive AND negative ints
        # although python does support negative integer indices
        return abs(key % len(self.static_arr))
