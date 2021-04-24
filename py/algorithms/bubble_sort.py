""" This module contains code representing the bubble sort algorithm """
from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """ This algorithm represents the bubble sort algorithm,
    meant to be used to sort an array of integers in ascending
    order.

    Time:
        - O(N**2) best/avg/worst
    Space:
        - O(1) best/avg/worst

    N - number of elements in input array

    Args:
        array:
            Array of integers to sort in ascending order

    Returns:
        The input array of integers sorted in ascending order
    """
    curr_idx = 0
    last_sorted_element = len(array)
    while last_sorted_element != 0:
        while curr_idx < last_sorted_element - 1:
            # bubble up the largest element to the end of the array every loop
            if array[curr_idx] >= array[curr_idx + 1]:
                swap(array, curr_idx, curr_idx + 1)
            curr_idx += 1
        last_sorted_element -= 1
        curr_idx = 0
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
