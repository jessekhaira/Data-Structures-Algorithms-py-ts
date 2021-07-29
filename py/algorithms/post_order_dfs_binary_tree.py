""" This module contains code representing the post order depth
first search algorithm for a binary tree"""

from py.utils.binary_tree import binaryTreeNode
from typing import Literal, List


def post_order_dfs_recursive(node: binaryTreeNode,
                             output: Literal[[]]) -> List[int]:
    """ This code describes the recursive post order traversal
    of a binary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.

    Args:
        node:
            Object that represents the root of the binary tree to traverse
            in a postorder manner

        output:
            List of length zero that will store the output

    Returns:
        A list of integers containing the binary trees values in post order
    """
    if not node:
        return
    post_order_dfs_recursive(node.left, output)
    post_order_dfs_recursive(node.right, output)
    output.append(node.val)
    return output


def post_order_dfs_iterative(node: binaryTreeNode) -> List[int]:
    """ This code describes the iterative post order traversal
    of a binary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.

    Args:
        node:
            Object that represents the root of the binary tree to traverse in
            a postorder manner

    Returns:
        List of integers containing the binary trees values in post order
    """
    if not node:
        return
    stack = []
    output = []
    last_node = None
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        if stack[-1].right and stack[-1].right != last_node:
            node = stack[-1].right
        else:
            curr_node = stack.pop()
            output.append(curr_node.val)
            last_node = curr_node
    return output
