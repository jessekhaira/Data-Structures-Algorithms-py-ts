from utils.binaryTree import binaryTreeNode

class BinarySearchTree(object):
    """
    This class represents a binary search tree. This data structure is a
    rooted binary tree where for any given node, all values in the left subtree
    of that node are less than or equal to that nodes value, while all values in the right 
    subtree of that node are greater than that nodes value.

    This allows for efficient lookups, insertions, and deletions in the average
    case of O(logN) T | O(1)S. But this data structure does not guarantee balancing,
    meaning that in the worst case, there are O(N) T | O(1) S lookups, insertions, and 
    deletions.

    Inputs:
        -> val (int): Integer representing the value at the root of the BST
    """  
    def __init__(self, val):
        self.root = binaryTreeNode(val)
    
    def insertion(self,val):
        node = self.root
        return self._insertionHelper(val,node)
        
    def _insertionHelper(self, val, node):
        if not node:
            return binaryTreeNode(val)
        elif val <= node.val:
            node.left = self._insertionHelper(val, node.left)
            return node 
        
        elif val > node.val:
            node.right = self._insertionHelper(val, node.right)
            return node 

    def lookup(self, val):
        node = self.root
        return self._lookupHelper(node, val)
    
    def _lookupHelper(self, node, val):
        if not node:
            return 
        elif node.val == val:
            return node
        elif val <= node.val:
            return self._lookupHelper(node.left, val)
        else:
            return self._lookupHelper(node.right, val)

    def delete(self, val):
        node = self.root
        self._deleteHelperV(node, val)

    
    def _deleteHelperV(self, node, val):
        """
        This delete helper uses a convenient method to erase the node when the node has two
        children. This node actually doesn't erase the node with the target value, this method
        just replaces its value with the minimum value in the nodes right subtree.

        If you want to actually remove the node when the node has two children, use deleteHelperA. 
        """

        if not node:
            return
        elif val < node.val:
            node.left = self._deleteHelper(node.left, val)
            return node
        elif val > node.val:
            node.right = self._deleteHelper(node.right, val)
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

            # if node has two children, replace this nodes value with the minimum value in the
            # nodes right subtree, and then delete that node 
            minVal_inRightSubtree = self._getMinValRightV(node.right)
            node.val = minVal_inRightSubtree
            node.right = self._deleteHelper(node.right, minVal_inRightSubtree)
            return node 
    
    def _getMinValRightV(self, node):
        # min val has no left child 
        if not node.left:
            return node.val 
        return self._getMinValRight(node.left) 


    def _deleteHelperA(self, node, val):
        """
        This delete helper is the same as the other one, except when the node has two children, this method
        actually removes the node from the tree rather than just replacing its value with the minimum value
        in the right subtree. 
        """
        if not node:
            return
        elif val < node.val:
            node.left = self._deleteHelperA(node.left, val)
            return node
        elif val > node.val:
            node.right = self._deleteHelperA(node.right,val)
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
            node.right, minNode = self._getMinNode(node.right)
            # we have the minNode, set its left and right subtrees and return up
            minNode.left = node.left 
            minNode.right = node.right
            return minNode 

        
    def _getMinNode(self, node):
        if not node.left:
            return node.right, node
        node.left, minNode = self._getMinNode(node.left)
        return node, minNode
        
    
        
            
        
    