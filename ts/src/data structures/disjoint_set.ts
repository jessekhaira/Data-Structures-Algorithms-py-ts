/**
 * @fileoverview This module contains code for a class that represents the
 * disjoint set data structure
 * @package
 */

/**
 *  This class represents an efficient implementation of the
 *  DisjointSet data structure.
 *
 *  Not only is the data structure implemented as an array, path
 *  compression is used in the find() method, and union by rank
 *  is used in the union() method.
 *
 *  This data structure tracks a set of elements partitioned into
 *  a number of disjoint subsets, typically used when dealing with
 *  undirected graphs. For example, to determine the number of
 *  connected components within an undirected graph, to determine
 *  if a cycle exists in an undirected graph, etc.
 *  @public @class
 */
class DisjointSet {
    disjointSet: number[];

    mapping: Record<string | number, number> | null;

    /**
     *
     * @param {number} numNodes Integer representing how many nodes
            there are in the undirected graph
     * @param {Record<string | number, number> | null} mapping Mapping between
            keys, which can be strings and numbers, to numbers which represent
            indices in the disjoint set. Can also be null if unneeded
     */
    constructor(
        numNodes: number,
        mapping: Record<string | number, number> | null = null,
    ) {
        /**
         *  Array of integers representing the disjoint set. When an index
         *  has a value less then zero, that indicates that it is the
         *  representative of a set, where you can find the rank by multiplying
         *  by -1 and adding 1
         * @public
         * @type {number[]}
         */
        this.disjointSet = [];
        for (let i = 0; i < numNodes; i += 1) {
            this.disjointSet.push(-1);
        }

        /**
         *  Dictionary representing a mapping between nodes and the index
         *  which represents them in the disjoint set, or None if not
         *  needed
         *  @public
         *  @type {Record<string | number, number> | null}
         */
        this.mapping = mapping;
    }

    /**
     *  This method carries out the find operation for a given node
     *  in the disjoint set, and returns the representative of the
     *  given set. Carries out path compression. 
     * 
     *  If the mapping is defined, then this method will always
     *  expect the input argument to be of type string. 

     * Time:
     * - O(1) best/avg/worst
     * 
     * Space:
     * - O(1) best/avg/worst  
     * 
     * @param {(number|any)} x Can be an int referring to the index that
     *      the node is within the forest, or can be a node itself
     * @returns {number} Int representing the representative of the set 
     */
    find(x: number | string): number {
        const lookupNode = this.mapping ? this.mapping[x] : (x as number);
        // if the current node is just pointing at itself, that means its the
        // representative of the set
        if (this.disjointSet[lookupNode] <= -1) {
            return lookupNode;
        }
        // otherwise find the representative of the set and set this nodes
        // pointer to it

        this.disjointSet[lookupNode] = this.find(this.disjointSet[lookupNode]);

        return this.disjointSet[lookupNode];
    }

    /**
     *  This method carries out the union operation for the disjoint set,
     *  merging the two sets that x and y belong to if x and y are not in
     *  the same set. Union by rank is implemented here. 
    
     * Time:
     * - O(1) best/avg/worst
     * 
     * Space:
     * - O(1) best/avg/worst  
     * 
     * @param {number|string} x Can be an int referring to the index that the
     *      node is within the forest, or can be a node itself
     * @param {number|string} y Can be an int referring to the index that the
     *      node is within the forest, or can be a node itself
     * @returns {null} None 
     */
    union(x: number | string, y: number | string): void {
        const rX = this.find(x);
        const rY = this.find(y);
        if (rX !== rY) {
            if (this.disjointSet[rX] < this.disjointSet[rY]) {
                this.disjointSet[rY] = rX;
            } else if (this.disjointSet[rY] < this.disjointSet[rX]) {
                this.disjointSet[rX] = rY;
            } else {
                this.disjointSet[rY] = rX;
                this.disjointSet[rX] -= 1;
            }
        }
    }
}

export default DisjointSet;
