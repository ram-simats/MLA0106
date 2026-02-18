from itertools import permutations

def tsp(graph, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)

    min_cost = float('inf')
    best_path = []

    # Generate all possible permutations
    for perm in permutations(cities):
        current_cost = 0
        k = start

        # Calculate cost of current path
        for city in perm:
            current_cost += graph[k][city]
            k = city

        # Return to starting city
        current_cost += graph[k][start]

        # Update minimum cost
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = (start,) + perm + (start,)

    return min_cost, best_path


# Example Distance Matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_city = 0

cost, path = tsp(graph, start_city)

print("Minimum Cost:", cost)
print("Best Path:", path)
