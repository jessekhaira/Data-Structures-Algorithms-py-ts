import {bubblesort} from '../../algorithms/bubbleSort.js';

test('test 1', () => {
    let obj1 = [20,4,5,-9,-120]
    expect(bubblesort(obj1)).toStrictEqual([-120,-9,4,5,20]);
});


test('test 2', () => {
    let obj1 = [-9,4,5,9,10,10,20,5,8,-30,-90];
    expect(bubblesort(obj1)).toStrictEqual(obj1.sort((a,b) => a-b));
})

test('test 3', () => {
    let obj1 = [-9,4,5,9,10,10,20,5,8,-30,-90, 20, 0, 0, 0, 3, 4,5, 0, 2,3, 3,3];
    expect(bubblesort(obj1)).toStrictEqual(obj1.sort((a,b) => a-b));
});
