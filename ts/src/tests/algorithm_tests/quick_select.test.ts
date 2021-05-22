import { recursiveQuickSelect } from '../../algorithms/quick_select';

describe('recursive quick select tests', () => {
    test('test 1', () => {
        const obj1 = [20, 4, 5, -9, -120];
        expect(recursiveQuickSelect(obj1, 0)).toEqual(-120);
    });

    test('test 2', () => {
        const obj1 = [-9, 4, 5, 9, 10, 10, 20, 5, 8, -30, -90];
        expect(recursiveQuickSelect(obj1, 5)).toEqual(5);
    });
});
