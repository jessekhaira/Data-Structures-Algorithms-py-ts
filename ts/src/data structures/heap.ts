/**
 *  This class represents a Heap.
    
    A heap is a special type of binary tree called a complete binary tree as every single level
    in the heap is filled up except for potentially the last level, and the levels are filled up
    from left to right.

    A heap also must obey the heap property. 
    
    For a max heap, the heap property entails:
    - The value of any given node must be greater than or equal to its children nodes values

    For a min heap, the heap property entails:
    - The value of any given node must be less than or equal to its children nodes values

    @constructor @public
 */
class Heap {
    comparator_function: (x: number, y: number) => 1 | 0;

    /**
     * @param {(Function|null)} custom_comparator Comparator function to be used to process this heap 
     * @param {Number} type_heap Integer indicating if heap is a min-heap or max-heap. 0 is min_heap, 1
        is max_heap. Important if custom comparator is null, otherwise we just use the comparator provided
        to process the heap. 
     */
    constructor(
        custom_comparator: null | ((x: number, y: number) => 1 | 0) = null,
        type_heap = 0,
    ) {
        if (!custom_comparator) {
            /*
                if the type_heap property is zero, the heap will be assumed to be a min-heap
                and the comparator function used to ensure the heap property is set appropriately 
                otherwise if the type_heap is 1, then the heap will be assumed to be a max-heap
            */
            if (type_heap === 0) {
                this.comparator_function = (x, y) => (x - y < 0 ? 1 : 0);
            } else {
                this.comparator_function = (x, y) => (x - y > 0 ? 1 : 0);
            }
        } else {
            this.comparator_function = custom_comparator;
        }
    }

    /**
     *  This method will create a heap out of the given array elements in-place, so the input
        array will be mutated.
        
     *  Time
     *- O(N) best/avg/worst
     
     * Space 
     *- O(1) best/avg/worst
     * @param {any[]} array 
     */
    heapify(array) {
        let parentIdx = Math.floor((array.length - 2) / 2);
        while (parentIdx >= 0) {
            this._siftDown(array, parentIdx, array.length - 1);
            parentIdx--;
        }
    }

    /**
     *  Inserts value into the min/max heap using the siftUp helper method.
     * 
     *  Time
     *- O(logN) best/avg/worst
     
     * Space 
     *- O(1) best/avg/worst
     * @param {any[]} heap Array of objects 
     * @param {any} val Object being pushed onto the heap
     */
    insert(heap, val) {
        heap.push(val);
        this._siftUp(heap, heap.length - 1, 0);
    }

    /**
     *  This method has the responsibility of ensuring the heap property is met when elements
        are inserted into the heap. 
        
        When an element is inserted into the heap, the heap property will most likely be violated.
        This method moves the inserted element up the heap until the heap property is satisifed.
     * @param {number[]} heap List of integers representing a heap
     * @param {number} start Integer representing the index in the array to start sifting up from
     * @param {number} end Integer representing the index in the array to stop sifting up 
     * @returns {undefined} Undefined. Sifts up in place.
     */
    _siftUp(heap, start, end) {
        let parentIdx = Math.floor((start - 1) / 2);
        while (parentIdx >= end) {
            // if heap property is not met, then we swap and continue upwards
            // if its true that heap[start] is less than heap[parent], we swap for min-heaps
            // if its true that heap[start] is greater than heap[parent], we swap for max-heaps
            if (this.comparator_function(heap[start], heap[parentIdx])) {
                this.swap(heap, start, parentIdx);
                start = parentIdx;
                parentIdx = Math.floor((start - 1) / 2);
            } else {
                break;
            }
        }
    }

    /**
     *  Removes the highest priority element from the min/max heap using the siftDown helper
        method.

     *  Time
     *- O(logN) best/avg/worst
     
     * Space 
     *- O(1) best/avg/worst
     * @param {any[]} heap Array of objects 
     */
    remove(heap) {
        if (heap == null || heap.length === 0) {
            return null;
        }
        this.swap(heap, 0, heap.length - 1);
        const removedVal = heap.pop();
        this._siftDown(heap, 0, heap.length - 1);
        return removedVal;
    }

    /**
     * This method has the responsibility of ensuring the heap property is met when elements
        are removed from the heap. 
        
        When the root element is removed from the heap, a new element is placed at the root. This method
        will move that element down the heap until the heap property is satisfied. 

     * @param {number[]} heap  List of integers representing a heap
     * @param {number} start Integer representing the index in the array to start sifting down from
     * @param {number} end Integer representing the index in the array to stop sifting down to
     * @returns {undefined} None. Sifts down in place. 

     */
    _siftDown(heap, start, end) {
        let currIdx = start;
        let firstChildIdx = currIdx * 2 + 1;
        while (firstChildIdx <= end) {
            const secondChildIdx =
                currIdx * 2 + 2 <= end ? currIdx * 2 + 2 : -1;
            let idxToSwap = null;
            if (
                secondChildIdx !== -1 &&
                this.comparator_function(
                    heap[secondChildIdx],
                    heap[firstChildIdx],
                )
            ) {
                idxToSwap = secondChildIdx;
            } else {
                idxToSwap = firstChildIdx;
            }

            if (this.comparator_function(heap[idxToSwap], heap[currIdx])) {
                this.swap(heap, currIdx, idxToSwap);
                currIdx = idxToSwap;
                firstChildIdx = currIdx * 2 + 1;
            } else {
                break;
            }
        }
    }

    /**
     * Peeks at highest priority element in the heap 
     * 
     *  Time
     *- O(1) best/avg/worst

     * Space 
     *- O(1) best/avg/worst
     * @param {any[]} heap Array of objects
     */
    peek(heap) {
        if (heap == null || heap.length === 0) {
            return null;
        }
        return heap[0];
    }

    /**
     * This method has the responsibility of swapping the values at two indices within an array
     * inplace.
     * @param {number[]} heap List of integers representing a heap
     * @param {number} i Integer representing an index within the input array
     * @param {number} j Integer representing an index within the input array
     * @returns {undefined} Swaps indices inplace
     */
    swap(heap, i, j) {
        [heap[i], heap[j]] = [heap[j], heap[i]];
    }
}

export { Heap };
