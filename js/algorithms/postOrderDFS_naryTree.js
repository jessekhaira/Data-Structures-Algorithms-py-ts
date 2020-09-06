
/**
 *  This code describes the recursive post order traversal
    of a n-ary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.

 * @param {object} node Root of Nary Tree
 * @param {number} node.val Value of current node 
 * @param {object[]} node.children Array of children that are rooted to current node
 * @returns {number[]} Output values of n-ary tree in post order 
 */
function postorder_recursive(node) {
    if (node == null) {
        return []; 
    }
    let output = [];
    postOrder_helperRecursive(node, output);
    return output; 
}

function postOrder_helperRecursive(node, output) {
    if (node == null) {
        return; 
    }
    for (let child of node.children) {
        postOrder_helperRecursive(child, output);
    }
    output.push(node.val);
}


/**
 *  This code describes the iterative post order traversal
    of a n-ary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.

 * @param {object} node Root of Nary Tree
 * @param {number} node.val Value of current node 
 * @param {object[]} node.children Array of children that are rooted to current node
 * @returns {number[]} Output values in binary tree in post order 
 */
function postorder_iterative(node) {
    if (node == null) {
       return []; 
    }
    let stack = [[node,0]];
    let output = [];
    while (stack.length >0) {
        let [node, idx] = stack.pop();
        if (idx === node.children.length) {
            output.push(node.val);
        }
        else {
            stack.push([node, idx+1]);
            stack.push([node.children[idx], 0]);
        }
    }
    return output; 
} 