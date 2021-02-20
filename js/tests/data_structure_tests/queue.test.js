import {Queue} from '../../data structures/Queue.js';


test('test1', () => {
    let testObj = new Queue();
    expect(testObj.top).toThrow();
    expect(testObj.pop).toThrow();
})

test('test2', () => {
    let testObj = new Queue(); 
    for (let i=0;i<150;i++) {
        testObj.push(i);
    }

    for (let i=0; i<150; i++) {
        expect(testObj.length()).toEqual(150-i);
        expect(testObj.top()).toEqual(i);
        expect(testObj.pop()).toEqual(i);
    }

    expect(testObj.top).toThrow(); 
})