function postorder_recursive(node) {
    /*
    This algorithm traverses an N-Ary tree
    in post-order fashion recursively. 

    Assumes input nodes have a property .children
    containing all the children the node is connected to,
    and a property .val
    */
    if (node == null) {
        return []; 
    }
    let output = [];
    postOrder_helperRecursive(node, output);
    return output; 
}

function postOrder_helperRecursive(node, output) {
    if (node == null) {
        return; 
    }
    for (let child of node.children) {
        postOrder_helperRecursive(child, output);
    }
    output.push(node.val);
}


function postorder_iterative(node) {
    /*
    This algorithm traverses an N-Ary tree in post-order fashion iteratively. 

    Assumes input nodes have a property .children containing all the children the node is connected to,
    and a property .val.

    Key thing: emulate the recursive call stack using an actual stack.
    How we convert recursive code to iterative code. 
    */
    if (node == null) {
       return []; 
    }
    let stack = [[node,0]];
    let output = [];
    while (stack.length >0) {
        let [node, idx] = stack.pop();
        if (idx === node.children.length) {
            output.push(node.val);
        }
        else {
            stack.push([node, idx+1]);
            stack.push([node.children[idx], 0]);
        }
    }
    return output; 
} 
