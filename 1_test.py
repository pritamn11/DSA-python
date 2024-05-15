class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)

        self.adjacency_list[vertex1].append((vertex2, weight))
        self.adjacency_list[vertex2].append((vertex1, weight))  # Uncomment for undirected graph

    def print_graph(self):
        for vertex, edges in self.adjacency_list.items():
            print(vertex, "->", ", ".join(f"{edge[0]} ({edge[1]})" for edge in edges))


# Example Usage:
if __name__ == "__main__":
    # Create a graph
    graph = Graph()

    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    # Add edges
    graph.add_edge("A", "B", 2)
    graph.add_edge("B", "C", 3)
    graph.add_edge("C", "D", 4)
    graph.add_edge("D", "A", 1)

    # Print the graph
    graph.print_graph()
