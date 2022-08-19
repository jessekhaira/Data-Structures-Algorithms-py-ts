""" This module contains code representing the merge sort algorithm """
from typing import List


def merge_sort(array: List[int]) -> List[int]:
    """ This function represents the merge sort algorithm used to
    sort an array of integers in ascending order.

    Time:
        O(Nlog(N)) best/avg/worst

    Space:
        O(N) best/avg/worst

    Where N is the length of the input array

    Args:
        array:
            List of integers to sort in ascending order

    Returns:
        Input list of integers sorted in ascending order

    """
    aux_array = array[:]
    merge_sort_helper(array, aux_array, 0, len(array) - 1)
    return array


def merge_sort_helper(array: List[int], aux_array: List[int], start: int,
                      end: int) -> None:
    """ This helper function helps to implement mergesort. This function
    is a recursive function that recurses to the base case of start >= end
    -> when the pointers point to the same element, or when its an invalid
    invalid configuration, return.

    We then partition and sort the main array using the help of the aux_array.

    Args:
        array:
            List of integers to sort from start ptr to end ptr

        aux_array:
            Copy of the main array used to help sort the array

        start:
            Integer representing start idx to sort from

        end:
            Integer representing end idx to sort to
    """
    if start >= end:
        return
    # aux_array isn't even sorted yet, can't be used to sort the main array
    # so we sort aux_array first before trying to sort main array
    # have to recurse to base case so we break array in half and sort each
    # half recursively
    middle = start + (end - start) // 2
    merge_sort_helper(aux_array, array, start, middle)
    merge_sort_helper(aux_array, array, middle + 1, end)
    _merge(array, aux_array, start, middle, middle + 1, end)


def _merge(array: List[int], aux_array: List[int], lstart: int, lend: int,
           rstart: int, rend: int) -> None:
    """ This function carries out the merge operation using the
    two sorted partitions of aux_array from lstart to lend, and
    rstart to rend, to sort the main array.

    Args:
        array:
            List of integers to sort from lstart to rend

        aux_array:
            Copy of the main array used to help sort the array

        lstart:
            Integer representing start idx of sorted left portion of aux_array

        lend:
            Integer representing end idx of sorted left portion of aux_array

        rstart:
            Integer representing start idx of sorted right portion of aux_array

        rend:
            Integer representing end idx of sorted right portion of aux_array
    """
    ptr_arr = lstart
    while lstart <= lend and rstart <= rend:
        if aux_array[lstart] <= aux_array[rstart]:
            array[ptr_arr] = aux_array[lstart]
            lstart += 1
        else:
            array[ptr_arr] = aux_array[rstart]
            rstart += 1
        ptr_arr += 1

    while lstart <= lend:
        array[ptr_arr] = aux_array[lstart]
        lstart += 1
        ptr_arr += 1

    while rstart <= rend:
        array[ptr_arr] = aux_array[rstart]
        rstart += 1
        ptr_arr += 1
