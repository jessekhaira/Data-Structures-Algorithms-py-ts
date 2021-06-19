/**
 *  This class represents an efficient implementation of the DisjointSet data structure.
 *  Not only is the data structure implemented as an array, path compression is used in the
 *  find() method, and union by rank is used in the union() method.
 *
 *  This data structure tracks a set of elements partitioned into a number of disjoint subsets,
 *  typically used when dealing with undirected graphs. For example, to determine the number of
 *  connected components within an undirected graph, to determine if a cycle exists in an undirected
 *  graph, etc.
 *  @public @class
 */
class DisjointSet {
    /**
     *
     * @param {number} numNodes Int representing how many nodes there are in the undirected graph
     * @param {(object|null)} mapping Mapping between the nodes and indices in the disjoint set
     */
    constructor(numNodes, mapping = null) {
        /**
         * Disjoint Set represented as an array
         *
         * @public
         * @type {number[]}
         */
        this.disjointSet = Array(numNodes).fill(-1);

        this.mapping = mapping;
    }

    /**
     *  This method carries out the find operation for a given node in the disjoint set,
        and returns the representative of the given set. Carries out path compression.

     * Time:
     * - O(1) best/avg/worst
     * 
     * Space:
     * - O(1) best/avg/worst  
     * 
     * @param {(number|any)} x Can be an int referring to the index that the node is within
      the forest, or can be a node itself
     * @returns {number} Int representing the representative of the set 
     */
    find(x) {
        x = this.mapping === null ? x : this.mapping[x];
        // if the current node is just pointing at itself, that means its the representative of the set
        if (this.disjointSet[x] <= -1) {
            return x;
        }
        // otherwise find the representative of the set and set this nodes pointer to it

        this.disjointSet[x] = this.find(this.disjointSet[x]);

        return this.disjointSet[x];
    }

    /**
     *  This method carries out the union operation for the disjoint set, merging the two 
        sets that x and y belong to if x and y are not in the same set. Union by rank
        is implemented here. 
    
     * Time:
     * - O(1) best/avg/worst
     * 
     * Space:
     * - O(1) best/avg/worst  
     * 
     * @param {(number|any)} x Can be an int referring to the index that the node is within
        the forest, or can be a node itself
     * @param {(number|any)} y Can be an int referring to the index that the node is within
        the forest, or can be a node itself

     * @returns {null} None 
     */
    union(x, y) {
        const rX = this.find(x);
        const rY = this.find(y);
        if (rX === rY) {
            return null;
        }
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

export { DisjointSet };
