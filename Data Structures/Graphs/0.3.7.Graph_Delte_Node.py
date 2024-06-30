# Function to add a node using adjacency List representation
# this is weighted, undirected graph

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
        list1 = [node2, cost]
        graph[node1].append(list1)
        # graph[node2].append(list2) 

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
add_node('E')


add_edge('A','B',10)
add_edge('A','D',4)
add_edge('B','D',7)
add_edge('C','A',5)
add_edge('D','C',1)
add_edge('B','E',3)
add_edge('E','D',2)
print(graph)

delete_node('E')
print("After deleting node E")
print(graph)


# https://www.youtube.com/watch?v=Am3g025nqXA&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=69