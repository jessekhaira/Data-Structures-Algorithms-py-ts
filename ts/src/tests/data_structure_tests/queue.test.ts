import Queue from '../../data structures/queue';

test('test1', () => {
    const testObj = new Queue();
    expect(testObj.top).toThrow();
    expect(testObj.pop).toThrow();
});

test('test2', () => {
    const testObj = new Queue();
    for (let i = 0; i < 150; i += 1) {
        testObj.push(i);
    }

    for (let i = 0; i < 150; i += 1) {
        expect(testObj.length()).toEqual(150 - i);
        expect(testObj.top()).toEqual(i);
        expect(testObj.pop()).toEqual(i);
    }

    expect(testObj.top).toThrow();
});
