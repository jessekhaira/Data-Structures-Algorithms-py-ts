/**
 *  This function represents an efficient implementation of the quick
 *  sort algorithm. Like the merge sort algorithm, this algorithm uses
 *  the divide and conquer strategy to efficiently sort an array. Unlike merge 
    sort, which splits arrays in half every time, quicksort places a pivot
    element (chosen to be the leftmost element in the array in this
    implementation) to its final sorted position. Quicksort then recurses
    and sorts all the elements to the left of a pivot element, and all the
    elements to the right of a pivot element until the base case is hit.   

 * Time:
 *- O(NlogN) best/avg
 *- O(N**2) worst 

 *Space:
 *- O(logN) best/avg/worst 
    
 *N - number of elements in the input array 

 * @param {number[]} array List of integers to sort in ascending order
 * @returns {number[]} List of integers sorted in ascending order 
 */
function quickSort(array: number[]): number[] {
    if (array == null) {
        return null;
    }
    quickSortHelper(array, 0, array.length - 1);
    return array;
}

function quickSortHelper(array, start, end) {
    if (start >= end) {
        return;
    }
    const pivot = start;
    let ptrL = start + 1;
    let ptrR = end;

    while (ptrL <= ptrR) {
        if (array[ptrL] > array[pivot] && array[pivot] > array[ptrR]) {
            swap(array, ptrL, ptrR);
            ptrL++;
            ptrR--;
        } else if (array[ptrL] <= array[pivot]) {
            ptrL++;
        } else if (array[ptrR] >= array[pivot]) {
            ptrR--;
        }
    }

    swap(array, pivot, ptrR);

    if (end - (ptrR + 1) > ptrR - 1 - start) {
        quickSortHelper(array, start, ptrR - 1);
        quickSortHelper(array, ptrR + 1, end);
    } else {
        quickSortHelper(array, ptrR + 1, end);
        quickSortHelper(array, start, ptrR - 1);
    }
}

function swap(array, i, j) {
    [array[i], array[j]] = [array[j], array[i]];
}

export default quickSort;
