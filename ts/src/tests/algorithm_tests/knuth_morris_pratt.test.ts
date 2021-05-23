import knuthMorrisPratt from '../../algorithms/knuth_morris_pratt';

test('test1', () => {
    const bigstr = '';
    const substr = 'xp';

    expect(knuthMorrisPratt(bigstr, substr)).toBe(-1);
});

test('test2', () => {
    const bigstr = 'xp';
    const substr = '';

    expect(knuthMorrisPratt(bigstr, substr)).toBe(-1);
});

test('test3', () => {
    const bigstr = 'loepanajsdnqjkweqwhekjdhfasdkjlashdlasjdjksaasdjias';
    const substr = 'weqwhek';

    expect(knuthMorrisPratt(bigstr, substr)).toBe(14);
});

test('test4', () => {
    const bigstr = 'bizxcnjasd';
    const substr = 'sd';

    expect(knuthMorrisPratt(bigstr, substr)).toBe(8);
});

test('test5', () => {
    const bigstr = 'sd';
    const substr = 'sd';

    expect(knuthMorrisPratt(bigstr, substr)).toBe(0);
});
