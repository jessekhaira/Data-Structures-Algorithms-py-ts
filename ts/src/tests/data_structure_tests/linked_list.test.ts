import DoubleLinkedList from '../../data structures/linked_list';

test('test1', () => {
    const linkedList = new DoubleLinkedList<number>(5);
    linkedList.addAtHead(9);
    linkedList.addAtHead(10);

    expect(linkedList.get(0)).toStrictEqual(10);
    expect(linkedList.get(2)).toStrictEqual(5);
    expect(linkedList.get(3)).toStrictEqual(-1);
});

test('test 2', () => {
    const linkedList = new DoubleLinkedList<number>(5);
    linkedList.addAtTail(9);
    linkedList.addAtTail(10);
    linkedList.addAtTail(123);

    expect(linkedList.get(0)).toStrictEqual(5);
    expect(linkedList.get(1)).toStrictEqual(9);
    expect(linkedList.get(2)).toStrictEqual(10);
    expect(linkedList.get(3)).toStrictEqual(123);
    expect(linkedList.get(4)).toStrictEqual(-1);
});

test('test 3', () => {
    const linkedList = new DoubleLinkedList<number>(5);

    linkedList.addAtIndex(1, 9);
    linkedList.addAtIndex(2, 90);
    linkedList.addAtIndex(0, -10);
    linkedList.addAtHead(21);
    linkedList.addAtTail(9);

    expect(linkedList.get(0)).toStrictEqual(21);
    expect(linkedList.get(1)).toStrictEqual(-10);
    expect(linkedList.get(2)).toStrictEqual(5);
    expect(linkedList.get(3)).toStrictEqual(9);
    expect(linkedList.get(4)).toStrictEqual(90);
});

test('test 4', () => {
    const linkedList = new DoubleLinkedList<number>(5);
    linkedList.addAtIndex(1, 9);
    linkedList.addAtIndex(2, 90);
    linkedList.addAtIndex(0, -10);
    linkedList.addAtHead(21);
    linkedList.addAtTail(9);
    linkedList.addAtIndex(4, 25);
    linkedList.addAtIndex(2, 32);

    expect(linkedList.get(0)).toStrictEqual(21);
    expect(linkedList.get(2)).toStrictEqual(32);
    linkedList.deleteAtIndex(2);

    expect(linkedList.get(2)).toStrictEqual(5);
    linkedList.deleteAtIndex(0);
    if (linkedList.head) {
        expect(linkedList.head.val).toStrictEqual(-10);
    }
});
