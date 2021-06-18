import BinarySearchTree from '../../data structures/binary_search_tree';
import { BinaryTreeNode } from '../../data structures/utils/binary_tree';

function validateBSTHelper(
    node: BinaryTreeNode | null,
    lowBound: number,
    highBound: number,
): boolean {
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

function validateBST(bst: BinarySearchTree): boolean {
    return validateBSTHelper(
        bst.root,
        Number.NEGATIVE_INFINITY,
        Number.POSITIVE_INFINITY,
    );
}
describe('Tests testing binary search tree', () => {
    test('testing bst insertion method', () => {
        const bst = new BinarySearchTree(4);
        const vals = [1, 2, 3, 4, 5, 6, 7, 8];
        vals.forEach((val) => {
            bst.insert(val);
        });
        expect(validateBST(bst)).toEqual(true);
    });

    test('testing bst lookup method', () => {
        const bst = new BinarySearchTree(4);
        const vals = [1, 2, 3, 4, 5, 6, 7, 8];
        vals.forEach((val) => {
            bst.insert(val);
        });

        vals.forEach((val) => {
            const returnNode = bst.lookup(val);
            if (returnNode != null) {
                expect(returnNode.val).toEqual(val);
            }
        });
    });

    test('testing bst delete method', () => {
        const bst = new BinarySearchTree(4);
        const vals = [1, 2, 3, 4, 5, 6, 7, 8];

        vals.forEach((val) => {
            bst.insert(val);
        });

        vals.forEach((val) => {
            const returnNode = bst.lookup(val);
            if (returnNode != null) {
                expect(returnNode.val).toEqual(val);
            }
            bst.delete(val);
            if (val !== 4) {
                expect(bst.lookup(val)).toEqual(null);
            }
            const lookedUpNode = bst.lookup(val);
            if (lookedUpNode != null) {
                expect(lookedUpNode.val).toEqual(4);
            }
        });
    });
});
