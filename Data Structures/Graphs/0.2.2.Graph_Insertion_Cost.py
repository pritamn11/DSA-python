# Function to add an edge using adjacency matrix representation 

def add_node(v):
    global node_count
    if v in nodes:
        print(v,"is already present in the graph")
    else:
        node_count = node_count + 1 
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def insert_edge(node1, node2,cost):
    if node1 not in nodes:
        print(node1,"is not present in graph")
    elif node2 not in nodes:
        print(node2,"is not present in graph")
    else:
        index1 = nodes.index(node1)
        index2 = nodes.index(node2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost 

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"), end="  ")   # We use format for printing matrix in properly
        print()


nodes = []
graph = []
node_count = 0

add_node("A") 
add_node("B")   
add_node("C") 
add_node("D") 

insert_edge('A','B',10)  
insert_edge('A','D',5)    
print_graph()

