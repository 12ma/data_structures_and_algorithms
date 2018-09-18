class Vertex:
    def __init__(self, vertex=None):
        """Constructs a vertex"""
        self.vertex = vertex

    def __repr__(self):
        """Set up a graph with vertices"""
        return f'Graph: {self.vertex}'

    def __str__(self):
        """An official String representation of the vertice object"""
        return f'Graph: {self.vertex}'


class Graph:
    def __init__(self):
        """Constructs an empty graph"""
        self.graph = {}

    def __repr__(self):
        """Set up a graph with vertices"""
        return f'Graph: {self.graph}'

    def __str__(self):
        """An official String representation of the vertice object"""
        return f'Graph: {self.graph}'

    def __len__(self):
        """Length of the graph"""
        return len(self.graph)

    def add_vert(self, val):
        """Add vertex as a value."""
        if self.has_vert(val):
            return 'Already has the vertex!'
        self.graph[val] = {}

    def has_vert(self, val):
        """A helper method to check for existing vertices."""
        if val in self.graph.keys():
            return True
        return False

    def add_edge(self, v1, v2, weight):
        """Adds an edge when two vertices are present, edge has a weight."""
        if self.has_vert(v1) is False:
            return 'No Vertex found'
        if v2 not in self.graph[v1]:
            self.graph[v1][v2] = weight
        else:
            return 'Edge already exist'

    def get_neighbors(self, val):
        """Gets the neighbors of that vertex"""
        if self.has_vert(val) is False:
            return 'No Vertex found'
        elif self.graph[val].keys():
            n = []

            for k in self.graph[val].keys():
                n.append(k)
            return n
        else:
            return 'No neighbors found.'

    def breadth_first_graph(self, start):
        """This method recursively visits the neighbors of the current vertex
        then returns the visited list"""
        visited = []

        def _walk(vertex):
            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    _walk(neighbor)
        visited.append(start)
        _walk(start)
        return visited











