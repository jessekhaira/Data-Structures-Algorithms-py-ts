def merge_sort(array):
    """This function represents the merge sort algorithm used to
    sort an array of integers in ascending order.
    
    Time:
        O(N**2)
    Space:
        O(N) 
    
    Where N is the length of the input array

    Args:
        array:
            List of integers to sort in ascending order

    Returns:
        Input list of integers sorted in ascending order

    """
    auxArray = array[:]
    merge_sort_helper(array, auxArray, 0, len(array) - 1)
    return array


def merge_sort_helper(array, auxArray, start, end):
    """
    This helper function helps to implement mergesort. This function is a recursive function that 
    recurses to the base case of start >= end -> when the pointers point to the same element or 
    when its an invalid configuration, return.

    We then partition and sort the main array using the help of the auxArray.

    Inputs:
        - array(list[int]): List of integers to sort from start ptr to end ptr
        - auxArray(list[int]): Copy of the main array used to help sort the array
        - start(int): Integer representing start idx to sort from
        - end(int): Integer representing end idx to sort to
    """
    if start >= end:
        return
    # auxArray isn't even sorted yet, can't be used to sort the main array
    # so we sort auxArray first before trying to sort main array
    # have to recurse to base case so we break array in half and sort each half recursively
    middle = start + (end - start) // 2
    merge_sort_helper(auxArray, array, start, middle)
    merge_sort_helper(auxArray, array, middle + 1, end)
    _merge(array, auxArray, start, middle, middle + 1, end)


def _merge(array, auxArray, lstart, lend, rstart, rend):
    """
    This function carries out the merge operation using the two sorted partitions of auxArray
    from lstart to lend, and rstart to rend, to sort the main array.

    Inputs:
        - array(list[int]): List of integers to sort from lstart to rend 
        - auxArray(list[int]): Copy of the main array used to help sort the array
        - lstart(int): Integer representing start idx of sorted left portion of auxArray
        - lend(int): Integer representing end idx of sorted left portion of auxArray
        - rstart(int): Integer representing start idx of sorted right portion of auxArray
        - rend(int): Integer representing end idx of sorted right portion of auxArray 
    """
    ptr1 = lstart
    ptrArr = lstart
    ptr2 = rstart
    while ptr1 <= lend and ptr2 <= rend:
        if auxArray[ptr1] <= auxArray[ptr2]:
            array[ptrArr] = auxArray[ptr1]
            ptr1 += 1
        else:
            array[ptrArr] = auxArray[ptr2]
            ptr2 += 1
        ptrArr += 1

    while ptr1 <= lend:
        array[ptrArr] = auxArray[ptr1]
        ptr1 += 1
        ptrArr += 1

    while ptr2 <= rend:
        array[ptrArr] = auxArray[ptr2]
        ptr2 += 1
        ptrArr += 1
