import Stack from '../../data structures/stack';

test('test1', () => {
    const newStack = new Stack();

    expect(() => newStack.top()).toThrow('empty stack');
    expect(() => newStack.pop()).toThrow('pop from empty stack');
});

test('test2', () => {
    const newStack = new Stack();
    for (let i = 0; i < 150; i += 1) {
        newStack.push(i);
    }

    for (let i = 149; i >= 0; i -= 1) {
        expect(newStack.length()).toEqual(i + 1);
        expect(newStack.top()).toEqual(i);
        expect(newStack.pop()).toEqual(i);
    }
});
