def quickselect(array, k):
    """
    This function represents the quickselect algorithm, which is used
    to efficiently find the kth smallest element in an unordered list.
    This algorithm is based off of quicksort.  

    Time - O(N) best/average, O(N**2) worst
    Space - O(logN) 

    Inputs:
        - array (list[int]): List of integers from which to retrieve the kth smallest value 
        - k (int): Value between 0<=k<len(array). Represents the (sorted) index from which
        to retrieve the output value. 
    
    Example:

    array = [3,5,-2,1,4,5]
    output = quickselect(array, 0) 
    print(output) # will be -2
    """
    assert k <= len(array), "k has to be within 0 to len(array)-1!"
    kth_elem = quickselectHelper(array, k, 0, len(array)-1)
    return kth_elem


def quickselectHelper(array, k, start, end):
    if start >= end:
        return array[start] if start == k else "Not found"
    pivot = start
    ptr1 = start+1
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
    if ptr2 == k:
        return array[k]
    elif ptr2 > k:
        return quickselectHelper(array, k, start, ptr2-1)
    else:
        return quickselectHelper(array, k, ptr2+1, end)        

    
def swap(array, i, j):
    array[i], array[j] = array[j], array[i] 
