""" This module contains code representing the post order depth
first search algorithm for a nary tree"""
from py.utils.binary_tree import binaryTreeNode
from typing import List


def post_order_dfs_nary_recursive(node: binaryTreeNode) -> List[int]:
    """ This algorithm traverses an N-Ary tree in
    post-order fashion recursively.
    """
    if not node:
        return
    output = []
    post_order_nary_helper_recursive(node, output)
    return output


def post_order_nary_helper_recursive(node, output):
    if not node:
        return
    for child in node.children:
        post_order_nary_helper_recursive(child, output)
    output.append(node.val)


def postorder_iterative(node: binaryTreeNode) -> List[int]:
    """ This algorithm traverses an N-Ary tree in post-order fashion
    iteratively.

    Key thing: emulate the recursive call stack using an actual stack. How we
    convert recursive code to iterative code.
    """
    if not node:
        return
    stack = [(node, 0)]
    output = []
    while stack:
        node, curr_idx_child = stack.pop()
        if curr_idx_child == len(node.children):
            output.append(node.val)
        else:
            stack.append((node, curr_idx_child + 1))
            stack.append((node.children[curr_idx_child], 0))

    return output
