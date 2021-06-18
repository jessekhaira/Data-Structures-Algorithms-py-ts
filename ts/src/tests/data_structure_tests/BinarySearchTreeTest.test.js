import { BinarySearchTree } from '../../data structures/binary_search_tree';

describe('Tests testing binary search tree', () => {
    test('testing bst insertion method', () => {
        const bst = new BinarySearchTree(4);
        const vals = [1, 2, 3, 4, 5, 6, 7, 8];
        for (const val of vals) {
            bst.insert(val);
        }
        expect(validateBST(bst)).toEqual(true);
    });

    test('testing bst lookup method', () => {
        const bst = new BinarySearchTree(4);
        const vals = [1, 2, 3, 4, 5, 6, 7, 8];
        for (const val of vals) {
            bst.insert(val);
        }

        for (const val of vals) {
            expect(bst.lookup(val).val).toEqual(val);
        }
    });

    test('testing bst delete method', () => {
        const bst = new BinarySearchTree(4);
        const vals = [1, 2, 3, 4, 5, 6, 7, 8];

        for (const val of vals) {
            bst.insert(val);
        }

        for (const val of vals) {
            expect(bst.lookup(val).val).toEqual(val);
            bst.delete(val);
            if (val !== 4) {
                expect(bst.lookup(val)).toEqual(null);
            } else {
                expect(bst.lookup(val).val).toEqual(4);
            }
        }
    });
});

function validateBST(bst) {
    return validateBSTHelper(
        bst.root,
        Number.NEGATIVE_INFINITY,
        Number.POSITIVE_INFINITY,
    );
}

function validateBSTHelper(node, lowBound, highBound) {
    if (!node) {
        return true;
    }
    if (!(node.val >= lowBound && node.val < highBound)) {
        return false;
    }
    const validSubtreeLeft = validateBSTHelper(node.left, lowBound, node.val);
    const validSubtreeRight = validateBSTHelper(
        node.right,
        node.val,
        highBound,
    );
    return validSubtreeLeft && validSubtreeRight;
}
