from py.data_structures.Queue import Queue
def breadthFirstSearch(node):
    """
    This algorithm represents the breadth first search traversal algorithm used specifically for a 
    binary tree.

    For shortest path problems from node i to node j in unweighted directed or undirected graphs, BFS 
    is the algorithm to use. This algorithm makes use of the queue data structure, which is known as a 
    first in first out data structure. 

    Input:
        - node (Binary Tree Root): Root of binary tree to traverse, with properties
        .val to represent the value held at this node, .left to represent the left subtree
        attached to this node, .right to represent the right subtree attached to this node 
    
    Output:
        A list(list[int]) of binary tree levels
    """
    queue = Queue() 
    queue.push(node) 
    output = []
    while queue:
        currLevel = []
        currLength = len(queue)
        for i in range(currLength):
            node = queue.poll()
            currLevel.append(node.val)
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
        output.append(currLevel)
    return output 



