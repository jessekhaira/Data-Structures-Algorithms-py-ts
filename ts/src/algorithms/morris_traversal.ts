import { BinaryTreeNode } from 'src/utils/binary_tree';
/**
 *  This algorithm represents a way to traverse binary trees in-order using just
    O(1) space with the Morris Traversal algorithm.
    
    In in-order traversal, all the nodes in a given nodes left subtree are
    visited, then the current node is visited, then all the nodes in the
    right subtree of a given node are visited.

    In this case, the algorithm is being used to find the number of nodes
    in the binary tree with just one child. 

    Time b/a/w: O(n) where n is the number of nodes in the tree
    Space b/a/w: O(1)
 * @param {BinaryTreeNode} node 
 * @returns {Set} Set containing all nodes with one child 
 */
function morrisInorderTraversal(node) {
    if (node == null) {
        return [];
    }
    const output = new Set();
    while (node) {
        if (!node.left) {
            if (node.right) {
                output.add(node);
            }
            node = node.right;
        } else {
            const prevNode = getPrevNode(node);
            if (!prevNode.right) {
                prevNode.right = node;
                node = node.left;
            } else {
                prevNode.right = null;
                if (prevNode.left) {
                    output.add(prevNode);
                } else {
                    output.delete(prevNode);
                }
                if (!node.right) {
                    output.add(node);
                }
                node = node.right;
            }
        }
    }
    return output;
}

function getPrevNode(node) {
    let nodeL = node.left;
    while (nodeL.right && nodeL.right !== node) {
        nodeL = nodeL.right;
    }
    return nodeL;
}

/**
    This algorithm represents a way to traverse binary trees in
    pre-order manner using just O(1) space with the Morris Traversal algorithm.
    
    In pre-order traversal, the node is visited first, then its left subtree,
    then its right subtree. 

    In this case, the algorithm is being used to find the number of nodes in
    the binary tree with just one child. 

    Time b/a/w: O(n) where n is the number of nodes in the tree
    Space b/a/w: O(1)
 * @param {BinaryTreeNode} node 
 * @returns {Set} Set containing all nodes with one child 
 */
function morrisPreorderTraversal(node) {
    if (node == null) {
        return [];
    }
    const output = new Set();
    while (node) {
        if (!node.left) {
            if (node.right) {
                output.add(node);
            }
            node = node.right;
        } else {
            const prevNode = getPrevNode(node);
            if (!prevNode.right) {
                prevNode.right = node;
                if (!node.right) {
                    output.add(node);
                }
                node = node.left;
            } else {
                prevNode.right = null;
                if (prevNode.left) {
                    output.add(prevNode);
                } else {
                    output.delete(prevNode);
                }
                node = node.right;
            }
        }
    }
    return output;
}

export { morrisInorderTraversal, morrisPreorderTraversal };
