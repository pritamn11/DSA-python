graph = {
    'A' : ['B','C','D'],
    'B' : ['A','D','E'],
    'C' : ['A','D'],
    'D' : ['A','B','C','D','E'],
    'E' : ['B','D']
}

graph['F'] = []
graph['E'].append('F')
print(graph)
