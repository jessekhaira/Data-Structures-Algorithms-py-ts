import {
    recursiveQuickSelect,
    iterativeQuickSelect,
} from '../../algorithms/quick_select';

describe('recursive quick select tests', () => {
    test('test 1', () => {
        const obj1 = [20, 4, 5, -9, -120];
        expect(recursiveQuickSelect(obj1, 0)).toEqual(-120);
    });

    test('test 2', () => {
        const obj1 = [-9, 4, 5, 9, 10, 10, 20, 5, 8, -30, -90];
        expect(recursiveQuickSelect(obj1, 5)).toEqual(5);
    });

    test('test 3', () => {
        const obj1 = [-2, -9, -12, 3, 2, 1];
        expect(recursiveQuickSelect(obj1, 0)).toEqual(-12);
    });

    test('test 4', () => {
        const obj1 = [-2, -9, -12, 3, 2, 1];
        expect(recursiveQuickSelect(obj1, 5)).toEqual(3);
    });

    test('test 5', () => {
        const obj1 = [-2, -9, -12, 3, 2, 1];
        expect(recursiveQuickSelect(obj1, 3)).toEqual(1);
    });

    test('test 6', () => {
        const obj1 = [-2, -9, -12, 3, 2, 1];
        expect(recursiveQuickSelect(obj1, 221)).toEqual(null);
    });
});

describe('iterative quick select tests', () => {
    test('test 1', () => {
        const obj1 = [20, 4, 5, -9, -120];
        expect(iterativeQuickSelect(obj1, 0)).toEqual(-120);
    });

    test('test 2', () => {
        const obj1 = [-9, 4, 5, 9, 10, 10, 20, 5, 8, -30, -90];
        expect(iterativeQuickSelect(obj1, 5)).toEqual(5);
    });

    test('test 3', () => {
        const obj1 = [-2, -9, -12, 3, 2, 1];
        expect(iterativeQuickSelect(obj1, 0)).toEqual(-12);
    });

    test('test 4', () => {
        const obj1 = [-2, -9, -12, 3, 2, 1];
        expect(iterativeQuickSelect(obj1, 5)).toEqual(3);
    });

    test('test 5', () => {
        const obj1 = [-2, -9, -12, 3, 2, 1];
        expect(iterativeQuickSelect(obj1, 3)).toEqual(1);
    });

    test('test 6', () => {
        const obj1 = [-2, -9, -12, 3, 2, 1];
        expect(iterativeQuickSelect(obj1, 221)).toEqual(null);
    });
});
