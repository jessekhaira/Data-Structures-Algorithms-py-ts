import mergesort from "../../algorithms/mergeSort"

test('test 1', () => {
    let obj1 = [20,4,5,-9,-120]
    expect(mergesort(obj1)).toStrictEqual([-120,-9,4,5,20]);
});


test('test 2', () => {
    let obj1 = [-9,4,5,9,10,10,20,5,8,-30,-90];
    expect(mergesort(obj1)).toStrictEqual(obj1.sort((a,b) => a-b));
} )

