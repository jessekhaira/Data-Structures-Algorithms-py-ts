import HashSet from '../../data structures/hash_set';

test('test1', () => {
    const obj1 = new HashSet();
    obj1.add(5);
    obj1.add(9);
    obj1.add(5);

    expect(obj1.contains(5)).toStrictEqual(true);
    expect(obj1.contains(9)).toStrictEqual(true);
    expect(obj1.contains(12)).toStrictEqual(false);
});

test('test 2', () => {
    const obj2 = new HashSet();
    obj2.add(0);
    obj2.add(-123);
    obj2.add(-123);
    obj2.add(1231);
    obj2.add(14123);

    expect(obj2.contains(14123)).toStrictEqual(true);
    obj2.remove(14123);

    expect(obj2.contains(14123)).toStrictEqual(false);

    obj2.remove(-123);
    expect(obj2.contains(-123)).toStrictEqual(false);
});

test('test 3', () => {
    const obj2 = new HashSet();
    for (let i = 0; i < 1000; i++) {
        obj2.add(0);
    }

    expect(obj2._curr_items_hashed).toStrictEqual(1);
});
