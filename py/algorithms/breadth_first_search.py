from py.data_structures.Queue import Queue

def breadth_first_search(node):
    """ This algorithm represents the breadth first search traversal algorithm
    used specifically for a binary tree.

    For shortest path problems from node i to node j in unweighted directed or
    undirected graphs, BFS is the algorithm to use. This algorithm makes use of
    the queue data structure, which is known as a first in first out data
    structure.

    Args:
        node (Binary Tree Root):
            Root of binary tree to traverse

    Returns:
        A list(list[int]) of binary tree levels
    """
    queue = Queue()
    queue.push(node)
    output = []
    while queue:
        curr_level = []
        curr_length = len(queue)
        while curr_length > 0:
            node = queue.poll()
            curr_level.append(node.val)
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            curr_length -= 1
        output.append(curr_level)
    return output
