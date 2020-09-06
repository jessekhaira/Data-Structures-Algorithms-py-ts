def postOrderDFS_nary(node):
    """
    This algorithm traverses an N-Ary tree
    in post-order fashion recursively. 

    Assumes input nodes have a property .children
    containing all the children the node is connected to,
    and a property .val
    """
    if not node:
        return
    output = []
    postOrderHelper_recursive(node, output)
    return output

def postOrderHelper_recursive(node, output):
    if not node:
        return
    for child in node.children:
        postOrderHelper_recursive(child, output)
    output.append(node.val)



def postorder_iterative(self, node):
    """
    This algorithm traverses an N-Ary tree in post-order fashion iteratively. 

    Assumes input nodes have a property .children containing all the children the node is connected to,
    and a property .val.

    Key thing: emulate the recursive call stack using an actual stack.
    How we convert recursive code to iterative code. 
    """
    if not node:
        return
    stack = [(node,0)]
    output = [] 
    while stack:
        node, currIdxChild = stack.pop() 
        if currIdxChild == len(node.children):
            output.append(node.val)
        else:
            stack.append((node, currIdxChild+1))
            stack.append((node.children[currIdxChild], 0))
            
    return output 