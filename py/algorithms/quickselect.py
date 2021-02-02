def quickselect(array, k):
    """
    This function represents the recursive quickselect algorithm, which is used to efficiently find the kth 
    smallest element in an unordered list. This algorithm chooses a pivot element, which in this implementation
    is chosen to be the leftmost element of the array in every subproblem. Every element of the array is then sorted
    with respect to this pivot element, with the pivot element then being inserted into its final sorted position. 
    If the final sorted position is equal to k, the value sorted in the index is returned. If the final sorted position
    is not equal to k, the portion of the array which contains k is recursed into. 

    Time 
        - O(N) best/average
        - O(N**2) worst
    Space 
        - O(logN) best/average/worst

    N - length of the input array

    Inputs:
        - array (list[int]): List of integers from which to retrieve the kth smallest value 
        - k (int): Value between 0<=k<len(array). Represents the (sorted) index from which
        to retrieve the output value. 
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
