""" This module contains code representing the morris traversal
algorithm """
from py.utils.binaryTree import binaryTreeNode
from typing import Set, Any


def morris_inorder_traversal(node: binaryTreeNode) -> Set[Any]:
    """ This algorithm represents a way to traverse binary
    trees in-order using just O(1) space with the Morris
    Traversal algorithm.

    In in-order traversal, all the nodes in a given nodes left
    subtree are visited, then the current node is visited,
    then all the nodes in the right subtree of a given
    node are visited.

    In this case, the algorithm is being used to find the number
    of nodes in the binary tree with just one child.

    Time:
        O(N) best/average/worst

    Space:
        O(1) best/average/worst

    Where N is the number of nodes in the binary tree

    Args:
        node:
            Binary tree node representing the root of the binary
            tree
    Returns:
        A hashset containing all nodes in the tree with one child
    """
    if not node:
        return
    output = set()
    while node:
        # inorder traversal easy case - no left subtree means we just visit
        # this node right away
        if not node.left:
            # don't want to add leaf nodes. also have to account for fact some
            # leaf nodes will have artifical right node
            # unless we use an addition data structure to track those,
            # we will just add and remove them from the hash-set, which
            # are efficient operations
            if node.right:
                output.add(node)
            node = node.right
        # if there is a left subtree, then we need some way to get back to
        # this node after visiting every node in the left subtree. So we
        # get the absolute last node that will be visited in the left
        # subtree and set its right pointer to the current node
        else:
            last_node_in_left_subtree = get_prev_node(node)
            if not last_node_in_left_subtree.right:
                last_node_in_left_subtree.right = node
                node = node.left
            elif last_node_in_left_subtree.right == node:
                last_node_in_left_subtree.right = None
                # if the node has a left subtree, its guaranteed at this point
                # to not have a right subtree so we can add it
                if last_node_in_left_subtree.left:
                    output.add(last_node_in_left_subtree)
                # otherwise, this connecting node was a leaf node and will be
                # present in output so we have to remove it
                else:
                    output.remove(last_node_in_left_subtree)
                if not node.right:
                    output.add(node)
                node = node.right
    return output


def get_prev_node(node: binaryTreeNode) -> binaryTreeNode:
    node_l = node.left
    while node_l.right and node_l.right != node:
        node_l = node_l.right
    return node_l


def morris_pre_order_traversal(node: binaryTreeNode) -> Set[Any]:
    """ This algorithm represents a way to traverse binary
    trees in pre-order manner using just O(1) space with
    the Morris Traversal algorithm.

    In pre-order traversal, the node is visited first, then
    its left subtree, then its right subtree.

    In this case, the algorithm is being used to find the number
    of nodes in the binary tree with just one child.

    Time:
        O(N) best/average/worst

    Space:
        O(1) best/average/worst

    Where N is the number of nodes in the tree

    Args:
        node:
            Binary tree node representing the root of the binary
            tree
    Returns:
        A hashset containing all nodes in the tree with one child
    """
    output = set()
    while node:
        if node.left:
            prev_node = get_prev_node(node)
            if not prev_node.right:
                prev_node.right = node
                if not node.right:
                    output.add(node)
                node = node.left
            else:
                prev_node.right = None
                if prev_node.left:
                    output.add(prev_node)
                else:
                    output.remove(prev_node)
                node = node.right
        else:
            if node.right:
                output.add(node)
            node = node.right
    return output
