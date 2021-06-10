""" This module contains code representing the heap sort algorithm """
from typing import List
from py.utils.utility_functions import swap
from py.data_structures.heap import Heap


def heap_sort(array: List[int]) -> List[int]:
    """ This algorithm represents the heap sort algorithm, used to
    sort an array of integers in ascending order. This algorithm relies
    on a data structure called a max-heap to efficiently sort an array
    of elements in-place.

    This algorithm does not produce a stable sort. This algorithm also
    has an additional operation of max-heapifying the input array, so
    on average it will run slower than quicksort, but has the advantage
    of having a worst case time complexity better then quicksort
    along with not using any space.

    Time:
        O(NlogN) best/avg/worst

    Space:
        O(1) best/avg/worst

    Where N represents the length of the input array

    Args:
        array:
            List of integers to sort in ascending order

    Returns:
        The input list of integers sorted in ascending order in place
    """
    if not array:
        return []
    # heap sort relies on the array being a max-heap -
    # therefore we have to heapify the array before
    # performing any swap operations
    heap = Heap(type_heap=1)
    heap.heapify(array)
    # endIdx represents the idx which the current largest element
    # in the max heap will swap to first iteration, this will be the
    # largest element in the heap so it should go in the last
    # idx spot, and so on from there
    end_idx = len(array) - 1
    while end_idx > 0:
        swap(array, 0, end_idx)
        end_idx -= 1
        # have to maintain heap property - every parent node has to have a value
        # greater than or equal to children nodes
        heap.sift_down(array, 0, end_idx)
    return array
