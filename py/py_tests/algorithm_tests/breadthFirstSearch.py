from py.data_structures.BinarySearchTree import BinarySearchTree
import unittest
from py.algorithms.breadthFirstSearch import breadthFirstSearch

class tests(unittest.TestCase):
    def test1(self):
        bst = BinarySearchTree(5)
        ints = [3,5,1,2,-5,-9]
        for val in ints:
            bst.insertion(val)

        self.assertEqual(breadthFirstSearch(bst.root), [[5], [3, 5], [1],[-5,2], [-9]])
        
if __name__ == "__main__": 
    unittest.main() 