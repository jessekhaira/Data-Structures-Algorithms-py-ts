""" This module contains utility functions used by many data structures
and algorithms """
from typing import List, Any


def swap(array: List[Any], i: int, j: int) -> None:
    """ This method has the responsibility of swapping the values at two indices
    within an array inplace.

    Inputs:
        array:
            List of objects representing an array

        i:
            Integer representing an index within the input array

        j:
            Integer representing an index within the input array
    """
    array[i], array[j] = array[j], array[i]
