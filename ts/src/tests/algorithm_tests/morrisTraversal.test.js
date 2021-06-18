import {
    Morris_Inorder_Traversal,
    Morris_PreOrder_Traversal,
} from '../../algorithms/MorrisTraversal';
import { BinaryTreeNode } from '../../data structures/utils/binary_tree';

describe('Test Inorder Morris', () => {
    test('test1', () => {
        const rootBT = new BinaryTreeNode(1);
        rootBT.right = new BinaryTreeNode(2);
        rootBT.right.left = new BinaryTreeNode(3);
        const output = new Set();
        output.add(rootBT.right);
        output.add(rootBT);

        expect(Morris_Inorder_Traversal(rootBT)).toEqual(output);
        expect(Morris_PreOrder_Traversal(rootBT)).toEqual(output);
    });

    test('test2', () => {
        const rootBT = new BinaryTreeNode(1);
        rootBT.right = new BinaryTreeNode(2);
        rootBT.right.left = new BinaryTreeNode(3);

        rootBT.right.right = new BinaryTreeNode(5);

        const output = new Set();
        output.add(rootBT);

        expect(Morris_Inorder_Traversal(rootBT)).toEqual(output);
        expect(Morris_PreOrder_Traversal(rootBT)).toEqual(output);
    });

    test('test3', () => {
        const rootBT = new BinaryTreeNode(1);
        rootBT.right = new BinaryTreeNode(2);
        rootBT.right.left = new BinaryTreeNode(3);
        rootBT.right.right = new BinaryTreeNode(5);
        rootBT.left = new BinaryTreeNode(9);

        const output = new Set();
        expect(Morris_Inorder_Traversal(rootBT)).toEqual(output);
        expect(Morris_PreOrder_Traversal(rootBT)).toEqual(output);
    });

    test('test4', () => {
        const rootBT = new BinaryTreeNode(1);
        rootBT.right = new BinaryTreeNode(2);
        rootBT.right.left = new BinaryTreeNode(3);
        rootBT.right.right = new BinaryTreeNode(5);
        rootBT.left = new BinaryTreeNode(9);
        rootBT.left.left = new BinaryTreeNode(6);
        rootBT.left.left.right = new BinaryTreeNode(10);

        const output = new Set();
        output.add(rootBT.left);
        output.add(rootBT.left.left);

        expect(Morris_Inorder_Traversal(rootBT)).toEqual(output);
        expect(Morris_PreOrder_Traversal(rootBT)).toEqual(output);
    });
});
