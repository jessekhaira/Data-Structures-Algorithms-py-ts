/**
 *  This algorithm represents the binary search algorithm implemented
    iteratively. This algorithm finds the position of a target value within
    within a sorted array by dividing a range of values into halves, and continuing 
    to narrow down the search space until the desired value is found. As such, 
    it is an example of a divide and conquer algorithm. 

    This algorithm assumes the simplest case of binary search searching over an explicit
    sorted array, but the search space can be any space that is sorted. For example, 
    binary search can be used on functions which are monotonically increasing 
    or decreasing in order to find the lowest possible value some condition is met (low
    bound binary search), or the highest possible value some condition is met (high bound
    binary search). This means binary searching over the inputs of these functions to
    determine which input produces the most optimal value -- highest or lowest output value 
    that meets some condition. 

    Key tip: If the search space consists of integers, then test the binary search on a two
    element set in order to ensure convergence. 
 * @param {number[]} array List of integers sorted in ascending order
 * @param {number} target Integer we're looking for in the array 
 * @returns {number} Represents the idx at which the target value occurs, or -1 if it does not occur
 */
export function iterativeBinarySearch(array, target) {
    if (array == null) {
        return -1;
    }
    let left = 0;
    let right = array.length - 1;
    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);

        if (array[mid] === target) {
            return mid;
        }
        if (array[mid] > target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }
    return array[left] === target ? left : -1;
}

/**
 *  This algorithm represents the binary search algorithm implemented
    recursively. This algorithm finds the position of a target value within
    within a sorted array by dividing a range of values into halves, and continuing 
    to narrow down the search space until the desired value is found. As such, 
    it is an example of a divide and conquer algorithm. 

    This algorithm assumes the simplest case of binary search searching over an explicit
    sorted array, but the search space can be any space that is sorted. For example, binary
    search can be used on functions which are monotonically increasing or decreasing 
    in order to find the lowest possible value some condition is met (low bound binary search), 
    or the highest possible value some condition is met (high bound binary search). This means 
    binary searching over the inputs of these functions to determine which input produces the most 
    optimal value -- highest or lowest output value that meets some condition. 

    Key tip: If the search space consists of integers, then test the binary search on a two
    element set in order to ensure convergence. 
 * @param {number[]} array List of integers sorted in ascending order
 * @param {number} target Integer we're looking for in the array 
 * @returns {number} Represents the idx at which the target value occurs, or -1 if it does not occur
 */
export function recursiveBinarySearch(array, target) {
    return recursiveHelperBinarySearch(array, target, 0, array.length - 1);
}

function recursiveHelperBinarySearch(array, target, left, right) {
    if (left == right) {
        return array[left] === target ? left : -1;
    }
    const mid = left + Math.floor((right - left) / 2);
    if (array[mid] === target) {
        return mid;
    }
    if (array[mid] > target) {
        return recursiveHelperBinarySearch(array, target, left, mid);
    }
    return recursiveHelperBinarySearch(array, target, mid + 1, right);
}
