import BinarySearchTree from '../../data structures/binary_search_tree';
import breadthFirstSearch from '../../algorithms/breadth_first_search';

test('test 1 for breadth first search algorithm', () => {
    const bst: BinarySearchTree = new BinarySearchTree(3);
    bst.insert(9);
    bst.insert(10);

    const output = [[3], [9], [10]];
    expect(breadthFirstSearch(bst.root)).toStrictEqual(output);
});

test('test 2 for breadth first search algorithm', () => {
    const bst: BinarySearchTree = new BinarySearchTree(3);

    const output = [[3]];
    expect(breadthFirstSearch(bst.root)).toStrictEqual(output);
});

test('test 3 for breadth first search algorithm', () => {
    const bst: BinarySearchTree = new BinarySearchTree(1235);
    bst.insert(50);
    bst.insert(95);
    bst.insert(3500);
    bst.insert(2400);
    bst.insert(2350);

    const output = [[1235], [50, 3500], [95, 2400], [2350]];
    console.log(breadthFirstSearch(bst.root));
    // expect(breadthFirstSearch(bst.root)).toStrictEqual(output);
});
