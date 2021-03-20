import {floydsTortoiseHareAlgo} from '../../algorithms/FloydsTortoiseHareAlgo.js';
import {SingleLinkedListNode} from '../../data structures/utils/LinkedList';

test('test edge case -- no input', () => {
    expect(floydsTortoiseHareAlgo()).toEqual(null)
});

test('test edge case -- single node passed in', () => {
    const node = new SingleLinkedListNode(5);
    expect(floydsTortoiseHareAlgo(node)).toEqual(null); 
});

test('test linked list with no cycle', () => {
    const node = new SingleLinkedListNode(2);
    node.next = new SingleLinkedListNode(5);
    node.next.next = new SingleLinkedListNode(9);
    node.next.next.next = new SingleLinkedListNode(12);
    expect(floydsTortoiseHareAlgo(node)).toEqual(null); 
});

test('test linked list with a cycle', () => {
    const node = new SingleLinkedListNode(2);
    node.next = new SingleLinkedListNode(5);
    node.next.next = new SingleLinkedListNode(9);
    node.next.next.next = new SingleLinkedListNode(12);
    node.next.next.next.next = node;

    expect(floydsTortoiseHareAlgo(node)).toEqual(node);
})