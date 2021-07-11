import quickSort from '../../algorithms/quick_sort';

test('test 1', () => {
    const obj1 = [20, 4, 5, -9, -120];
    expect(quickSort(obj1)).toStrictEqual([-120, -9, 4, 5, 20]);
});

test('test 2', () => {
    const obj1 = [-9, 4, 5, 9, 10, 10, 20, 5, 8, -30, -90];
    expect(quickSort(obj1)).toStrictEqual(obj1.sort((a, b) => a - b));
});
