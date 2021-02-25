def bubblesort(array):
    """
    This algorithm represents the bubble sort algorithm, meant to be used to sort an
    array of integers in ascending order.

    Time:
        - O(N**2) best/avg/worst
    Space:
        - O(1) best/avg/worst

    N - number of elements in input array
    """
    curr_idx = 0
    last_sorted_element = len(array)
    while last_sorted_element != 0: 
        while curr_idx < last_sorted_element-1:
            # bubble up the largest element to the end of the array every loop
            if array[curr_idx] >= array[curr_idx+1]:
                swap(array, curr_idx, curr_idx+1)
            curr_idx += 1 
        last_sorted_element -= 1 
        curr_idx = 0 
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i] 
