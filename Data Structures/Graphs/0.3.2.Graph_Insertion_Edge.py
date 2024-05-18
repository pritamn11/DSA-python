# Function to add a node using adjacency List representation
# this is unweighted, undirected graph

def add_node(node):
    if node in graph:
        print(node,"is already present in graph")
    else:
        graph[node] = []

def add_edge(node1,node2):
    if node1 not in graph:
        print(node1,"is not present in graph")
    elif node2 not in graph:
        print(node2,"is not present in graph")
    else:
        graph[node1].append(node2)
        graph[node2].append(node1)


graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
print(graph)
add_edge('A','D')
add_edge('A','B')
add_edge('A','C')
print(graph)

