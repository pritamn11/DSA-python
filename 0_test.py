
def add_node(node):
    global node_count
    if node in nodes:
        print(node,'is already exist in nodes')
    else:
        node_count = node_count + 1
        nodes.append(node)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


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
add_node('C')
print(nodes)
print(graph)
print_graph() 