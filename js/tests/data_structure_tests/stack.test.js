import {Stack} from '../../data structures/Stack.js';


test('test1', () => {
    let new_stack = new Stack();
    
    expect(() => new_stack.top()).toThrow('empty stack');
    expect(() => new_stack.pop()).toThrow('pop from empty stack');
})

test('test2', () => {
    let new_stack = new Stack(); 
    for (let i=0; i<150; i++) {
        new_stack.push(i);
    }

    for (let i=149; i>=0; i--) {
        expect(new_stack.length()).toEqual(i+1);
        expect(new_stack.top()).toEqual(i);
        expect(new_stack.pop()).toEqual(i);
    }
})