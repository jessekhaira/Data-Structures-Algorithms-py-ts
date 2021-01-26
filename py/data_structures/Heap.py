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
            # if the type_heap property is zero, the heap will be assumed to be a min-heap
            # and the comparator function used to ensure the heap property is set appropriately 
            # otherwise if the type_heap is 1, then the heap will be assumed to be a max-heap
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
        
        Time
            - O(N) best/avg/worst
        Space 
            - O(1) best/avg/worst
        """
        firstParentIdx = (len(array)-2)//2
        while firstParentIdx >= 0:
            self._siftDown(array, firstParentIdx, len(array)-1)
            firstParentIdx -= 1
        
    def insert(self, heap, val):
        """
        Inserts value into the min/max heap using the siftUp helper method.
        
        Time
            - O(logN) best/avg/worst
        Space 
            - O(1) best/avg/worst
        """ 
        heap.append(val)
        self._siftUp(heap, len(heap)-1, 0)        

    def peek(self, heap):
        """
        Peeks at the highest priority element in the min/max heap.

        Time 
            - O(1) best/avg/worst
        Space 
            - O(1) best/avg/worst
        """ 
        if not heap:
            return 
        return heap[0] 

    def remove(self, heap):
        """
        Removes the highest priority element from the min/max heap using the siftDown helper
        method.

        Time
            - O(logN) best/avg/worst
        Space 
            - O(1) best/avg/worst
        """
        if not heap:
            return 
        self._swap(heap, 0, len(heap)-1)
        removedVal = heap.pop()
        self._siftDown(heap, 0, len(heap)-1)
        return removedVal


    def _siftDown(self, heap, start, end):
        """
        This method has the responsibility of ensuring the heap property is met when elements
        are removed from the heap. 
        
        When the root element is removed from the heap, a new element is placed at the root. 
        This method will move that element down the heap until the heap property is satisfied. 

        Inputs:
            - heap(list[int]): List of integers representing a heap
            - start (int): Integer representing the index in the array to start sifting down from
            - end (int): Integer representing the index in the array to stop sifting down to
        Outputs:
            - None. Sifts down in place. 
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
        This method has the responsibility of ensuring the heap property is met when elements
        are inserted into the heap. 
        
        When an element is inserted into the heap, the heap property will most likely be violated.
        This method moves the inserted element up the heap until the heap property is satisifed.

        Inputs:
            - heap(list[int]): List of integers representing a heap
            - start (int): Integer representing the index in the array to start sifting up from
            - end (int): Integer representing the index in the array to stop sifting up 
        Outputs:
            - None. Sifts up in place. 
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
        This method has the responsibility of swapping the values at two indices within an array
        inplace. 

        Inputs:
            - heap(list[int]): List of integers representing a heap
            - i (int): Integer representing an index within the input array
            - j (int): Integer representing an index within the input array
        Outputs:
            - None. Swaps indices inplace. 
        """ 
        heap[i], heap[j] = heap[j], heap[i]
