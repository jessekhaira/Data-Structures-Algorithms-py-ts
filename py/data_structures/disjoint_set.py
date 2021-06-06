""" This module contains code for a class that represents the
disjoint set data structure """
from typing import Dict, Any, Union


class DisjointSet:
    """ This class represents an efficient implementation of the
    DisjointSet data structure.

    Not only is the data structure implemented as an array, path
    compression is used in the find() method, and union by rank
    is used in the union() method.

    This data structure tracks a set of elements partitioned into
    a number of disjoint subsets, typically used when dealing with
    undirected graphs. For example, to determine the number of
    connected components within an undirected graph, to determine
    if a cycle exists in an undirected graph, etc.

    Attributes:
        number_nodes:
            Integer representing how many nodes there are in the undirected
            graph

        mapping_nodes:
            Dictionary representing a mapping between nodes and the index
            whcih represents them in the disjoint set, or None if not
            needed.
    """

    def __init__(self,
                 number_nodes: int,
                 mapping_nodes: Union[Dict[Any, int], None] = None):
        # may need to have a mapping between the nodes and index they
        # are slotted in array
        self.forest = [-1] * number_nodes
        self.mapping = mapping_nodes

    def find(self, x: Union[int, Any]) -> int:
        """ This method carries out the find operation for a given node
        in the disjoint set, and returns the representative of the given
        set. Carries out path compression.

        Time:
            O(1) best/avg/worst

        Space:
            O(1) best/avg/worst

        Args:
            x:
                Integer representing the index that the node is stored within
                inside of the disjoint set, or can be the node itself. If the
                node is provided, self.mapping cannot be None.

        Returns:
            An integer representing the representative of the set
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

        Time:
            - O(1) best/avg/worst
        Space:
            - O(1) best/avg/worst

        Inputs:
            - x (int || node): Can be an int referring to the index that the node is within
                the forest, or can be a node itself
                
            - y (int || node): Can be an int referring to the index that the node is within
                the forest, or can be a node itself
        
        Returns:
            - None
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
