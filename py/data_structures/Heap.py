""" This module contains code for a class that represents the heap
data structure """
from typing import Callable, Literal, Union, List


class Heap:
    """ This class represents a Heap.

    A heap is a special type of binary tree called a complete binary tree
    as every single level in the heap is filled up except for potentially
    the last level, and the levels are filled up from left to right. In
    addition, a heap must obey the heap property.

    For max heaps, the heap property entails that the value of any given
    node must be greater than or equal to its children nodes values.

    For min heaps, the heap property entails that the value of any given
    node must be less than or equal to its children nodes values.

    Attributes:
        custom_comparator:
            Function that represents the comparator function to be used to
            arrange nodes in the heap, or None which results in a default
            comparator being used assuming that the values contained in
            nodes are numbers

        type_heap:
            An integer value that should be either 0 or 1, indicating if
            the heap is a min-heap or max-heap. 0 will cause the heap
            created to be a min heap, 1 will cause the heap created to
            be a max heap
    """

    def __init__(self,
                 custom_comparator: Union[Callable, None] = None,
                 type_heap: Literal[0, 1] = 0):
        if not custom_comparator:
            # if the type_heap property is zero, the heap will be assumed to
            # be a min-heap and the comparator function used to ensure the heap
            # property is set appropriately otherwise if the type_heap is 1,
            # then the heap will be assumed to be a max-heap
            if type_heap == 0:
                self.comparator_func = lambda x, y: 1 if x - y < 0 else 0
            else:
                self.comparator_func = lambda x, y: 1 if x - y > 0 else 0
        else:
            self.comparator_func = custom_comparator

    def heapify(self, array: List[object]) -> None:
        """ This method will create a heap out of the given array elements
        in-place.

        Time:
            O(N) best/average/worst

        Space:
            O(1) best/average/worst

        Where N is the number of elements inside of the heap

        Args:
            array:
                List of objects to be heapified. By default, these are
                assumed to be integers.
        """
        first_parent_idx = (len(array) - 2) // 2
        while first_parent_idx >= 0:
            self._sift_down(array, first_parent_idx, len(array) - 1)
            first_parent_idx -= 1

    def insert(self, heap: List[object], val: object) -> None:
        """ Inserts value into the heap using the sift_up helper
        method.

        Time:
            O(logN) best/average/worst

        Space:
            O(1) best/average/worst

        Where N is the number of elements inside of the heap

        Args:
            heap:
                Array holding objects that represents a heap

            val:
                Object of the same type as those contained inside of the
                heap. By default, assumed to be an integer.
        """
        heap.append(val)
        self._sift_up(heap, len(heap) - 1, 0)

    def peek(self, heap: List[object]) -> object:
        """ Peeks at the highest priority element in the heap.

        Time:
            O(1) best/average/worst

        Space:
            O(1) best/average/worst

        Args:
            heap:
                Array holding objects that represents a heap

        Returns:
            The object with the highest priority in the heap
        """
        if not heap:
            return
        return heap[0]

    def remove(self, heap: List[object]) -> object:
        """ Removes the highest priority element from the heap
        using the sift_down helper method and returns it.

        Time:
            O(logN) best/average/worst

        Space:
            O(1) best/average/worst

        Where N is the number of elements inside of the heap

        Args:
            heap:
                Array holding objects that represents a heap

        Returns:
            The object with the highest priority in the heap
        """
        if not heap:
            return
        self._swap(heap, 0, len(heap) - 1)
        removed_val = heap.pop()
        self._sift_down(heap, 0, len(heap) - 1)
        return removed_val

    def _sift_down(self, heap, start, end):
        """
        This method has the responsibility of ensuring the heap property is met when elements
        are removed from the heap. 
        
        When the root element is removed from the heap, a new element is placed at the root. 
        This method will move that element down the heap until the heap property is satisfied. 

        Inputs:
            - heap(list[int]): List of integers representing a heap
            - start (int): Integer representing the index in the array to start sifting down from
            - end (int): Integer representing the index in the array to stop sifting down to
        Outputs:
            - None. Sifts down in place. 
        """
        currIdx = start
        firstChildIdx = start * 2 + 1
        while firstChildIdx <= end:
            secondChildIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= end else -1
            # If val at secondChildIdx is less than val at firstChildIdx in minHeaps, then its candidate to consider when swapping
            # If val at secondChildIdx is greater than val at firstChildIdx in maxHeaps, then its candidate to consider when swapping
            if secondChildIdx != -1 and self.comparator_func(
                    heap[secondChildIdx], heap[firstChildIdx]):
                idxToSwap = secondChildIdx
            else:
                idxToSwap = firstChildIdx
            if self.comparator_func(heap[idxToSwap], heap[currIdx]):
                self._swap(heap, idxToSwap, currIdx)
                currIdx = idxToSwap
                firstChildIdx = currIdx * 2 + 1
            else:
                break

    def _sift_up(self, heap, start, end):
        """
        This method has the responsibility of ensuring the heap property is met when elements
        are inserted into the heap. 
        
        When an element is inserted into the heap, the heap property will most likely be violated.
        This method moves the inserted element up the heap until the heap property is satisifed.

        Inputs:
            - heap(list[int]): List of integers representing a heap
            - start (int): Integer representing the index in the array to start sifting up from
            - end (int): Integer representing the index in the array to stop sifting up 
        Outputs:
            - None. Sifts up in place. 
        """
        parentIdx = (start - 1) // 2
        while parentIdx >= end:
            # if heap property is not met, then we swap and continue upwards
            # if its true that heap[start] is less than heap[parent], we swap for min-heaps
            # if its true that heap[start] is greater than heap[parent], we swap for max-heaps
            if self.comparator_func(heap[start], heap[parentIdx]):
                self._swap(heap, start, parentIdx)
                start = parentIdx
                parentIdx = (start - 1) // 2
            else:
                break

    def _swap(self, heap, i, j):
        """
        This method has the responsibility of swapping the values at two indices within an array
        inplace. 

        Inputs:
            - heap(list[int]): List of integers representing a heap
            - i (int): Integer representing an index within the input array
            - j (int): Integer representing an index within the input array
        Outputs:
            - None. Swaps indices inplace. 
        """
        heap[i], heap[j] = heap[j], heap[i]
