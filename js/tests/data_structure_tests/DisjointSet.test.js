import {DisjointSet} from "../../data structures/DisjointSet.js";




test('test 1', () => {
    let obj1 = new DisjointSet(20);
    expect(obj1.disjointSet).toStrictEqual(Array(20).fill(-1));
});


test('test2', () => {
    let obj1 = new DisjointSet(20)
    obj1.union(4,5);
    obj1.union(4,9);
    obj1.union(4,15);
    obj1.union(4,19);

    expect(4).toBe(obj1.find(4));
    expect(4).toBe(obj1.find(9));
    expect(4).toBe(obj1.find(15));
    expect(4).toBe(obj1.find(19));

});

test('test3', () => {
    let obj1 = new DisjointSet(20);
    obj1.union(1,5);
    obj1.union(1,9);
    obj1.union(4,15);
    obj1.union(4,3);
    obj1.union(4,16);
    obj1.union(3,1);

    expect(4).toBe(obj1.find(4));
    expect(4).toBe(obj1.find(3)); 
    expect(4).toBe(obj1.find(1)); 
    expect(1).not.toBe(obj1.find(9)); 

});