
def add_node(node):
    global node_count
    if node in nodes:
        print(node,"is already exist")
    else:
        node_count = node_count + 1
        nodes.append(node)

        for n in graph:
            n.append(0)
        
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


def insert_edge(node1, node2):
    if node1 not in nodes:
        print(node1,"not present in nodes")
    elif node2 not in nodes:
        print(node2,"not present in nodes")
    else:
        index1 = nodes.index(node1)
        index2 = nodes.index(node2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()



nodes = []
graph = []
node_count = 0 

add_node('A')
add_node('B')
add_node('C')
add_node('D')
print(nodes)
print(graph)
insert_edge('A','D')
print_graph()
