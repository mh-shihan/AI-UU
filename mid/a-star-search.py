import heapq

def a_star_search(graph, start, goal, heuristic):
    open_list = []  # Priority queue to store (f, g, node, path)
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))  # (f, g, node, path)

    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)  # Get the node with the lowest f(n)

        if current == goal:
            return path  # Return the shortest path

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None  # No path found

# Example Graph (Adjacency List)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'E': 2, 'G': 1},
    'E': {'B': 5, 'D': 2, 'H': 3},
    'F': {'C': 3, 'I': 6},
    'G': {'D': 1, 'H': 2},
    'H': {'E': 3, 'G': 2, 'I': 4},
    'I': {'F': 6, 'H': 4}
}

# Heuristic Values (Estimated distance to goal 'I')
heuristic = {
    'A': 10, 'B': 8, 'C': 9, 'D': 6, 'E': 4,
    'F': 7, 'G': 3, 'H': 2, 'I': 0
}

# Run A* Search from 'A' to 'I'
path = a_star_search(graph, 'A', 'I', heuristic)
print("Optimal Path:", path)

     
