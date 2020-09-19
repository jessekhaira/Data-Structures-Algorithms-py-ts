/**
 *  This function represents the quickselect algorithm, which is used
    to efficiently find the kth smallest element in an unordered list.
    This algorithm is based off of quicksort.  

    Time - O(N) best/average, O(N**2) worst
    Space - O(logN) 
    
    Example:

    array = [3,5,-2,1,4,5]
    output = quickselect(array, 0) 
    print(output) # will be -2
 * @param {number[]} array List of integers from which to retrieve the kth smallest value 
 * @param {number} k Value between 0<=k<len(array). Represents the (sorted) index from which
 * to retrieve the output value. 
 * 
 * @returns {number} Value between 0<=k<len(array). Represents the (sorted) index from which
    to retrieve the output value. 
 */
function quickselect(array, k) {
    if (array == null) {
        return null;
    }
    else if (!(0<=k<array.length-1)) {
        return "k has to be between 0 and array.length-1";
    }
    let output = quickselectHelper(array, k, 0, array.length-1);
    return output;
}


function quickselectHelper(array, k, start, end) {
    if (start >= end) {
        return (start === k ? array[start]: "Value not found");
    }
    let pivot = start;
    let ptr1 = start+1;
    let ptr2 = end;
    while (ptr1 <= ptr2) {
        if (array[ptr1] > array[pivot] && array[pivot] > array[ptr2]) {
            [array[ptr1], array[ptr2]] = [array[ptr2], array[ptr1]];
        }
        else if (array[ptr1] <= array[pivot]) {
            ptr1++;
        }
        else if (array[ptr2] >= array[pivot]) {
            ptr2--;
        }
    }
    [array[pivot], array[ptr2]] = [array[ptr2], array[pivot]];
    if (k === ptr2) {
        return array[k];
    }
    else if (ptr2 > k) {
        return quickselectHelper(array, k, start, ptr2-1);
    }
    else {
        return quickselectHelper(array, k, ptr2+1, end);
    }
}

export {quickselect}; 