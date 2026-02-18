import heapq

def a_star(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    f_cost = {node: float('inf') for node in graph}
    f_cost[start] = heuristics[start]

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current]:
            temp_g_cost = g_cost[current] + cost

            if temp_g_cost < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = temp_g_cost
                f_cost[neighbor] = temp_g_cost + heuristics[neighbor]
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))

    return None


# Example Graph (node: [(neighbor, cost)])
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heuristic values (estimated distance to goal F)
heuristics = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

path = a_star(graph, heuristics, start, goal)

print("Shortest Path:", path)
