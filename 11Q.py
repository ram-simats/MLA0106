# Map Coloring using Backtracking (CSP)

# Define the map (Adjacency List)
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW':['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  []  # Tasmania (no neighbors)
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Dictionary to store final color assignment
solution = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True


def solve():
    if len(solution) == len(graph):
        return True

    # Select unassigned region
    for region in graph:
        if region not in solution:
            for color in colors:
                if is_safe(region, color):
                    solution[region] = color

                    if solve():
                        return True

                    # Backtrack
                    del solution[region]

            return False


if solve():
    print("Map Coloring Solution:")
    for region in solution:
        print(region, "→", solution[region])
else:
    print("No solution found.")
