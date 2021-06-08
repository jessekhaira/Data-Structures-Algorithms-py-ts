""" This module contains code for a class that represents the binary
search tree data structure """
from py.data_structures.utils.binaryTree import binaryTreeNode
from typing import Union, Tuple


class BinarySearchTree:
    """ This class represents a binary search tree. This data structure is a
    rooted binary tree where for any given node, all values in the left subtree
    of that node are less than or equal to that nodes value, while all values
    in the right subtree of that node are greater than that nodes value.

    This allows for efficient lookups, insertions, and deletions in the average
    case of O(logN) time. But this data structure does not guarantee
    balancing, meaning that in the worst case, lookups, insertions, and
    deletions will take O(N) time and space.

    Attributes:
        val:
            Integer representing the value at the root of the BST
           
        root:
            Object of type binaryTreeNode representing the node at the root
            of the binary search tree
    """

    def __init__(self, val: int):
        self.root = binaryTreeNode(val)

    def insertion(self, val: int) -> None:
        """ This method inserts a node into the binary search tree, while
        ensuring that the binary search tree property is adhered to.

        Time:
            O(logN) best/average
            O(N) worst

        Space:
            O(logN) best/average
            O(N) worst

        Where N is the number of nodes contained in the tree

        Args:
            val:
                Integer representing the value to be inserted into the tree
        """

        node = self.root
        return self._insertion_helper(val, node)

    def _insertion_helper(self, val: int, node: binaryTreeNode) -> None:
        if not node:
            return binaryTreeNode(val)
        elif val < node.val:
            node.left = self._insertion_helper(val, node.left)
            return node

        elif val >= node.val:
            node.right = self._insertion_helper(val, node.right)
            return node

    def lookup(self, val: int) -> Union[binaryTreeNode, None]:
        """ This method will return the first node that contains the input
        value in the tree, or None if no node contains the value.

        Time:
            O(logN) best/average
            O(N) worst

        Space:
            O(1) best/average/worst

        Where N is the number of nodes in the tree

        Args:
            val:
                Integer representing the node value to look up in the tree

        Returns:
            Binary tree node that contains the given value in the BST
            or None if no node contains the given value
        """
        node = self.root
        return self._lookup_helper(node, val)

    def _lookup_helper(self, node: binaryTreeNode,
                       val: int) -> Union[binaryTreeNode, None]:
        if not node:
            return
        elif node.val == val:
            return node
        elif val <= node.val:
            return self._lookup_helper(node.left, val)
        else:
            return self._lookup_helper(node.right, val)

    def delete(self, val: int) -> None:
        """ This method deletes the first node with the given value inside
        of the binary search tree if it exists.

        Time:
            O(logN) best/average
            O(N) worst

        Space:
            O(logN) best/average
            O(N) worst

        Where N is the number of nodes in the binary search tree

        Args:
            val:
                Integer representing the node value to delete inside of the tree
        """
        node = self.root
        self._delete_helper_v(node, val)

    def _delete_helper_v(self, node: binaryTreeNode, val: int):
        """ This delete helper uses a convenient method to erase
        the node when the node has two children. This node actually
        doesn't erase the node with the target value, this method
        just replaces its value with the minimum value in the nodes
        right subtree.

        If you want to actually remove the node when the node has two
        children, use deleteHelperA.
        """
        if not node:
            return
        elif val < node.val:
            node.left = self._delete_helper_v(node.left, val)
            return node
        elif val > node.val:
            node.right = self._delete_helper_v(node.right, val)
            return node
        else:
            # no left or right child, just delete
            if not node.left and not node.right:
                return
            # no left child, then return the right subtree
            elif not node.left:
                return node.right
            # no right child, then return the left subtree
            elif not node.right:
                return node.left

            # if node has two children, replace this nodes value
            # with the minimum value in the nodes right subtree,
            # and then delete that node
            min_val_in_right_subtree = self._get_min_val_right_v(node.right)
            node.val = min_val_in_right_subtree
            node.right = self._delete_helper_v(node.right,
                                               min_val_in_right_subtree)
            return node

    def _get_min_val_right_v(self, node: binaryTreeNode) -> int:
        # min val has no left child
        if not node.left:
            return node.val
        return self._getMinValRight(node.left)

    def _delete_helper_a(self, node: binaryTreeNode,
                         val: int) -> Union[binaryTreeNode, None]:
        """ This delete helper is the same as the other one, except when
        the node has two children, this method actually removes the node
        from the tree rather than just replacing its value with the minimum
        value in the right subtree.
        """
        if not node:
            return
        elif val < node.val:
            node.left = self._delete_helper_a(node.left, val)
            return node
        elif val > node.val:
            node.right = self._delete_helper_a(node.right, val)
            return node
        else:
            if not node.left and not node.right:
                return
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left

            # have to delete the min val in right subtree while going down
            # so this nodes right subtree has to be changed
            node.right, min_node = self._get_min_node(node.right)
            # we have the min_node, set its left and right subtrees and
            # return up
            min_node.left = node.left
            min_node.right = node.right
            return min_node

    def _get_min_node(
            self,
            node: binaryTreeNode) -> Tuple[binaryTreeNode, binaryTreeNode]:
        if not node.left:
            return node.right, node
        node.left, min_node = self._get_min_node(node.left)
        return node, min_node
