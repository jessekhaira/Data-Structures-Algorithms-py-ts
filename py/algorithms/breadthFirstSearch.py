from collections import deque
def breadthFirstSearch(node):
    """
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

    """
    queue = deque()
    queue.append(node)
    output = []
    while queue:
        currLevel = []
        currLength = len(queue)
        for i in range(currLength):
            node = queue.popleft()
            currLevel.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        output.append(currLevel)
    return output 



