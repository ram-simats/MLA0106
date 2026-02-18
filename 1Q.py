from collections import deque

# Goal State
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

# Possible moves (Up, Down, Left, Right)
MOVES = {
    "UP": -3,
    "DOWN": 3,
    "LEFT": -1,
    "RIGHT": 1
}

def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)

    for move, position_change in MOVES.items():
        new_index = zero_index + position_change

        # Check boundaries
        if move == "LEFT" and zero_index % 3 == 0:
            continue
        if move == "RIGHT" and zero_index % 3 == 2:
            continue
        if 0 <= new_index < 9:
            new_state = list(state)
            # Swap
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))

    return neighbors


def solve_puzzle(start_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state == GOAL_STATE:
            return path + [current_state]

        visited.add(current_state)

        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                queue.append((neighbor, path + [current_state]))

    return None


def print_solution(solution):
    for step in solution:
        print("-------")
        print(step[0], step[1], step[2])
        print(step[3], step[4], step[5])
        print(step[6], step[7], step[8])
    print("-------")


# Example Start State
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = solve_puzzle(start)

if solution:
    print("Solution Found!\n")
    print_solution(solution)
else:
    print("No solution exists.")
