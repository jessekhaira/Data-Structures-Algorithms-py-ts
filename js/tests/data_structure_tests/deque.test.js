import {Deque} from "../../data structures/Deque.js";

test('test 1', () => {
    const obj1 = new Deque();
    expect(obj1.popFirst).toThrow();
    expect(obj1.popLast).toThrow();
    expect(obj1.peekFirst).toThrow();
    expect(obj1.peekLast).toThrow();
})