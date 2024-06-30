# Function to delete a node using adjacency List representation
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

def delete_node(node):
    if node not in graph:
        print(f"{node} not present in graph")
    else:
        graph.pop(node)
        for i in graph:
            list1 = graph[i]
            if node in list1:
                list1.remove(node)


graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')

add_edge('A','D')
add_edge('B','D')
add_edge('C','A')
add_edge('A','B')
add_edge('D','C')
print(graph)
print()
delete_node('A')
print(graph)

