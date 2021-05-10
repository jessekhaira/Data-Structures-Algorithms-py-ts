/**
 * This algorithm contains the breadth first search
traversal algorithm used specifically for a binary tree.

For shortest path problems from node i to node j in 
unweighted directed or undirected graphs, BFS is the algorithm 
to use. This algorithm makes use of the queue data structure, 
which is known as a first in first out data structure. 

 * @param {object} node Root of Binary Tree
 * @param {number} node.val Value of current node 
 * @param {object} node.left Left subtree rooted to current node
 * @param {object} node.right Right subtree rooted to current node 
 * @returns {number[][]} 2d list of ints containing trees value level by level
 */
function breadthFirstSearch(node) {
    if (node == null) {
        return [];
    }
    let output = [];
    let queue = [node];
    while (queue.length > 0) {
        let currLevel = [];
        let currLevelLength = queue.length;
        while (currLevelLength !== 0) {
            let node = queue.shift();
            currLevel.push(node.val);
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
            currLevelLength--;
        }
        output.push(currLevel);
    }
    return output;
}

export default breadthFirstSearch;
