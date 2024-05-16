graph = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
nodes = ['A', 'B', 'C','D']

index1 = nodes.index('A')
index2 = nodes.index('D')


print(index1)
print(index2)

graph[index1][index2] = 1
graph[index2][index1] = 1

def print_graph():
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            print(graph[i][j],end=" ")
        print()
print_graph()
