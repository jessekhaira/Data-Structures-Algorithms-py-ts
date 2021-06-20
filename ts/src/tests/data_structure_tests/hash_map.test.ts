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

test('test 3', () => {
    const obj1 = new HashMap<string>();
    for (let i = 0; i < 6000; i += 1) {
        obj1.put(i, `a${i}`);
        expect(obj1.get(i)).toStrictEqual(`a${i}`);
    }
    expect(obj1.get(5)).toStrictEqual('a5');
    expect(obj1.get(15)).toStrictEqual('a15');
    expect(obj1.get(25)).toStrictEqual('a25');
    expect(obj1.get(-1)).toStrictEqual(null);

    for (let i = 250; i < 500; i += 1) {
        obj1.remove(i);
        expect(obj1.get(i)).toStrictEqual(null);
    }
});
