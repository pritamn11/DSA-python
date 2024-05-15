graph = []

node_count=3

temp = []
for i in range(node_count):
    temp.append(0)
    graph.append(temp)
# print(graph)
# print(temp)

for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end=" ")
        print()