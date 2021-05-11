import { BinaryTreeNode } from '../data structures/utils/BinaryTree';
/**
 * This algorithm contains the breadth first search
traversal algorithm used specifically for a binary tree.

For shortest path problems from node i to node j in 
unweighted directed or undirected graphs, BFS is the algorithm 
to use. This algorithm makes use of the queue data structure, 
which is known as a first in first out data structure. 

 * @param {BinaryTreeNode} node Root of Binary Tree
 * @param {number} node.val Value of current node 
 * @param {BinaryTreeNode} node.left Left subtree rooted to current node
 * @param {BinaryTreeNode} node.right Right subtree rooted to current node 
 * @returns {number[][]} 2d list of ints containing trees value level by level
 */
function breadthFirstSearch(node: BinaryTreeNode): number[][] {
    if (node == null) {
        return [];
    }
    const output: number[][] = [];
    const queue: BinaryTreeNode[] = [node];
    while (queue.length > 0) {
        const currLevel: number[] = [];
        let currLevelLength = queue.length;
        while (currLevelLength !== 0) {
            const currNode = queue.shift() as BinaryTreeNode;
            currLevel.push(currNode.val);
            if (currNode.left) {
                queue.push(currNode.left);
            }
            if (currNode.right) {
                queue.push(currNode.right);
            }
            currLevelLength -= 1;
        }
        output.push(currLevel);
    }
    return output;
}

export default breadthFirstSearch;
