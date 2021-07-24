from py.utils.binaryTree import binaryTreeNode
from typing import Literal, List


def post_order_dfs_recursive(node: binaryTreeNode,
                             output: Literal[[]]) -> List[int]:
    """ This code describes the recursive post order traversal
    of a binary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.

    Args:
        node:
            Object of type Binary Tree Node

        output:
            List of length zero that will store the output

    Returns:
        A list of integers containing binary trees values in post-order
    """
    if not node:
        return
    post_order_dfs_recursive(node.left, output)
    post_order_dfs_recursive(node.right, output)
    output.append(node.val)
    return output


def post_order_dfs_iterative(node):
    """ This code describes the iterative post order traversal
    of a binary tree. Before any given node in the tree is visited,
    all the nodes in the left subtree of the current node, and all
    the nodes in the right subtree of the current node are visited.

    Args:
        -> node (Binary Tree Node): Binary Tree node that is assumed 
        to have a .left property, .right property, and .val property.
        -> output(list)
    Returns:
        -> list[int] containing binary trees values in post-order
    """
    if not node:
        return
    stack = []
    output = []
    lastNode = None
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        if stack[-1].right and stack[-1].right != lastNode:
            node = stack[-1].right
        else:
            currNode = stack.pop()
            output.append(currNode.val)
            lastNode = currNode
    return output
