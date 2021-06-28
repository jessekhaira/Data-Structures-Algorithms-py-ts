import Queue from '../../data structures/queue';

test('test1', () => {
    const testObj = new Queue<number>();
    expect(testObj.top).toThrow();
    expect(testObj.pop).toThrow();
});

test('test2', () => {
    const testObj = new Queue<number>();
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

test('test3', () => {
    const testObj = new Queue<string>();
    for (let i = 0; i < 100; i += 1) {
        testObj.push(`a${'a'.repeat(i)}`);
        expect(testObj.top()).toEqual(`a`);
        expect(testObj.length()).toEqual(i + 1);
    }

    for (let i = 0; i < 100; i += 1) {
        expect(testObj.pop()).toEqual(`a${'a'.repeat(i)}`);
    }
});
