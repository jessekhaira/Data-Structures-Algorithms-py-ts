def heapsort(array):
    """
    This algorithm represents the heap sort algorithm, used to sort an array of integers in ascending
    order. This algorithm relies on a data structure called a max-heap to efficiently sort an array 
    of elements in-place.

    This algorithm does not produce a stable sort. This algorithm also has an additional operation of
    max-heapifying the input array, so on average it will run slower than quicksort, but has the advantage
    of having a worst case time complexity better then quicksort along with not using any space.

    N -> represents the length of the input array
    Time Complexity b/a/w:
    - O(NlogN)

    Space Complexity:
    - O(1) 
    """
    if not array:
        return [] 
    heapify(array)
    # endIdx represents the idx which the current largest element in the max heap will swap to
    # first iteration, this will be the largest element in the heap so it should go in the last 
    # idx spot, and so on from there 
    endIdx = len(array)-1
    while endIdx > 0:
        swap(array, 0, endIdx) 
        endIdx -= 1 
        # have to maintain heap property - every parent node has to have a value 
        # greater than or equal to children nodes 
        siftDown(array, 0, endIdx) 
    return array


def heapify(array):
    pointer = (len(array)-2)//2
    while pointer >= 0:
        siftDown(array, pointer, len(array)-1)
        pointer -= 1 
    
def siftDown(array, start, end):
    firstChild = start*2+1
    while firstChild <= end:
        secondChild = start*2+2 if start*2+2 <= end else -1 
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
    array[i], array[j] = array[j], array[i] 