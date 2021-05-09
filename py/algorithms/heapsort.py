def heapsort(array):
    """
    This algorithm represents the heap sort algorithm, used to sort an array of integers in ascending
    order. This algorithm relies on a data structure called a max-heap to efficiently sort an array 
    of elements in-place.

    This algorithm does not produce a stable sort. This algorithm also has an additional operation of
    max-heapifying the input array, so on average it will run slower than quicksort, but has the advantage
    of having a worst case time complexity better then quicksort along with not using any space.

    Time:
        - O(NlogN) best/avg/worst

    Space:
        - O(1) best/avg/worst 

    N - represents the length of the input array
    """
    if not array:
        return []
    # heap sort relies on the array being a max-heap - therefore we have to heapify the array before
    # performing any swap operations
    heapify(array)
    # endIdx represents the idx which the current largest element in the max heap will swap to
    # first iteration, this will be the largest element in the heap so it should go in the last
    # idx spot, and so on from there
    endIdx = len(array) - 1
    while endIdx > 0:
        swap(array, 0, endIdx)
        endIdx -= 1
        # have to maintain heap property - every parent node has to have a value
        # greater than or equal to children nodes
        siftDown(array, 0, endIdx)
    return array


def heapify(array):
    """
    This function accepts an input array of integers, and max-heapifys the array. 

    Inputs:
        - array(list[int]): List of integers
    Outputs:
        - None 
    """
    pointer = (len(array) - 2) // 2
    while pointer >= 0:
        siftDown(array, pointer, len(array) - 1)
        pointer -= 1


def siftDown(array, start, end):
    """
    This function represents the siftdown algorithm used to maintain the heap property for a 
    max heap. This algorithm accepts an array of integers, and two integers that represent indices 
    within the heap such that start <= end. The element located at the start index is moved down 
    the heap until start > end, or the heap property is satisifed. 

    Inputs:
        - array(list[int]): List of integers representing a heap
        - start(int): Integer representing an index within the heap
        - end(int): Integer representing an index within the heap
    Outputs:
        - None
    """
    firstChild = start * 2 + 1
    while firstChild <= end:
        secondChild = start * 2 + 2 if start * 2 + 2 <= end else -1
        if secondChild != -1 and array[secondChild] > array[firstChild]:
            idxToSwap = secondChild
        else:
            idxToSwap = firstChild

        if array[idxToSwap] > array[start]:
            swap(array, idxToSwap, start)
            start = idxToSwap
            firstChild = start * 2 + 1
        else:
            break


def swap(array, i, j):
    """
    This function accepts an array of integers, and two integers i and j that represent
    indices within the array of integers, and swaps the values contained at the two indices.

    Inputs:
        - array(list[int]): List of integer 
        - i(int): Integer representing an index in the array
        - j(int): Integer representing an index in the array 
    Outputs:
        - None. Swaps inplace. 
    """
    array[i], array[j] = array[j], array[i]
