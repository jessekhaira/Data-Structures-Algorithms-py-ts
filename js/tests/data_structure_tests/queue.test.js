import {Queue} from '../../data structures/Queue.js';


test('test1', () => {
    let testObj = new Queue();
    expect(testObj.top).toThrow();
    expect(testObj.pop).toThrow();
})