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
function bubblesort(array) {
    let end_idx = array.length;
    let curr_idx = 0;
    while (end_idx > 0) {
        // bubble up largest element in array every time 
        while (curr_idx < end_idx-1) {
            let curr_val = array[curr_idx];
            let next_val = array[curr_idx+1];
            if (curr_val >= next_val) {
                swap(array, curr_idx, curr_idx+1)
            }
            curr_idx++;
        }
        curr_idx = 0; 
        end_idx--;
    }
    return array; 
}

function swap(array, i, j) {
    [array[i], array[j]] = [array[j], array[i]]; 
}

export {bubblesort}; 