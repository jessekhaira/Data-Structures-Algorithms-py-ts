class DisjointSet:
    """
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
    """
    def __init__(self, number_nodes, mapping_nodes = None):
        # may need to have a mapping between the nodes and index they 
        # are slotted in array
        self.forest = [-1] * number_nodes
        self.mapping = mapping_nodes

    def find(self, x):
        """
        This method carries out the find operation for a given node in the disjoint set,
        and returns the representative of the given set. Carries out path compression. 

        Inputs:
            -> x (int//node): Can be an int referring to the index that the node is within
            the forest, or can be a node itself
        Outputs:
            -> int representing the representative of the set 
        """
        x = x if not self.mapping else self.mapping[x]
        # if the current node is just pointing at itself, that means its the representative of the set
        if self.forest[x] <= -1:
            return x
        # otherwise find the representative of the set and set this nodes pointer to it
        else:
            self.forest[x] = self.find(self.forest[x])
        
        return self.forest[x] 
        

    
    def union(self, x, y):
        """
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
        """
        rX = self.find(x)
        rY = self.find(y)
        if rX == rY:
            return
        
        # if rank is lower, more nodes point to that particular node and it will be
        # remain the representative of the entire set including merging node
        if self.forest[rX] < self.forest[rY]:
            self.forest[rY] = rX
        elif self.forest[rY] < self.forest[rX]:
            self.forest[rX] = rY
        
        # if they are equal, merge rY to rX randomly and decrease rank of rX
        else:
            self.forest[rY] = rX
            self.forest[rX] -= 1




        


