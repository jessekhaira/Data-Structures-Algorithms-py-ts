""" This module contains code for an efficient implementation of the
quick sort algorithm """
from py.utils.utility_functions import swap


def quick_sort(array):
    """ This function represents an efficient implementation of the
    quick sort algorithm. Like the merge sort algorithm, this algorithm
    uses the divide and conquer strategy to efficiently sort an array.
    Unlike merge sort, which splits arrays in half every time, quicksort
    places a pivot element (chosen to be the leftmost element in the array
    in this implementation) to its final sorted position. Quicksort then
    recurses and sorts all the elements to the left of a pivot element,
    and all the elements to the right of a pivot element until the base
    case is hit.

    Time:
        O(NlogN) best/avg
        O(N**2) worst

    Space:
        O(logN) best/average/worst

    Where N is the number of elements in the input array

    Args:
        array:
            List of integers to sort in ascending order

    Returns:
        The input list of integers sorted in ascending order
    """
    if not array:
        return
    quick_sort_helper(array, 0, len(array) - 1)
    return array


def quick_sort_helper(array, start, end):
    if start >= end:
        return
    pivot = start
    ptr_l = start + 1
    ptr_r = end

    while ptr_l <= ptr_r:
        if array[ptr_l] > array[pivot] and array[pivot] > array[ptr_r]:
            swap(array, ptr_l, ptr_r)
            ptr_l += 1
            ptr_r -= 1

        elif array[ptr_l] <= array[pivot]:
            ptr_l += 1

        elif array[ptr_r] >= array[pivot]:
            ptr_r -= 1

    swap(array, pivot, ptr_r)
    if end - (ptr_r + 1) > (ptr_r - 1) - start:
        quick_sort_helper(array, start, ptr_r - 1)
        quick_sort_helper(array, ptr_r + 1, end)

    else:
        quick_sort_helper(array, ptr_r + 1, end)
        quick_sort_helper(array, start, ptr_r - 1)
