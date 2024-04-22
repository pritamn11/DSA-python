import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    # Set the distance to the start node as 0
    distances[start] = 0
    
    # Priority queue to store nodes with their tentative distances
    pq = [(0, start)]
    
    while pq:
        # Pop the node with the smallest tentative distance
        current_distance, current_node = heapq.heappop(pq)
        
        # If current distance is greater than the known shortest distance to current_node, skip
        if current_distance > distances[current_node]:
            continue
        
        # Iterate over neighbors of current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If the new distance is shorter than the known distance to neighbor, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, ":", shortest_distances)
