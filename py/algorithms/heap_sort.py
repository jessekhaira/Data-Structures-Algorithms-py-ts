""" This module contains code representing the heap sort algorithm """
from typing import List
from py.utils.utility_functions import swap


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

    N - represents the length of the input array

    Args:
        array:
            List of integers

    Returns:
        The input list of integers sorted in ascending order in place
    """
    if not array:
        return []
    # heap sort relies on the array being a max-heap -
    # therefore we have to heapify the array before
    # performing any swap operations
    heapify(array)
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
        sift_down(array, 0, end_idx)
    return array


def heapify(array: List[int]) -> None:
    """ This function accepts an input array of integers,
    and max-heapifys the array.

    Args:
        array:
            List of integers
    """
    pointer = (len(array) - 2) // 2
    while pointer >= 0:
        sift_down(array, pointer, len(array) - 1)
        pointer -= 1


def sift_down(array: List[int], start: int, end: int) -> None:
    """ This function represents the siftdown algorithm used
    to maintain the heap property for a max heap. This algorithm
    accepts an array of integers, and two integers that represent
    indices within the heap such that start <= end. The element
    located at the start index is moved down the heap until start > end,
    or the heap property is satisifed.

    Args:
        array:
            List of integers representing a heap

        start:
            Integer representing an index within the heap

        end:
            Integer representing an index within the heap
    """
    first_child = start * 2 + 1
    while first_child <= end:
        second_child = start * 2 + 2 if start * 2 + 2 <= end else -1
        if second_child != -1 and array[second_child] > array[first_child]:
            idx_to_swap = second_child
        else:
            idx_to_swap = first_child

        if array[idx_to_swap] > array[start]:
            swap(array, idx_to_swap, start)
            start = idx_to_swap
            first_child = start * 2 + 1
        else:
            break
