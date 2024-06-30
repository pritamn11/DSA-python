# Function to delete a node using adjacency matrix representation 
# This is weighted undirected graph

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


def add_edge(node1, node2,e):
    if node1 not in nodes:
        print(node1,"is not present in graph")
    elif node2 not in nodes:
        print(node2,"is not present in graph")
    else:
        index1 = nodes.index(node1)
        index2 = nodes.index(node2)
        graph[index1][index2] = e
        graph[index2][index1] = e

def delete_node(node):
    global node_count
    if node not in nodes:
        print(node,"is not present in graph")
    else:
        index1 = nodes.index(node)
        node_count = node_count - 1 
        nodes.remove(node)
        graph.pop(index1) 
        for i in graph:
            i.pop(index1)

        
        

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"), end="  ") 
        print()


nodes = []
graph = []
node_count = 0

add_node("A") 
add_node("B")   
add_node("C") 
add_node("D") 

add_edge('A','B',10)  
add_edge('A','D',5)    
add_edge('A','C',7) 
add_edge('B','D',4)
add_edge('D','C',8)
# print(graph)   
# print(nodes)
print_graph()
delete_node('A')
print()
print_graph()
# print(graph)
# print(nodes)


