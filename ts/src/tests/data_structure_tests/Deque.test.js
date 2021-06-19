import { Deque } from '../../data structures/Deque.js';

test('test 1', () => {
    const obj1 = new Deque();
    expect(obj1.popFirst).toThrow();
    expect(obj1.popLast).toThrow();
    expect(obj1.peekFirst).toThrow();
    expect(obj1.peekLast).toThrow();
});

test('test 2', () => {
    const obj2 = new Deque();
    for (let i = 0; i < 150; i++) {
        obj2.addLast(i);
    }

    let countPopped = 0;
    for (let i = 149; i >= 0; i--) {
        expect(obj2.length()).toEqual(150 - countPopped);
        expect(obj2.peekLast()).toEqual(150 - countPopped - 1);
        expect(obj2.popLast()).toEqual(i);
        countPopped++;
    }
});

test('test 3', () => {
    const obj2 = new Deque();
    for (let i = 0; i < 150; i++) {
        obj2.addFirst(i);
    }

    for (let i = 149; i >= 0; i--) {
        expect(obj2.peekFirst()).toEqual(i);
        expect(obj2.popFirst()).toEqual(i);
    }
});
