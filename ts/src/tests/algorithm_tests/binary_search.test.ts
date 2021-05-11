import {
    iterativeBinarySearch,
    recursiveBinarySearch,
} from '../../algorithms/binary_search';

describe('test iterative and recursive binary search', () => {
    test('test iterative binary search', () => {
        const arr = [-100, -2, 3, 5];

        expect(3).toEqual(iterativeBinarySearch(arr, 5));
        expect(0).toEqual(iterativeBinarySearch(arr, -100));
        expect(1).toEqual(iterativeBinarySearch(arr, -2));
        expect(-1).toEqual(iterativeBinarySearch(arr, -122));
    });

    test('test recursive binary search', () => {
        const arr = [-100, -2, 3, 5];

        expect(3).toEqual(recursiveBinarySearch(arr, 5));
        expect(0).toEqual(recursiveBinarySearch(arr, -100));
        expect(1).toEqual(recursiveBinarySearch(arr, -2));
        expect(-1).toEqual(recursiveBinarySearch(arr, -122));
    });
});
