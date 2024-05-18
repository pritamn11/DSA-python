# Function to add a node using adjacency List representation
# this is unweighted, undirected graph

def add_node(node):
    if node in graph:
        print(node,"is already present in graph")
    else:
        graph[node] = []



graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
print(graph)


