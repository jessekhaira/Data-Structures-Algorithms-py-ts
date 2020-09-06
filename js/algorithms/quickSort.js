
/**
 * This function represents an efficient implementation of the quick sort
   algorithm that runs in O(NlogN) time and O(logN) space, where N is the 
   length of the input array.
 * @param {number[]} array List of integers to sort in ascending
    order
 * @returns {number[]} List of integers sorted in ascending order 
 */
function quickSort(array) {
   if (array == null) {
       return null;
   }
   quickSortHelper(array, 0, array.length-1);
   return array;
}

function quickSortHelper(array, start, end) {
    if (start >= end) {
        return;
    }
    let pivot = start;
    let ptrL = start+1;
    let ptrR = end;

    while (ptrL <= ptrR) {
        if (array[ptrL] > array[pivot] && array[pivot] > array[ptrR]) {
            swap(array, ptrL, ptrR);
            ptrL++;
            ptrR--;
        }

        else if (array[ptrL] <= array[pivot]) {
            ptrL++;
        }

        else if (array[ptrR] >= array[pivot]) {
            ptrR--;
        }
    }

    swap(array, pivot, ptrR);

    if (end - (ptrR+1) > (ptrR-1) - start) {
        quickSortHelper(array, start, ptrR-1);
        quickSortHelper(array, ptrR+1, end);
    }

    else {
        quickSortHelper(array, ptrR+1, end);
        quickSortHelper(array, start, ptrR-1);      
    }
}

function swap(array, i, j) {
    [array[i], array[j]] = [array[j], array[i]];
}

export default quickSort; 