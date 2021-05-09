/**
 * This algorithm represents the bubble sort algorithm, meant to be used to sort an
    array of integers in ascending order.

 *Time:
 *- O(N**2) best/avg/worst
    
 *Space:
 *- O(1) best/avg/worst

 * N - number of elements in input array
 * @param {number[]} array Array of integers
 * @returns {number[]} Array of integers sorted in ascending order 
 */
function bubbleSort(array) {
    let endIdx = array.length;
    let currIdx = 0;
    while (endIdx > 0) {
        // bubble up largest element in array every time
        while (currIdx < endIdx - 1) {
            let currVal = array[currIdx];
            let nextVal = array[currIdx + 1];
            if (currVal >= nextVal) {
                swap(array, currIdx, currIdx + 1);
            }
            currIdx++;
        }
        currIdx = 0;
        endIdx--;
    }
    return array;
}

function swap(array, i, j) {
    [array[i], array[j]] = [array[j], array[i]];
}

export default bubbleSort;
