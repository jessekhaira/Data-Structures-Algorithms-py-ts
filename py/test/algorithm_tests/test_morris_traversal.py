import unittest
from py.algorithms.morris_traversal import morris_inorder_traversal
from py.algorithms.morris_traversal import morris_pre_order_traversal
from py.utils.binary_tree import BinaryTreeNode


class test(unittest.TestCase):

    def test1(self):
        rootBT = BinaryTreeNode(1)
        rootBT.right = BinaryTreeNode(2)
        rootBT.right.left = BinaryTreeNode(3)

        output = set()
        output.add(rootBT.right)
        output.add(rootBT)

        self.assertEqual(morris_inorder_traversal(rootBT), output)
        self.assertEqual(morris_pre_order_traversal(rootBT), output)

    def test2(self):
        rootBT = BinaryTreeNode(1)
        rootBT.right = BinaryTreeNode(2)
        rootBT.right.left = BinaryTreeNode(3)

        rootBT.right.right = BinaryTreeNode(5)

        output = set()
        output.add(rootBT)
        self.assertEqual(morris_inorder_traversal(rootBT), output)
        self.assertEqual(morris_pre_order_traversal(rootBT), output)

    def test3(self):
        rootBT = BinaryTreeNode(1)
        rootBT.right = BinaryTreeNode(2)
        rootBT.right.left = BinaryTreeNode(3)
        rootBT.right.right = BinaryTreeNode(5)
        rootBT.left = BinaryTreeNode(9)

        output = set()
        self.assertEqual(morris_inorder_traversal(rootBT), output)
        self.assertEqual(morris_pre_order_traversal(rootBT), output)

    def test4(self):
        rootBT = BinaryTreeNode(1)
        rootBT.right = BinaryTreeNode(2)
        rootBT.right.left = BinaryTreeNode(3)
        rootBT.right.right = BinaryTreeNode(5)
        rootBT.left = BinaryTreeNode(9)
        rootBT.left.left = BinaryTreeNode(6)
        rootBT.left.left.right = BinaryTreeNode(10)

        output = set()
        output.add(rootBT.left)
        output.add(rootBT.left.left)
        self.assertEqual(morris_inorder_traversal(rootBT), output)
        self.assertEqual(morris_pre_order_traversal(rootBT), output)


if __name__ == "__main__":
    unittest.main()
