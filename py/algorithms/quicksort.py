def quickSort(array):
    """
    This function represents an efficient implementation of the quick sort algorithm.

    Time:
        - O(NlogN) best/avg
        - O(N**2) worst 

    Space:
        - O(logN) best/avg/worst 
    
    N - number of elements in the input array 

    Inputs:
        - array(list[int]): List of integers
    
    Returns:
        - The input list of integers sorted in ascending order 
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


