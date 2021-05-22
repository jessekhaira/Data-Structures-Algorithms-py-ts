function iterativeQuickSelect(array: number[], k: number): number | null {
    let left = 0;
    let right = array.length - 1;
    while (left <= right) {
        const pivot = left;
        let p1 = pivot + 1;
        let p2 = right;
        while (p1 <= p2) {
            if (array[p1] >= array[pivot] && array[pivot] >= array[p2]) {
                [array[p1], array[p2]] = [array[p2], array[p1]];
                p1 += 1;
                p2 -= 1;
            } else if (array[p1] <= array[pivot]) {
                p1 += 1;
            } else if (array[p2] >= array[pivot]) {
                p2 -= 1;
            }
        }
        [array[pivot], array[p2]] = [array[p2], array[pivot]];
        if (p2 === k) {
            return array[p2];
        }
        if (p2 < k) {
            left = p2 + 1;
        } else {
            right = p2 - 1;
        }
    }
    return k === left ? left : null;
}

function recursiveQuickSelectHelper(
    array: number[],
    k: number,
    start: number,
    end: number,
): number | null {
    if (start >= end) {
        return start === k ? array[start] : null;
    }
    const pivot = start;
    let ptr1 = start + 1;
    let ptr2 = end;
    while (ptr1 <= ptr2) {
        if (array[ptr1] > array[pivot] && array[pivot] > array[ptr2]) {
            [array[ptr1], array[ptr2]] = [array[ptr2], array[ptr1]];
        } else if (array[ptr1] <= array[pivot]) {
            ptr1 += 1;
        } else if (array[ptr2] >= array[pivot]) {
            ptr2 -= 1;
        }
    }
    [array[pivot], array[ptr2]] = [array[ptr2], array[pivot]];
    if (k === ptr2) {
        return array[k];
    }
    if (ptr2 > k) {
        return recursiveQuickSelectHelper(array, k, start, ptr2 - 1);
    }
    return recursiveQuickSelectHelper(array, k, ptr2 + 1, end);
}

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

 * @param {number[]} array List of integers from which to retrieve
    the kth smallest value 
 * @param {number} k Value between 0<=k<len(array). Represents the
    (sorted) index from which to retrieve the output value. 
 * 
 * @returns {number} Value between 0<=k<len(array). Represents the
 * (sorted) index from which to retrieve the output value. 
 */
function recursiveQuickSelect(array: number[], k: number): number | null {
    const output = recursiveQuickSelectHelper(array, k, 0, array.length - 1);
    return output;
}

export { recursiveQuickSelect, iterativeQuickSelect };
