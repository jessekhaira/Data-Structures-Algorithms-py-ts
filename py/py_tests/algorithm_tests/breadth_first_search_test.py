""" This module holds unit tests for the breadth first search algorithm """
from py.data_structures.BinarySearchTree import BinarySearchTree
import unittest
from py.algorithms.breadth_first_search import breadth_first_search


class BreadthFirstSearchTests(unittest.TestCase):

    def test1(self):
        bst = BinarySearchTree(5)
        ints = [3, 5, 1, 2, -5, -9]
        for val in ints:
            bst.insertion(val)
        self.assertEqual(breadth_first_search(bst.root),
                         [[5], [3, 5], [1], [-5, 2], [-9]])


if __name__ == "__main__":
    unittest.main()
