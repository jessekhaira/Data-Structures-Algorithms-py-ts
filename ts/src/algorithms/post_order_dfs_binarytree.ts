import { BinaryTreeNode } from '../utils/binary_tree';
/**
 *  This code describes the recursive post order traversal
    of a binary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.
    
 * @param {object} node Root of Binary Tree
 * @param {number} node.val Value of current node 
 * @param {object} node.left Left subtree rooted to current node
 * @param {object} node.right Right subtree rooted to current node 
 * @param {number[]} output Array of values 
 * @returns {number[]} Output values in binary tree in post order 
 */
function postOrderDFSRecursive(
    node: BinaryTreeNode | null,
    output: number[],
): number[] | undefined {
    if (node == null) {
        return;
    }
    postOrderDFSRecursive(node.left, output);
    postOrderDFSRecursive(node.right, output);
    output.push(node.val);
    return output;
}

/**
 *  This code describes the iterative post order traversal
    of a binary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.

 * @param {object} node Root of Binary Tree
 * @param {number} node.val Value of current node 
 * @param {object} node.left Left subtree rooted to current node
 * @param {object} node.right Right subtree rooted to current node 
 * @returns {number[]} Output values in binary tree in post order 
 */
function postOrderDFSIterative(node: BinaryTreeNode): number[] {
    const output: number[] = [];
    const stack: BinaryTreeNode[] = [];
    let lastNode = null;
    // empty arrays, objects, sets are truthy statements in javascript
    // not in python so have to explicitly specify the length
    let mainNode: BinaryTreeNode | null = node;
    while (stack.length > 0 || node) {
        while (mainNode) {
            stack.push(mainNode);
            mainNode = node.left;
        }
        if (
            stack[stack.length - 1].right &&
            stack[stack.length - 1].right !== lastNode
        ) {
            mainNode = stack[stack.length - 1].right;
        } else {
            const currNode = stack.pop();
            lastNode = currNode;
            if (currNode) output.push(currNode.val);
        }
    }
    return output;
}

export { postOrderDFSIterative, postOrderDFSRecursive };
