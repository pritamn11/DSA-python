class Graph:
    def __init__(self):
        """
        Initialize an empty graph with no nodes and an empty adjacency matrix.
        """
        self.nodes = []
        self.graph = []
        self.node_count = 0

    def add_node(self,node):
        """
        Add a node to the graph and update the adjacency matrix.
        :param node: The node to be added to the graph.
        """
        if node in self.nodes:
            print(f"{node} already exists in the graph")
        else:
            self.node_count += 1
            self.nodes.append(node)
            # Expand existing rows to include the new node
            for n in self.graph:
                n.append(0)
            # Add a new row for the new node
            temp = [0] * self.node_count
            self.graph.append(temp)

    def add_edge(self,node1,node2):
        if node1 not in self.nodes:
            print(f"{node1} is not present in nodes")
        elif node2 not in self.nodes:
            print(f"{node2} is not present in nodes")
        else:
            index1 = self.nodes.index(node1)
            index2 = self.nodes.index(node2)
            self.graph[index1][index2] = 1
            self.graph[index2][index1] = 1

    
    def display_graph(self):
        """
        Display the adjacency matrix of the graph.
        """
        print("Adjacency Matrix:")
        for row in self.graph:
            print(" ".join(map(str, row)))
        

graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D') 

graph.display_graph()
graph.add_edge('A','D')
graph.add_edge('C','B')
graph.add_edge('A','C')
graph.display_graph()