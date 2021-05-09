import quickSelect from '../../algorithms/quick_select';

test('test 1', () => {
    let obj1 = [20, 4, 5, -9, -120];
    expect(quickSelect(obj1, 0)).toEqual(-120);
});

test('test 2', () => {
    let obj1 = [-9, 4, 5, 9, 10, 10, 20, 5, 8, -30, -90];
    expect(quickSelect(obj1, 5)).toEqual(5);
});
