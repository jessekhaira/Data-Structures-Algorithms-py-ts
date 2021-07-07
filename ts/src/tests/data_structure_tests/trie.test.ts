import Trie from '../../data structures/trie';

test('test1', () => {
    const obj1 = new Trie();
    obj1.insert('Cat');
    obj1.insert('cat');

    expect(obj1.lookup('Cat')).toEqual(true);
    expect(obj1.lookup('cat')).toEqual(true);

    expect(obj1.lookup('ca')).toEqual(false);
    expect(obj1.lookup('c')).toEqual(false);

    expect(obj1.startsWith('C')).toEqual(true);
    expect(obj1.startsWith('ca')).toEqual(true);
});

test('test2', () => {
    const obj1 = new Trie();
    obj1.insert('cat');
    obj1.insert('call');

    obj1.delete('cat');

    expect(obj1.lookup('cat')).toEqual(false);
    expect(obj1.lookup('call')).toEqual(true);

    obj1.insert('back');
    obj1.insert('backly');
    obj1.insert('backl');
    obj1.delete('backl');

    expect(obj1.lookup('backl')).toEqual(false);
    expect(obj1.lookup('back')).toEqual(true);
    expect(obj1.lookup('backly')).toEqual(true);
});
