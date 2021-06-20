import HashMap from '../../data structures/hash_map';

test('test 1', () => {
    const obj1 = new HashMap<number>();
    obj1.put(5, 12);
    obj1.put(15, 23);
    obj1.put(25, 93);
    expect(obj1.get(5)).toStrictEqual(12);
    expect(obj1.get(15)).toStrictEqual(23);
    expect(obj1.get(25)).toStrictEqual(93);
});

test('test 2', () => {
    const obj1 = new HashMap<number>();
    obj1.put(5, 12);
    obj1.put(15, 23);
    obj1.put(25, 93);
    obj1.put(5, 123);
    obj1.remove(15);
    obj1.put(25, 1231);
    expect(obj1.get(5)).toStrictEqual(123);
    expect(obj1.get(15)).toStrictEqual(null);
    expect(obj1.get(25)).toStrictEqual(1231);
    expect(obj1.get(-1)).toStrictEqual(null);
});
