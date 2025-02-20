# Function to add node using adjacency matrix representation 

def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present in the graph")
    else:
        node_count = node_count + 1 
        nodes.append(v)
        for n in graph:     # adding new column with 0 
            n.append(0)
        # we need to add new row
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()


nodes = []
graph = []
node_count = 0


add_node("A") 
add_node("B")   
add_node("C") 
add_node("D") 
print("After adding nodes")
print(nodes)
print(graph)
print_graph()


