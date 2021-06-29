""" This module contains code for a class that represents the heap
data structure """
from typing import Callable, Literal, Union, List
from py.utils.utility_functions import swap


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
        comparator_func:
            Function that if specified, should accept two objects as input,
            compare them, and return an integer representing which object is
            bigger then the other. If None, it will be assumed that the
            objects the heap will contain are numbers.

        type_heap:
            An integer value that should be either 0 or 1, indicating if
            the heap is a min-heap or max-heap. 0 will cause the heap
            created to be a min heap, 1 will cause the heap created to
            be a max heap
    """

    def __init__(self,
                 comparator_func: Union[Callable[[object, object], int],
                                        None] = None,
                 type_heap: Literal[0, 1] = 0):
        if not comparator_func:
            # if the type_heap property is zero, the heap will be assumed to
            # be a min-heap and the comparator function used to ensure the heap
            # property is set appropriately otherwise if the type_heap is 1,
            # then the heap will be assumed to be a max-heap
            if type_heap == 0:
                self.comparator_func = lambda x, y: 1 if x - y < 0 else 0
            else:
                self.comparator_func = lambda x, y: 1 if x - y > 0 else 0

        else:
            self.comparator_func = comparator_func

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
            self.sift_down(array, first_parent_idx, len(array) - 1)
            first_parent_idx -= 1

    def insert(self, heap: List[object], val: object) -> None:
        """ Inserts value into the heap using the sift_up helper method.

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
        """ Removes the highest priority element from the heap using the
        sift_down helper method and returns it.

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
        swap(heap, 0, len(heap) - 1)
        removed_val = heap.pop()
        self.sift_down(heap, 0, len(heap) - 1)
        return removed_val

    def sift_down(self, heap: List[object], start: int, end: int) -> None:
        """ This method has the responsibility of ensuring the heap property
        is met when elements are removed from the heap.

        When the root element is removed from the heap, a new element is
        placed at the root. This method will move that element down the heap
        until the heap property is satisfied.

        Args:
            heap:
                Array holding objects that represents a heap

            start:
                Integer representing the index in the array to start sifting
                down from

            end:
                Integer representing the last index in the array to sift down to
        """
        curr_idx = start
        first_child_idx = start * 2 + 1
        while first_child_idx <= end:
            second_child_idx = (curr_idx * 2 +
                                2 if curr_idx * 2 + 2 <= end else -1)
            # If val at second_child_idx is less than val at first_child_idx in
            # minHeaps,then its candidate to consider when swapping. If val at
            # second_child_idx is greater than val at first_child_idx in
            # maxHeaps, then its candidate to consider when swapping
            if second_child_idx != -1 and self.comparator_func(
                    heap[second_child_idx], heap[first_child_idx]):
                idx_to_swap = second_child_idx
            else:
                idx_to_swap = first_child_idx
            if self.comparator_func(heap[idx_to_swap], heap[curr_idx]):
                swap(heap, idx_to_swap, curr_idx)
                curr_idx = idx_to_swap
                first_child_idx = curr_idx * 2 + 1
            else:
                break

    def _sift_up(self, heap: List[object], start: int, end: int) -> None:
        """ This method has the responsibility of ensuring the heap
        property is met when elements are inserted into the heap.

        When an element is inserted into the heap, the heap property
        will most likely be violated. This method moves the inserted
        element up the heap until the heap property is satisifed.

        Args:
            heap:
                Array holding objects that represents a heap

            start:
                Integer representing the index in the array to start sifting
                up from

            end:
                Integer representing the last index in the array to sift up to
        """
        parent_idx = (start - 1) // 2
        while parent_idx >= end:
            # if heap property is not met, then we swap and continue upwards
            # if its true that heap[start] is less than heap[parent], we swap
            # for min-heaps. if its true that heap[start] is greater than
            # heap[parent], we swap for max-heaps
            if self.comparator_func(heap[start], heap[parent_idx]):
                swap(heap, start, parent_idx)
                start = parent_idx
                parent_idx = (start - 1) // 2
            else:
                break
