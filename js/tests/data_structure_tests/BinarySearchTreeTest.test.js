import {BinarySearchTree} from '../../data structures/BinarySearchTree';

describe('Tests testing binary search tree', () => {
    test('testing bst insertion method', () => {
        const bst = new BinarySearchTree(4);
        const vals = [1, 2, 3, 5, 6 ,7, 8];
        for (const val of vals) {
            bst.insert(val);
        }
        expect(validateBST(bst)).toEqual(true); 
    });

})

function validateBST(bst) {
    return validateBSTHelper(bst.root, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY); 
}

function validateBSTHelper(node, lowBound, highBound) {
    if (!node) {
        return true; 
    }
    if (!(node.val >= lowBound && node.val < highBound)) {
        return false;
    }
    const validSubtreeLeft = validateBSTHelper(node.left, lowBound, node.val);
    const validSubtreeRight = validateBSTHelper(node.right, node.val, highBound); 
    return validSubtreeLeft && validSubtreeRight; 
}