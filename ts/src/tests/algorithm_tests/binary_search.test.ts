import {
    iterativeLowBoundBinarySearch,
    recursiveBinarySearch,
} from '../../algorithms/binary_search';

describe('test iterative low bound binary search', () => {
    test('test1', () => {
        const arr = [-100, -2, 3, 5];

        expect(3).toEqual(iterativeLowBoundBinarySearch(arr, 5));
        expect(0).toEqual(iterativeLowBoundBinarySearch(arr, -100));
        expect(1).toEqual(iterativeLowBoundBinarySearch(arr, -2));
        expect(-1).toEqual(iterativeLowBoundBinarySearch(arr, -122));
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
            -2,
            3,
            5,
            5,
            10,
        ];

        expect(0).toEqual(iterativeLowBoundBinarySearch(arr, -100));
        expect(7).toEqual(iterativeLowBoundBinarySearch(arr, -50));
        expect(arr.length - 4).toEqual(iterativeLowBoundBinarySearch(arr, 3));
        expect(-1).toEqual(iterativeLowBoundBinarySearch(arr, 52));
    });

    test('test3', () => {
        const arr = [
            -1000,
            -1000,
            5,
            10,
            10,
            15,
            35,
            45,
            45,
            45,
            45,
            45,
            50,
            55,
        ];

        expect(0).toEqual(iterativeLowBoundBinarySearch(arr, -1000));
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
