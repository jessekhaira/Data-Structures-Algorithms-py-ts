def Morris_Inorder_Traversal(node):
    """
    This algorithm represents a way to traverse binary trees in-order using just
    O(1) space with the Morris Traversal algorithm.
    
    In in-order traversal, all the nodes in a given nodes left subtree are visited,
    then the current node is visited, then all the nodes in the right subtree of a given
    node are visited. 
    
    In this case, the algorithm is being used to find the number of nodes in the binary
    tree with just one child. 

    Time b/a/w: O(n) where n is the number of nodes in the tree
    Space b/a/w: O(1)

    Input:
        -> node (Binary Tree Node): Root of binary tree
    Output:
        -> set{} containing all nodes in the tree with one child 
    """
    if not node:
        return
    output = set()
    while node:
        # inorder traversal easy case - no left subtree means we just visit this node right away
        if not node.left:
            # don't want to add leaf nodes
            # also have to account for fact some leaf nodes will have artifical right node
            # unless we use an addition data structure to track those, we will just add and remove them
            # from the hash-set, which are efficient operations
            if node.right:
                output.add(node)
            node = node.right
        # if there is a left subtree, then we need some way to get back to this node after
        # visiting every node in the left subtree. So we get the absolute last node that will be visited
        # in the left subtree and set its right pointer to the current node
        else:
            lastNodeInLeftSubtree = getPrevNode(node)
            if not lastNodeInLeftSubtree.right:
                lastNodeInLeftSubtree.right = node
                node = node.left
            elif lastNodeInLeftSubtree.right == node:
                lastNodeInLeftSubtree.right = None
                # if the node has a left subtree, its guaranteed at this point to not have
                # a right subtree so we can add it
                if lastNodeInLeftSubtree.left:
                    output.add(lastNodeInLeftSubtree)
                # otherwise, this connecting node was a leaf node and will be present in output
                # so we have to remove it
                else:
                    output.remove(lastNodeInLeftSubtree)
                if not node.right:
                    output.add(node)
                node = node.right
    return output


def getPrevNode(node):
    nodeL = node.left
    while nodeL.right and nodeL.right != node:
        nodeL = nodeL.right
    return nodeL


def Morris_PreOrder_Traversal(node):
    """
    This algorithm represents a way to traverse binary trees in pre-order manner using just
    O(1) space with the Morris Traversal algorithm.
    
    In pre-order traversal, the node is visited first, then its left subtree, then its right subtree. 

    In this case, the algorithm is being used to find the number of nodes in the binary
    tree with just one child. 

    Time b/a/w: O(n) where n is the number of nodes in the tree
    Space b/a/w: O(1)

    Input:
        -> node (Binary Tree Node): Root of binary tree
    Output:
        -> set{} containing all nodes in the tree with one child 
    """
    output = set()
    while node:
        if node.left:
            prevNode = getPrevNode(node)
            if not prevNode.right:
                prevNode.right = node
                if not node.right:
                    output.add(node)
                node = node.left
            else:
                prevNode.right = None
                if prevNode.left:
                    output.add(prevNode)
                else:
                    output.remove(prevNode)
                node = node.right
        else:
            if node.right:
                output.add(node)
            node = node.right
    return output
