class DisjointSet {
    /*
    This class represents the DisjointSet data structure using path compression, union 
    by rank, and implemented efficiently as an array. This data structure tracks a
    set of elements partitioned into a number of disjoint (non-overlapping) subsets.

    This data structure is primarily used when dealing with undirected graphs. For example,
    to find the number of connected components in an undirected graph, or to find if there
    is a cycle in a undirected graph.

    Provides constant time operations for all methods.

    Inputs:
        -> numNodes (int): Int representing how many nodes there are in the undirected graph
        -> mapping (HashMap // null): Mapping between the nodes and indices in the disjoint set
    */ 

    constructor(numNodes, mapping = null) {
        this.disjointSet = Array(numNodes).fill(-1);
        this.mapping = mapping; 
    }

    find(x) {
        /*
        This method carries out the find operation for a given node in the disjoint set,
        and returns the representative of the given set. Carries out path compression. 

        Inputs:
            -> x (int//node): Can be an int referring to the index that the node is within
            the forest, or can be a node itself
        Outputs:
            -> int representing the representative of the set 
        */
        x = (this.mapping === null ? x: this.mapping[x]);
        // if the current node is just pointing at itself, that means its the representative of the set
        if (this.disjointSet[x] <= -1) {
            return x; 
        }
        // otherwise find the representative of the set and set this nodes pointer to it
        else {
            this.disjointSet[x] = this.find(this.disjointSet[x]);
        }
        return this.disjointSet[x]; 
    }

    union(x, y) {
        /*
        This method carries out the union operation for the disjoint set, merging the two 
        sets that x and y belong to if x and y are not in the same set. Union by rank
        is implemented here. 

        Inputs:
            -> x (int//node): Can be an int referring to the index that the node is within
            the forest, or can be a node itself
            -> y (int//node): Can be an int referring to the index that the node is within
            the forest, or can be a node itself
        
        Returns:
            -> None
        */
        let rX = this.find(x);
        let rY = this.find(y);
        if (rX === rY) {
            return null;
        }
        else if (this.disjointSet[rX] < this.disjointSet[rY]) {
            this.disjointSet[rY] = rX;
        }
        else if (this.disjointSet[rY] < this.disjointSet[rX]) {
            this.disjointSet[rX] = rY; 
        }

        else {
            this.disjointSet[rY] = rX;
            this.disjointSet[rX] -= 1; 
        }
    }
}

export {DisjointSet}; 