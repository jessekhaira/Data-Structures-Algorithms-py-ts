def quickSort(array):
    """
    This function represents an efficient implementation of the quick sort
    algorithm that runs in O(NlogN) time and O(logN) space, where N is the 
    length of the input array.

    Inputs:
        -> array(list[int]): List of integers
    Returns:
        -> array(list[int]): Sorted in ascending order
    """
    if not array:
        return
    quickSortHelper(array, 0, len(array)-1)
    return array

def quickSortHelper(array, start, end):
    if start >= end:
        return
    pivot = start
    ptrL = start+1
    ptrR = end

    while ptrL <= ptrR:
        if array[ptrL] > array[pivot] and array[pivot] > array[ptrR]:
            swap(array, ptrL, ptrR)
            ptrL += 1
            ptrR -= 1

        elif array[ptrL] <= array[pivot]:
            ptrL += 1

        elif array[ptrR] >= array[pivot]:
            ptrR -= 1

    swap(array, pivot, ptrR)
    if end - (ptrR+1) > (ptrR-1) - start:
        quickSortHelper(array, start, ptrR-1)
        quickSortHelper(array, ptrR+1, end)

    else:
        quickSortHelper(array, ptrR+1, end)
        quickSortHelper(array, start, ptrR-1)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i] 


