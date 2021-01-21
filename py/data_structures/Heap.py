class Heap:
    """
    This class represents a Heap.
    
    A heap is a special type of binary tree called a complete binary tree as every single level
    in the heap is filled up except for potentially the last level, and the levels are filled up
    from left to right.

    A heap also must obey the heap property. 
    
    For a max heap, the heap property entails:
    - The value of any given node must be greater than or equal to its children nodes values

    For a min heap, the heap property entails:
    - The value of any given node must be less than or equal to its children nodes values

    Inputs:
        -> custom_comparator (Function | None): Comparator function to be used to process this heap 
        -> type_heap (int): Integer indicating if heap is a min-heap or max-heap. 0 is min_heap, 1
        is max_heap. 
    """
    def __init__(self, custom_comparator = None, type_heap =0):
        if not custom_comparator:
            if type_heap == 0:
                self.comparator_func = lambda x,y: 1 if x-y < 0 else 0 
            else:
                self.comparator_func = lambda x,y: 1 if x-y > 0 else 0 
        else:
            self.comparator_func = custom_comparator 
        
    def heapify(self, array):
        """
        This method will create a heap out of the given array elements in-place, so the input
        array will be mutated.
        
        T O(N) best/avg/worst
        S O(1) 
        """
        firstParentIdx = (len(array)-2)//2
        while firstParentIdx >= 0:
            self._siftDown(array, firstParentIdx, len(array)-1)
            firstParentIdx -= 1
        
    def insert(self, heap, val):
        """
        Inserts value into the min/max heap using the siftUp helper method.
        
        T O(logN) best/avg/worst
        S O(1) 
        """ 
        heap.append(val)
        self._siftUp(heap, len(heap)-1, 0)        

    def peek(self, heap):
        """
        Peeks at the highest priority element in the min/max heap.

        T O(1) best/avg/worst
        S O(1) 
        """ 
        if not heap:
            return 
        return heap[0] 

    def remove(self, heap):
        """
        Removes the highest priority element from the min/max heap using the siftDown helper
        method.

        T O(logN) best/avg/worst
        S O(1)
        """
        if not heap:
            return 
        self._swap(heap, 0, len(heap)-1)
        removedVal = heap.pop()
        self._siftDown(heap, 0, len(heap)-1)
        return removedVal


    def _siftDown(self, heap, start, end):
        """
        Used to ensure the heap property is met when a value has been removed from the heap by moving
        the new root down the heap until the heap property is satisfied. Also used for heapifying.
        """
        currIdx = start 
        firstChildIdx = start*2+1
        while firstChildIdx <= end:
            secondChildIdx = currIdx * 2 + 2 if currIdx*2+2 <= end else -1
            # If val at secondChildIdx is less than val at firstChildIdx in minHeaps, then its candidate to consider when swapping
            # If val at secondChildIdx is greater than val at firstChildIdx in maxHeaps, then its candidate to consider when swapping
            if secondChildIdx != -1 and self.comparator_func(heap[secondChildIdx], heap[firstChildIdx]):
                idxToSwap = secondChildIdx
            else:
                idxToSwap = firstChildIdx
            if self.comparator_func(heap[idxToSwap], heap[currIdx]):
                self._swap(heap, idxToSwap, currIdx)
                currIdx = idxToSwap
                firstChildIdx = currIdx *2 + 1
            else:
                break 


    def _siftUp(self, heap, start, end):
        """
        Used to ensure the heap property is met when a value has been inserted into the 
        heap by moving the inserted value up the heap until the heap property has been satisfied
        """
        parentIdx = (start-1)//2
        while parentIdx >= end:
            # if heap property is not met, then we swap and continue upwards
            # if its true that heap[start] is less than heap[parent], we swap for min-heaps
            # if its true that heap[start] is greater than heap[parent], we swap for max-heaps
            if self.comparator_func(heap[start], heap[parentIdx]):
                self._swap(heap, start, parentIdx)
                start = parentIdx
                parentIdx = (start-1)//2
            else:
                break

    def _swap(self, heap, i, j):
        """
        This method has the responsibility of swapping the values at two indices within an array.

        Inputs:
            - heap(list[int]): List of integers representing a heap
            - i (int): Integer representing an index within the input array
            - j (int): Integer representing an index within the input array
        Outputs:
            - None 
        """ 
        heap[i], heap[j] = heap[j], heap[i]
