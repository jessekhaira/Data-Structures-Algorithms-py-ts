""" This module contains code for a class that represents the hash
set data structure """
from py.utils.linked_list import SinglyLinkedListNode


class HashSet:
    """ This class represents a Hash Set designed specifically to accept
    integer values. Hash collisons are dealt with through chaining with
    linked lists.

    A HashSet is a data structure built on static arrays which is meant to
    hold a collection of unique items.

    Attributes:
        init_capacity:
            Integer representing the initial capacity of the hash set

        load_factor:
            Floating point value representing the maximum load factor of the
            hash set
    """

    def __init__(self, init_capacity: int = 1000, load_factor: float = 0.75):
        # A static array is the base data structure of a Hash Set
        self._buckets = [None] * init_capacity
        self._design_load_factor = load_factor
        self._curr_items_hashed = 0

    def add(self, val: int) -> None:
        """ Inserts the input argument, expected to be an integer, into the hash
        set. If by adding the element, the design load factor is exceeded,
        rehashing is done.

        Time:
            O(1) best/average
            O(N) worst

        Space:
            O(1) best/average
            O(N) worst

        Where N is the number of items hashed into the hash set

        Args:
            val:
                Integer input argument to be added to Hash Set
        """
        hash_val = self._hashing_algorithm(val)
        node_wrapper_val = SinglyLinkedListNode(val)
        if not self._buckets[hash_val]:
            self._buckets[hash_val] = node_wrapper_val
        else:
            node = self._buckets[hash_val]
            prev = None
            while node:
                # unique collection of items - if we're adding same item twice,
                # then only one of them counts
                if node.val == val:
                    return
                else:
                    prev = node
                    node = node.next

            prev.next = node_wrapper_val

        # adding items to hash set increases current load factor, and
        # if the load factor is >= then # the design load factor,
        # we rehash to keep the time complexity of the hash set methods low
        self._curr_items_hashed += 1
        curr_load_factor = (self._curr_items_hashed) / len(self._buckets)
        if curr_load_factor >= self._design_load_factor:
            self._rehash()

    def _rehash(self):
        # double the number of buckets, and since no items will initially be
        # hashed into the new buckets
        # array, set the size to be zero.
        saved_version_old_buckets = self._buckets
        self._buckets = (len(self._buckets) * 2) * [None]
        self._curr_items_hashed = 0
        for node in saved_version_old_buckets:
            while node:
                self.add(node.val)
                node = node.next

    def contains(self, val: int) -> bool:
        """ Returns a boolean indicating whether or not the hash set
        contains the integer input argument.

        Time:
            O(1) best/average
            O(N) worst

        Space:
            O(1) best/average
            O(N) worst

        Where N is the number of items hashed into the hash set

        Args:
            val:
                Integer input argument to check exists in the hash set

        Output:
            Boolean indicating whether the hash set contains the integer input
        """
        hash_val = self._hashing_algorithm(val)
        node = self._buckets[hash_val]
        while node:
            if node.val == val:
                return True
            else:
                node = node.next
        return False

    def remove(self, val: int) -> None:
        """ Removes the input value from the hash set if it is currently
        stored in the hash set

        Args:
            val:
                Integer input argument to remove from the hash set if it
                is currently stored
        """
        hash_val = self._hashing_algorithm(val)
        self._curr_items_hashed -= 1
        node = self._buckets[hash_val]
        prev = None
        while node:
            if node.val == val:
                # edge case - deleting head of linked list from bucket
                # means the new head will be the node after the head node
                # (which can be None)
                if not prev:
                    self._buckets[hash_val] = node.next
                else:
                    saved_next = node.next
                    prev.next = saved_next
                return
            else:
                prev = node
                node = node.next

    def _hashing_algorithm(self, val: int) -> int:
        """ This function represents the hashing algorithm being used for the
        hashset. This function takes integers as inputs and produces the bucket
        within the hashset the integer falls into.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Args:
            key:
                Integer representing the value to hash into the hashset

        Returns:
            Integer representing the index within the hashset the value falls
            into
        """
        return val % len(self._buckets)
