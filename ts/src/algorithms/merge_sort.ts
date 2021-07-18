/**
 * This function carries out the merge operation using the two sorted partitions
 * of auxArray from lstart to lend, and rstart to rend, to sort the main array.
 *
 *
 *
 * @param {number[]} array List of integers to sort from lstart to rend
 * @param {number[]} auxArray Copy of the main array used to help sort the array
 * @param {number} lstart Integer representing start idx of sorted left portion
 * of auxArray
 * @param {number} lend Integer representing end idx of sorted left portion
 * of auxArray
 * @param {number} rstart Integer representing start idx of sorted right
 * portion of auxArray
 * @param {number} rend Integer representing end idx of sorted right
 * portion of auxArray
 *
 */
function merge(
    array: number[],
    auxArray: number[],
    lstart: number,
    lend: number,
    rstart: number,
    rend: number,
): void {
    let ptr1 = lstart;
    let ptr2 = rstart;
    let ptrArr = lstart;
    while (ptr1 <= lend && ptr2 <= rend) {
        if (auxArray[ptr1] <= auxArray[ptr2]) {
            array[ptrArr] = auxArray[ptr1];
            ptr1 += 1;
        } else {
            array[ptrArr] = auxArray[ptr2];
            ptr2 += 1;
        }
        ptrArr += 1;
    }

    while (ptr1 <= lend) {
        array[ptrArr] = auxArray[ptr1];
        ptrArr += 1;
        ptr1 += 1;
    }

    while (ptr2 <= rend) {
        array[ptrArr] = auxArray[ptr2];
        ptr2 += 1;
        ptrArr += 1;
    }
}

/**
 *  This helper function helps to implement mergesort.
    This function is a recursive function that 
    recurses to the base case of start >= end -> when
    the pointers point to the same element or when its an
    invalid configuration, return.

    We then partition and sort the main array using the help of
    the auxArray.
 * @param {number[]} array List of integers to sort from start ptr to end ptr
 * @param {number[]} auxArray Copy of the main array used to help sort the array
 * @param {number} start Integer representing start idx to sort from
 * @param {number} end Integer representing end idx to sort to
 */
function mergeSortHelper(
    array: number[],
    auxArray: number[],
    start: number,
    end: number,
) {
    if (start >= end) {
        return;
    }
    const middle = start + Math.floor((end - start) / 2);
    mergeSortHelper(auxArray, array, start, middle);
    mergeSortHelper(auxArray, array, middle + 1, end);
    _merge(array, auxArray, start, middle, middle + 1, end);
}

/**
 * This function represents the merge sort algorithm. Merge
 * sort is an algorithm used to efficiently sort an array of 
 * integers in O(NlogN) time using just O(N) space.
 * 
 * Time:
 *   O(NlogN) best/avg/worst
 * 
 * Space:
 *   O(N) best/avg/worst
 * 
 * Where N is the length of the input array of integers
 * 
 * @param {number[]} array List of integers to sort in ascending
    order
 * @returns {number[]} List of integers sorted in ascending order
 */
function mergeSort(array: number[]): number[] | null {
    if (array == null || array.length === 0) {
        return null;
    }
    const auxArray = array.slice();
    mergeSortHelper(array, auxArray, 0, array.length - 1);
    return array;
}

export default mergeSort;
