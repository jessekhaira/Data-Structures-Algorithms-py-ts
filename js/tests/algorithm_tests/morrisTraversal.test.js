import {Morris_Inorder_Traversal, Morris_PreOrder_Traversal} from "../../algorithms/MorrisTraversal"
import {BinaryTreeNode} from "../../data structures/utils/BinaryTree";


describe('Test Inorder Morris', () => {
    test('test1', () => {
        let rootBT = new BinaryTreeNode(1);
        rootBT.right = new BinaryTreeNode(2);
        rootBT.right.left = new BinaryTreeNode(3);
        let output = new Set(); 
        output.add(rootBT.right);
        output.add(rootBT);

        expect(Morris_Inorder_Traversal(rootBT)).toEqual(output); 
        expect(Morris_PreOrder_Traversal(rootBT)).toEqual(output); 

    });

    test('test2', () => {
        let rootBT = new BinaryTreeNode(1)
        rootBT.right = new BinaryTreeNode(2)
        rootBT.right.left = new BinaryTreeNode(3)

        rootBT.right.right = new BinaryTreeNode(5)

        let output = new Set()
        output.add(rootBT);

        expect(Morris_Inorder_Traversal(rootBT)).toEqual(output); 
        expect(Morris_PreOrder_Traversal(rootBT)).toEqual(output); 

    })

    test('test3', () => {
        let rootBT = new BinaryTreeNode(1)
        rootBT.right = new BinaryTreeNode(2)
        rootBT.right.left = new BinaryTreeNode(3)
        rootBT.right.right = new BinaryTreeNode(5)
        rootBT.left = new BinaryTreeNode(9) 

        let output = new Set();
        expect(Morris_Inorder_Traversal(rootBT)).toEqual(output); 
        expect(Morris_PreOrder_Traversal(rootBT)).toEqual(output); 

    })

    test('test4', () => {
        let rootBT = new BinaryTreeNode(1)
        rootBT.right =new BinaryTreeNode(2)
        rootBT.right.left = new BinaryTreeNode(3)
        rootBT.right.right =new BinaryTreeNode(5)
        rootBT.left = new BinaryTreeNode(9) 
        rootBT.left.left =new BinaryTreeNode(6)
        rootBT.left.left.right =new BinaryTreeNode(10)

        let output = new Set()
        output.add(rootBT.left);
        output.add(rootBT.left.left);

        expect(Morris_Inorder_Traversal(rootBT)).toEqual(output); 
        expect(Morris_PreOrder_Traversal(rootBT)).toEqual(output); 

    })
})