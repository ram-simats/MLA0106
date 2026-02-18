from collections import deque

# Initial state: (M_left, C_left, Boat_position)
# Boat_position = 1 means left side, 0 means right side
start = (3, 3, 1)
goal = (0, 0, 0)

# Possible boat moves (M, C)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def is_valid(state):
    M_left, C_left, boat = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    # Check boundaries
    if M_left < 0 or C_left < 0 or M_left > 3 or C_left > 3:
        return False

    # Missionaries should not be outnumbered
    if (M_left > 0 and C_left > M_left):
        return False
    if (M_right > 0 and C_right > M_right):
        return False

    return True


def solve():
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        visited.add(state)

        M_left, C_left, boat = state

        for M, C in moves:
            if boat == 1:  # Boat on left side
                new_state = (M_left - M, C_left - C, 0)
            else:  # Boat on right side
                new_state = (M_left + M, C_left + C, 1)

            if is_valid(new_state) and new_state not in visited:
                queue.append((new_state, path + [state]))

    return None


def print_solution(solution):
    print("Solution Found:\n")
    for step in solution:
        M_left, C_left, boat = step
        side = "Left" if boat == 1 else "Right"
        print(f"Left: M={M_left}, C={C_left} | Boat: {side}")


solution = solve()

if solution:
    print_solution(solution)
else:
    print("No Solution Exists")
