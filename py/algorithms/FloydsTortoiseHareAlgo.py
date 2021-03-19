def floydsTortoiseHareAlgo(node):
    """
    This function represents floyd's tortoise and hare algorithm. It can be used to find whether or 
    not a cycle exists in a linked list, and at which node the cycle starts at using O(1) space 
    (versus doing the above tasks with a data structure like a hash set). 

    Time:
        - O(N) best/avg/worst

    Space:
        - O(1) best/avg/worst

    N - number of nodes in linked list 

    Inputs:
        - node (Linked List Node): Assumes the input is a node within a linked list with a .val property and 
        a .next property

    Outputs:
        - None if there is no cycle in the linked list, or the Node that starts the cycle 
    """
    if not node or not node.next:
        return  
    ptr1 = node
    ptr2 = node
    while ptr2 and ptr2.next:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
        if ptr1 == ptr2:
            break
    if ptr1 != ptr2:
        return  
    ptr1 = node
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1 
