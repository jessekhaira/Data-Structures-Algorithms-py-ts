import { NaryTreeNode } from 'src/utils/binary_tree';

function postOrderHelperRecursive<T>(node: NaryTreeNode<T>, output: T[]): void {
    node.children.forEach((child) => {
        postOrderHelperRecursive(child, output);
    });
    output.push(node.val);
}

/**
 *  This code describes the recursive post order traversal
    of a n-ary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.

 * @param {NaryTreeNode} node Root of Nary Tree
 * @returns {number[]} Output values of n-ary tree in post order 
 */
function postOrderRecursive<T>(node: NaryTreeNode<T>): T[] {
    const output: T[] = [];
    postOrderHelperRecursive<T>(node, output);
    return output;
}

/**
 *  This code describes the iterative post order traversal
    of a n-ary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.

 * @param {NaryTreeNode} node Root of Nary Tree
 * @returns {number[]} Output values in binary tree in post order 
 */
function postOrderIterative<T>(node: NaryTreeNode<T>): T[] {
    const stack = [[node, 0]];
    const output: T[] = [];
    while (stack.length > 0) {
        const [currNode, idx] = stack.pop() as [NaryTreeNode<T>, number];
        if (idx === currNode.children.length) {
            output.push(currNode.val);
        } else {
            stack.push([currNode, idx + 1]);
            stack.push([currNode.children[idx], 0]);
        }
    }
    return output;
}

export { postOrderRecursive, postOrderIterative };
