# Function to add a node using adjacency List representation
# this is weighted, directed graph

def add_node(node):
    if node in graph:
        print(node,"is already present in graph")
    else:
        graph[node] = []

def add_edge(node1,node2,cost):
    if node1 not in graph:
        print(node1,"is not present in graph")
    elif node2 not in graph:
        print(node2,"is not present in graph")
    else:
        list1 = [node2,cost]  
        # list2 = [node1,cost]
        graph[node1].append(list1)
        # graph[node2].append(list2) 

graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
print(graph)
add_edge('A','D',4)
print(graph)

