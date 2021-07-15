import { floydsTortoiseHareAlgo } from '../../algorithms/floyds_tortoise_hare';
import { SingleLinkedListNode } from '../../utils/linked_list_utility';

test('test edge case -- no input', () => {
    expect(floydsTortoiseHareAlgo()).toEqual(null);
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

test('test linked list with a cycle 1', () => {
    const node = new SingleLinkedListNode(2);
    node.next = new SingleLinkedListNode(5);
    node.next.next = new SingleLinkedListNode(9);
    node.next.next.next = new SingleLinkedListNode(12);
    node.next.next.next.next = node;

    expect(floydsTortoiseHareAlgo(node)).toEqual(node);
});

test('test linked list with a cycle 2', () => {
    const node = new SingleLinkedListNode(2);
    node.next = new SingleLinkedListNode(5);
    node.next.next = new SingleLinkedListNode(9);
    node.next.next.next = new SingleLinkedListNode(12);
    node.next.next.next.next = new SingleLinkedListNode(5);
    node.next.next.next.next.next = node.next.next.next.next;
    expect(floydsTortoiseHareAlgo(node)).toEqual(node.next.next.next.next);
});
