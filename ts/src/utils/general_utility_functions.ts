/**
 * This method has the responsibility of swapping the values at
 * two indices within an array inplace.
 * @param {T[]} arr List of integers representing a heap
 * @param {number} i Integer representing an index within the input array
 * @param {number} j Integer representing an index within the input array
 */
// eslint-disable-next-line
function swap(arr: any[], i: number, j: number): void {
    // eslint-disable-next-line
    [arr[i], arr[j]] = [arr[j], arr[i]];
}

export { swap };
