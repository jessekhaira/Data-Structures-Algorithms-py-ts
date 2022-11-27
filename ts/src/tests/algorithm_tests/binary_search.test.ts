import {
    iterativeBinarySearch,
    recursiveBinarySearch,
} from '../../algorithms/binary_search';

describe('test iterative low bound binary search', () => {
    test('test1', () => {
        const arr = [-100, -2, 3, 5];

        expect(3).toEqual(iterativeBinarySearch(arr, 5));
        expect(0).toEqual(iterativeBinarySearch(arr, -100));
        expect(1).toEqual(iterativeBinarySearch(arr, -2));
        expect(-1).toEqual(iterativeBinarySearch(arr, -122));
    });

    test('test2', () => {
        const arr = [
            -100,
            -100,
            -100,
            -100,
            -100,
            -100,
            -100,
            -50,
            -50,
            5,
            10,
            -2,
            3,
            5,
        ];

        expect(0).toEqual(iterativeBinarySearch(arr, -100));
        expect(7).toEqual(iterativeBinarySearch(arr, -50));
    });
});

describe('test recursive binary search', () => {
    test('test recursive binary search', () => {
        const arr = [-100, -2, 3, 5];

        expect(3).toEqual(recursiveBinarySearch(arr, 5));
        expect(0).toEqual(recursiveBinarySearch(arr, -100));
        expect(1).toEqual(recursiveBinarySearch(arr, -2));
        expect(-1).toEqual(recursiveBinarySearch(arr, -122));
    });
});
