""" This module contains code representing the quickselect algorithm, used
to efficiently find the kth smallest/largest element in a collection """
from typing import List, Union


def recursive_quickselect(array: List[int], k: int) -> Union[int, None]:
    """
    This function represents the recursive quickselect algorithm,
    which is used to efficiently find the kth smallest or largest
    element in a collection, which in this case is assumed to be an
    array.

    This algorithm chooses a pivot element, which in this implementation
    is chosen to be the leftmost element of the array in every subproblem.
    Every element of the array is then sorted with respect to this pivot
    element, with the pivot element then being inserted into its final sorted
    position.

    If the final sorted position is equal to k, the value sorted in the index
    is returned. If the final sorted position is not equal to k, the portion
    of the array which contains k is recursed into.

    Time:
        O(N) best/average
        O(N**2) worst

    Space:
        O(logN) best/average/worst

    N - length of the input array

    Args:
        array:
            List of integers from which to retrieve the kth smallest value

        k:
            Value between 0<=k<len(array). Represents the (sorted) index from
            which to retrieve the output value

    Returns:
        An integer representing the kth smallest or largest element inside
        the input array, or None if it is not found
    """
    kth_elem = _recursive_quick_select_helper(array, k, 0, len(array) - 1)
    return kth_elem


def _recursive_quick_select_helper(array: List[int], k: int, start: int,
                                   end: int) -> int:
    if start >= end:
        return array[start] if start == k else None
    pivot = start
    ptr1 = start + 1
    ptr2 = end
    while ptr1 <= ptr2:
        if array[ptr1] > array[pivot] and array[pivot] > array[ptr2]:
            swap(array, ptr1, ptr2)
            ptr1 += 1
            ptr2 -= 1

        elif array[ptr1] <= array[pivot]:
            ptr1 += 1

        elif array[ptr2] >= array[pivot]:
            ptr2 -= 1

    swap(array, pivot, ptr2)
    # if the final sorted index the pivot is sorted to is equal to k,
    # then we've found the kth smallest element. Otherwise, we recurse into the
    # portion of the array that must contain the kth smallest element
    if ptr2 == k:
        return array[k]
    elif ptr2 > k:
        return _recursive_quick_select_helper(array, k, start, ptr2 - 1)
    else:
        return _recursive_quick_select_helper(array, k, ptr2 + 1, end)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
