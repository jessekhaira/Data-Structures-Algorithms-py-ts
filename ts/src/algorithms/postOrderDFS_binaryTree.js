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
function postOrderDFS_recursive(node, output) {
    if (node == null) {
        return;
    }
    postOrderDFS_recursive(node.left, output);
    postOrderDFS_recursive(node.right, output);
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
function postOrderDFS_iterative(node) {
    if (node == null) {
        return; 
    }
    let output =[];
    let stack = [];
    let lastNode = null;
    // empty arrays, objects, sets are truthy statements in javascript not in python so have
    // to explicitly specify the length 
    while (stack.length>0 || node) {
        while (node) {
            stack.push(node);
            node = node.left;
        }
        if (stack[stack.length-1].right && stack[stack.length-1].right !== lastNode) {
            node = stack[stack.length-1].right; 
        }
        else {
            let currNode = stack.pop();
            lastNode = currNode;
            output.push(currNode.val);
        }
    }
    return output; 
}