import unittest
from py.algorithms.morris_traversal import Morris_Inorder_Traversal
from py.algorithms.morris_traversal import Morris_PreOrder_Traversal
from py.utils.binary_tree import binaryTreeNode


class test(unittest.TestCase):

    def test1(self):
        rootBT = binaryTreeNode(1)
        rootBT.right = binaryTreeNode(2)
        rootBT.right.left = binaryTreeNode(3)

        output = set()
        output.add(rootBT.right)
        output.add(rootBT)

        self.assertEqual(Morris_Inorder_Traversal(rootBT), output)
        self.assertEqual(Morris_PreOrder_Traversal(rootBT), output)

    def test2(self):
        rootBT = binaryTreeNode(1)
        rootBT.right = binaryTreeNode(2)
        rootBT.right.left = binaryTreeNode(3)

        rootBT.right.right = binaryTreeNode(5)

        output = set()
        output.add(rootBT)
        self.assertEqual(Morris_Inorder_Traversal(rootBT), output)
        self.assertEqual(Morris_PreOrder_Traversal(rootBT), output)

    def test3(self):
        rootBT = binaryTreeNode(1)
        rootBT.right = binaryTreeNode(2)
        rootBT.right.left = binaryTreeNode(3)
        rootBT.right.right = binaryTreeNode(5)
        rootBT.left = binaryTreeNode(9)

        output = set()
        self.assertEqual(Morris_Inorder_Traversal(rootBT), output)
        self.assertEqual(Morris_PreOrder_Traversal(rootBT), output)

    def test4(self):
        rootBT = binaryTreeNode(1)
        rootBT.right = binaryTreeNode(2)
        rootBT.right.left = binaryTreeNode(3)
        rootBT.right.right = binaryTreeNode(5)
        rootBT.left = binaryTreeNode(9)
        rootBT.left.left = binaryTreeNode(6)
        rootBT.left.left.right = binaryTreeNode(10)

        output = set()
        output.add(rootBT.left)
        output.add(rootBT.left.left)
        self.assertEqual(Morris_Inorder_Traversal(rootBT), output)
        self.assertEqual(Morris_PreOrder_Traversal(rootBT), output)


if __name__ == "__main__":
    unittest.main()
