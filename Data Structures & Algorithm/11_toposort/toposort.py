# -*- coding: utf-8 -*-
# Nimi: Ali Amaan
# Opiskelijanumero: 906955
class Graph:
    """A graph represented in terms
        of vertices and an adjacency list
        (implemented as a dictionary).
        Adjacency list has vertices as keys
        and their corresponding neighbour lists
        as values. The class is mainly a wrapper for
        vertex and adjacency listing."""

    def __init__(self, V: list, Adj: list):
        """Create a graph from given vertices
            and their adjacency listing."""
        #​‌​‌‌​​​‌​‌​​​‌ List of vertices, e.g. clothes
        self.vertices = V

        #​‌​‌‌​​​‌​‌​​​‌ Dictionary, key is the vertex itself and value is a list of its neighbours
        #​‌​‌‌​​​‌​‌​​​‌ given as their indices in the vertex listing
        #​‌​‌‌​​​‌​‌​​​‌ E.g. {"collared shirt": [6, 7, 9], ...}
        self.adjacency = {V[i]: Adj[i] for i in range(len(V))}

    def neighbours(self, vertex):
        """Return the neighbours of given vertex in a list.
        E.g. input neighbours("shirt") would return
        ["belt", "necktie", "teekkari cap"]."""
        return [self.vertices[i] for i in self.adjacency[vertex]]

    def __iter__(self):
        """An iterator to access the vertices of the graph e.g.
            in a for-loop."""
        yield from self.vertices

def sort_help(G: Graph, v, visited, ordering):
    visited.remove(v)
    for i in G.neighbours(v):
        if i in visited:
            sort_help(G, i, visited, ordering)
    ordering.insert(0, v)

def topo_sort(G: Graph):
    """Topologically sort the given DAG G.
        Return a list containing G's vertices
        in a topological order. Use depth first search.
        It is recommended to use a recursive helper
        function to visit the vertices."""
    ordering = []
    visited = set()
    for i in G.vertices:
        visited.add(i)
    for i in G.vertices:
        if i in visited:
            sort_help(G, i, visited, ordering)

    return ordering

def main():
    #​‌​‌‌​​​‌​‌​​​‌A simple test for your function, more tests in tests.py
    #​‌​‌‌​​​‌​‌​​​‌Topologically sort clothes to determine a dressing order.
    clothes = ["shoes",
               "collared shirt",
               "socks",
               "watch",
               "suit trousers",
               "undershorts",
               "belt",
               "necktie",
               "suit jacket",
               "teekkari cap"]
    #​‌​‌‌​​​‌​‌​​​‌Store relationships between clothes (edges of graph) as an adjacency list
    #​‌​‌‌​​​‌​‌​​​‌The clothes are described by their indices in 'clothes'
    #​‌​‌‌​​​‌​‌​​​‌A position in 'clothAdjacency' corresponds to item with same
    #​‌​‌‌​​​‌​‌​​​‌position in 'clothes' and the list stored in that position contains
    #​‌​‌‌​​​‌​‌​​​‌the item's neighbours
    #​‌​‌‌​​​‌​‌​​​‌Neighbours are clothes that can be put on only after their parent is on
    #​‌​‌‌​​​‌​‌​​​‌I.e. "socks" have to be put on before "shoes"
    clothAdjacency = [[], #"shoes" don't have neighbours
                      [6, 7, 9],
                      [0], #"socks" have "shoes" as neighbour
                      [],
                      [6],
                      [4, 0],
                      [8],
                      [8],
                      [],
                      []]
    #​‌​‌‌​​​‌​‌​​​‌Create a graph from the two lists
    clothGraph = Graph(clothes, clothAdjacency)
    #​‌​‌‌​​​‌​‌​​​‌Topologically sort the graph with your implementation
    ordering = topo_sort(clothGraph)
    print("Clothes can be put on in the following order:")
    for garment in ordering:
        print(garment)

if __name__ == '__main__':
    main()

