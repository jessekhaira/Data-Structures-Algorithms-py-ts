import unittest
from py.data_structures.BinarySearchTree import BinarySearchTree

class Tests(unittest.TestCase):
    def testInsertion(self):
        bst = BinarySearchTree(3)
        for val in range(8):
            bst.insertion(val)
        
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