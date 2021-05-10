/**
 * This algorithm represents the bubble sort algorithm,
 *  meant to be used to sort an array of integers in
 *  ascending order.

 *Time:
 *- O(N**2) best/avg/worst
    
 *Space:
 *- O(1) best/avg/worst

 * N - number of elements in input array
 * @param {number[]} array Array of integers
 * @returns {number[]} Array of integers sorted in ascending order 
 */
function bubbleSort(array: number[]): number[] {
    let endIdx = array.length;
    let currIdx = 0;
    while (endIdx > 0) {
        // bubble up largest element in array every time
        while (currIdx < endIdx - 1) {
            const currVal = array[currIdx];
            const nextVal = array[currIdx + 1];
            if (currVal >= nextVal) {
                swap(array, currIdx, currIdx + 1);
            }
            currIdx += 1;
        }
        currIdx = 0;
        endIdx -= 1;
    }
    return array;
}

function swap(array: number[], i: number, j: number) {
    [array[i], array[j]] = [array[j], array[i]];
}

export default bubbleSort;
