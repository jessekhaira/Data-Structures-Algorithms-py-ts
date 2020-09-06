function breadthFirstSearch(node) {
    /*
    This algorithm contains the breadth first search
    traversal algorithm used specifically for a binary tree.

    For shortest path problems from node i to node j in 
    unweighted directed or undirected graphs, BFS is the algorithm 
    to use. This algorithm makes use of the queue data structure, 
    which is known as a first in first out data structure. 

    Input:
        -> node (Binary Tree Root): 
    Output:
        -> list[list[int]] of binary tree levels
    */

    if (node == null) {
        return [];
    }
    let output = [];
    let queue = [node];
    while (queue.length >0) {
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