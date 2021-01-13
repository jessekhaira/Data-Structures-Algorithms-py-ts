/**
 *  This algorithm represents the heap sort algorithm, used to sort an array of integers in ascending
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
 * @param {number[]} array List of integers to sort in ascending order
 * @returns {number[]} List of integers in ascending order 
 */
function heapsort(array) {
    if (array == null || array.length == 0) {
        return [];
    }
    heapify(array);
    // endIdx represents the idx which the current largest element in the max heap will swap to
    // first iteration, this will be the largest element in the heap so it should go in the last 
    // idx spot, and so on from there 
    let endIdx = array.length-1;
    while (endIdx > 0) {
        swap(array, 0, endIdx);
        endIdx--;
        // have to maintain heap property - every parent node has to have a value 
        // greater than or equal to children nodes         
        siftDown(array, 0, endIdx);
    }
    return array;
}


/**
 * This function accepts an input array of integers, and max-heapifys the array. 
 * @param {number[]} array List of integers 
 */
function heapify(array) {
    let parentIdx = Math.floor(array.length-2/2);
    while (parentIdx >= 0) {
        siftDown(array, parentIdx, array.length-1);
        parentIdx--;
    }
}

/**
 * This function accepts an array of integers, and two integers i and j that represent
 * indices within the array of integers, and swaps the values contained at the two indices.
 * @param {number[]} array List of integers
 * @param {number} i int that represents an index in the array
 * @param {number} j int that represents an index in the array 
 * @returns {undefined} Swaps inplace 
 */
function swap(array, i, j) {
    [array[i], array[j]] = [array[j], array[i]];
}

/**
 *  This function represents the siftdown algorithm used to maintain the heap property for a 
    max heap. This algorithm accepts an array of integers, and two integers that represent indices 
    within the heap such that start <= end. The element located at the start index is moved down 
    the heap until start > end, or the heap property is satisifed. 

 * @param {number[]} array List of integers representing a heap
 * @param {number} start Integer representing an index within the heap
 * @param {number} end Integer representing an index within the heap
 * @returns {undefined} Sifts down in place 
 */
function siftDown(array, start, end) {
    let firstChild = start*2+1;
    while (firstChild <= end) {
        let secondChild = (start*2+2 <= end ? start*2+2: -1);
        let idxToSwap = null;
        if (secondChild !== -1 && array[secondChild] > array[firstChild]) {
            idxToSwap = secondChild;
        }
        else {
            idxToSwap = firstChild;
        }

        if (array[idxToSwap] > array[start]) {
            swap(array, idxToSwap, start);
            start = idxToSwap;
            firstChild = start*2+1;
        }
        else {
            break; 
        }
    }
}

export default heapsort; 