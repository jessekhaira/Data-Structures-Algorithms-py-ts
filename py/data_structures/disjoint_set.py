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

        mapping:
            Dictionary representing a mapping between nodes and the index
            which represents them in the disjoint set, or None if not
            needed

        forest:
            Array of integers representing the disjoint set. When an index
            has a value less then zero, that indicates that it is the
            representative of a set, where you can find the rank by multiplying
            by -1 and adding 1
    """

    def __init__(self,
                 number_nodes: int,
                 mapping: Union[Dict[Any, int], None] = None):
        # may need to have a mapping between the nodes and index they
        # are slotted in array
        self.forest = [-1] * number_nodes
        self.mapping = mapping

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
        # if the current node is just pointing at itself, that means its the
        # representative of the set
        if self.forest[x] <= -1:
            return x
        # otherwise find the representative of the set and set this nodes
        # pointer to it
        else:
            self.forest[x] = self.find(self.forest[x])

        return self.forest[x]

    def union(self, x: Union[int, Any], y: Union[int, Any]) -> None:
        """ This method carries out the union operation for the disjoint set,
        merging the two sets that x and y belong to if x and y are not in the
        same set. Union by rank is implemented here.

        Time:
            O(1) best/avg/worst

        Space:
            O(1) best/avg/worst

        Args:
            x:
                Integer representing the index that the node is stored within
                inside of the disjoint set, or can be the node itself. If the
                node is provided, self.mapping cannot be None.

            y:
                Integer representing the index that the node is stored within
                inside of the disjoint set, or can be the node itself. If the
                node is provided, self.mapping cannot be None.
        """
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x == r_y:
            return

        # if rank is lower, more nodes point to that particular node and it will
        # remain the representative of the entire set including merging node
        if self.forest[r_x] < self.forest[r_y]:
            self.forest[r_y] = r_x
        elif self.forest[r_y] < self.forest[r_x]:
            self.forest[r_x] = r_y

        # if they are equal, merge r_y to r_x randomly and decrease rank of r_x
        else:
            self.forest[r_y] = r_x
            self.forest[r_x] -= 1
