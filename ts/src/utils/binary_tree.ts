class BinaryTreeNode {
    val;

    left: null | BinaryTreeNode;

    right: null | BinaryTreeNode;

    constructor(val: number) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class NaryTreeNode<T> {
    val: T;

    children: NaryTreeNode<T>[];

    constructor(val: T) {
        this.val = val;
        this.children = [];
    }
}

export { BinaryTreeNode, NaryTreeNode };
