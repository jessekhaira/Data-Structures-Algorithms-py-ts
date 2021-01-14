import {BinaryTreeNode} from "./utils/BinaryTree";

/**
 *  This class represents a binary search tree. This data structure is a
    rooted binary tree where for any given node, all values in the left subtree
    of that node are less than or equal to that nodes value, while all values in the right 
    subtree of that node are greater than that nodes value.

    This allows for efficient lookups, insertions, and deletions in the average
    case of O(logN) T | O(1)S. But this data structure does not guarantee balancing,
    meaning that in the worst case, lookups, insertions, and deletions take O(N) T | O(1) S.

 * @constructor @public
 */
class BinarySearchTree {
    /**@param {number} val Value present at the root of the binary search tree */
    constructor(val) {
        /** Root of binary tree
         * @public
         * @type {BinaryTreeNode}
         */
        this.root = new BinaryTreeNode(val);
    }
    
    /**
     *  This method inserts a node into the binary search tree, will ensuring that the 
        binary search tree property is adhered to.

        Time Complexity:
            - best/average: O(logN)
            - worst: O(N) 
        Space Complexity:
            - O(1) b/a/w 
        
     * @param {number} val Integer representing the value to be inserted into the tree 
     */
    insert(val) {
        let node = this.root;
        return this._insertHelper(node, val);
    }
    
    _insertHelper(node, val) {
        if (node == null) {
            return new BinaryTreeNode(val);
        }
        else if (val <= node.val) {
            node.left = this._insertHelper(node.left, val);
            return node; 
        }
        else {
            node.right = this._insertHelper(node.right, val);
            return node; 
        }
    }

    lookup(val) {
        node = this.root;
        return this._lookupHelper(node, val);
    }

    _lookupHelper(node, val) {
        if (node == null) {
            return null; 
        }
        else if (val === node.val) {
            return node; 
        }
        else if (val < node.val) {
            return this._lookupHelper(node.left, val);
        }
        else if (val > node.val) {
            return this._lookupHelper(node.right, val);
        }
    }

    delete(val) {
        let node = this.root;
        return this._deleteHelperV(node, val);
    }

    _deleteHelperV(node, val) {
        /*
        This delete helper uses a convenient method to erase the node when the node has two
        children. This node actually doesn't erase the node with the target value, this method
        just replaces its value with the minimum value in the nodes right subtree.

        If you want to actually remove the node when the node has two children, use deleteHelperVA. 
        */
        if (node == null) {
            return null; 
        }
        else if (val < node.val) {
            node.left = this._deleteHelperV(node.left, val);
            return node; 
        }
        else if (val > node.val) {
            node.right = this._deleteHelperV(node.right, val);
            return node; 
        }
        else {
            if (node.left == null && node.right == null) {
                return null;
            }
            else if (!node.left) {
                return node.right;
            }
            else if (!node.right) {
                return node.left; 
            }
            let minVal = this._findMinValV(node.right);
            node.val = minVal;
            node.right = this._deleteHelperV(node.right, minVal);
            return node; 
        }
    }

    _findMinValV(node) {
        if (!node.left) {
            return node.val; 
        }
        return this._findMinValV(node.left); 
    }

    _deleteHelperVA(node,val) {
        /*
        This delete helper is the same as the other one, except when the node has two children, this method
        actually removes the node from the tree rather than just replacing its value with the minimum value
        in the right subtree. 
        */
        if (node == null) {
            return null;
        }
        else if (val < node.val) {
            node.left = this._deleteHelperVA(node.left, val);
            return node; 
        }
        else if (val > node.val) {
            node.right = this._deleteHelperVA(node.right, val);
            return node;
        }
        else {
            if (node.left == null && node.right == null) {
                return null;
            }
            else if (!node.left) {
                return node.right; 
            }
            else if (!node.right) {
                return node.left; 
            }
            [node.right, minNodeSubtree] = this._findMinNode(node.right);
            minNodeSubtree.left = node.left;
            minNodeSubtree.right = node.right;
            return minNodeSubtree; 
        }
    }

    _findMinNode(node) {
        if (node.left == null) {
            return [node.right, node];
        }
        [node.left, minNode] = this._findMinNode(node.left);
        return [node, minNode];
    }



}