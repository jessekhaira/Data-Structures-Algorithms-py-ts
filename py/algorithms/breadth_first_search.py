""" This module contains the breadth first search algorithm """
from py.data_structures.queue import Queue
from py.data_structures.utils.binaryTree import binaryTreeNode
from typing import List


def breadth_first_search(node: binaryTreeNode) -> List[List[int]]:
    """ This algorithm represents the breadth first search traversal algorithm
    used specifically for a binary tree.

    For shortest path problems from node i to node j in unweighted directed or
    undirected graphs, BFS is the algorithm to use. This algorithm makes use of
    the queue data structure, which is known as a first in first out data
    structure.

    Args:
        node:
            Root of binary tree to traverse

    Returns:
        A 2D list, where list[i] represents a list containing integers for all
        the nodes contained on the i-th level of the input binary tree
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
