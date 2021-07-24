""" This module holds unit tests for the post order depth first
search algorithm """
from py.data_structures.binary_search_tree import BinarySearchTree
from py.algorithms.post_order_dfs_binary_tree import post_order_dfs_iterative, post_order_dfs_recursive
import unittest


class PostOrderDFSBinary(unittest.TestCase):
    """ This class contains tests for the post order depth
    first search algorithm """

    def test1(self):
        bst = BinarySearchTree(5)
        ints = [3, 5, 1, 2, -5, -9]
        for val in ints:
            bst.insertion(val)

        self.assertEqual(post_order_dfs_iterative(bst.root),
                         [-9, -5, 2, 1, 3, 5, 5])

    def test2(self):
        bst = BinarySearchTree(5)
        ints = [3, 5, 1, 2, -5, -9]
        for val in ints:
            bst.insertion(val)

        self.assertEqual(post_order_dfs_recursive(bst.root, []),
                         [-9, -5, 2, 1, 3, 5, 5])

    def test3(self):
        bst = BinarySearchTree(5)
        ints = []
        for val in ints:
            bst.insertion(val)

        self.assertEqual(post_order_dfs_iterative(bst.root), [5])

    def test4(self):
        bst = BinarySearchTree(5)
        ints = []
        for val in ints:
            bst.insertion(val)

        self.assertEqual(post_order_dfs_recursive(bst.root, []), [5])


if __name__ == "__main__":
    unittest.main()
