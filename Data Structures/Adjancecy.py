class GraphAdjMatrix:
    def __init__(self, n):
        """
        Initialize the graph with n vertices (0-based index).
        We create an n x n matrix initialized to 0 (no edges).
        
        Time Complexity: O(n²) for space allocation.
        Space Complexity: O(n²)
        """
        self.n = n  # Number of vertices
        self.graph = [[0] * n for _ in range(n)]  # Create an n x n adjacency matrix

    def add_edge(self, u, v, weight=1):
        """
        Add an edge between vertex u and v with a given weight (default weight = 1).
        If weight is not provided, it's assumed unweighted (default is 1).
        
        For undirected graph, we need to add the reverse edge as well.
        
        Time Complexity: O(1) for adding an edge (constant time).
        Space Complexity: O(1) for adding one edge (constant space).
        """
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # Since it's an undirected graph

    def display(self):
        """Display the adjacency matrix."""
        for row in self.graph:
            print(row)

# Example: No weights, no directions (undirected unweighted graph)
n = 4  # Number of vertices
graph_matrix = GraphAdjMatrix(n)
graph_matrix.add_edge(0, 1)
graph_matrix.add_edge(1, 2)
graph_matrix.add_edge(2, 3)
graph_matrix.display()

# Time and Space Complexity:
# Time Complexity of adding an edge: O(1)
# Space Complexity: O(n²) (as we store an n x n matrix)
