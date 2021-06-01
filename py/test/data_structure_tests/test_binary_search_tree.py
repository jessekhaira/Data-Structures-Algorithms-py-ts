import unittest
from py.data_structures.binary_search_tree import BinarySearchTree


class Tests(unittest.TestCase):

    def testInsertion(self):
        bst = BinarySearchTree(3)
        for val in range(8):
            bst.insertion(val)

        self.assertEqual(validateBST(bst), True)

    def testLookup(self):
        bst = BinarySearchTree(4)
        ints = [1, 2, 3, 5, 6, 7, 8]
        for val in ints:
            bst.insertion(val)

        for val in ints:
            self.assertEqual(bst.lookup(val).val, val)

    def testDelete(self):
        bst = BinarySearchTree(4)
        ints = [1, 2, 3, 5, 6, 7, 8]
        for val in ints:
            bst.insertion(val)

        bst.delete(5)
        bst.delete(4)
        self.assertEqual(None, bst.lookup(5))
        self.assertEqual(None, bst.lookup(4))
        self.assertEqual(validateBST(bst), True)


def validateBST(bst):
    return validateBSTHelper(bst.root, float('-inf'), float('inf'))


def validateBSTHelper(node, lowBound, highBound):
    if not node:
        return True
    if not lowBound <= node.val < highBound:
        return False
    valid_left_subtree = validateBSTHelper(node.left, lowBound, node.val)
    valid_right_subtree = validateBSTHelper(node.right, node.val, highBound)
    return valid_left_subtree and valid_right_subtree


if __name__ == "__main__":
    unittest.main()
