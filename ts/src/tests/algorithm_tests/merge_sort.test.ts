import mergesort from '../../algorithms/merge_sort';

test('test 1', () => {
    const obj1 = [20, 4, 5, -9, -120];
    expect(mergesort(obj1)).toStrictEqual(obj1.sort((a, b) => a - b));
});

test('test 2', () => {
    const obj1 = [-9, 4, 5, 9, 10, 10, 20, 5, 8, -30, -90];
    expect(mergesort(obj1)).toStrictEqual(obj1.sort((a, b) => a - b));
});

test('test 3', () => {
    const obj1 = [
        -9,
        4,
        5,
        9,
        10,
        10,
        20,
        5,
        8,
        -30,
        -90,
        20,
        0,
        0,
        0,
        3,
        4,
        5,
        0,
        2,
        3,
        3,
        3,
    ];
    expect(mergesort(obj1)).toStrictEqual(obj1.sort((a, b) => a - b));
});

test('test 4', () => {
    const obj = [
        -10,
        -9,
        -8,
        5,
        2,
        8,
        -12321,
        123012321,
        1232131258,
        1.231,
        1.1235,
        1238581,
        -1231230,
        -1232139,
    ];

    expect(mergesort(obj)).toStrictEqual(obj.sort((a, b) => a - b));
});

test('test edge case', () => {
    const obj: number[] = [];

    expect(mergesort(obj)).toStrictEqual(null);
});
