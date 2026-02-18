from collections import deque

def water_jug_problem(x, y, target):
    # To keep track of visited states
    visited = set()
    
    # Queue for BFS
    queue = deque()
    
    # Initial state (0, 0)
    queue.append((0, 0, []))  # (jug1, jug2, path)

    while queue:
        jug1, jug2, path = queue.popleft()
        
        # If target is reached
        if jug1 == target or jug2 == target:
            path.append((jug1, jug2))
            return path
        
        # If already visited, skip
        if (jug1, jug2) in visited:
            continue
        
        visited.add((jug1, jug2))
        
        # Possible operations
        next_states = [
            (x, jug2),  # Fill Jug1
            (jug1, y),  # Fill Jug2
            (0, jug2),  # Empty Jug1
            (jug1, 0),  # Empty Jug2
            # Pour Jug1 -> Jug2
            (jug1 - min(jug1, y - jug2), jug2 + min(jug1, y - jug2)),
            # Pour Jug2 -> Jug1
            (jug1 + min(jug2, x - jug1), jug2 - min(jug2, x - jug1)),
        ]
        
        for state in next_states:
            queue.append((state[0], state[1], path + [(jug1, jug2)]))
    
    return None


# Example usage
if __name__ == "__main__":
    x = 4   # Capacity of Jug1
    y = 3   # Capacity of Jug2
    target = 2  # Target amount
    
    solution = water_jug_problem(x, y, target)
    
    if solution:
        print("Steps to reach the target:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")
