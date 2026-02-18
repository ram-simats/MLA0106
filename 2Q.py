N = 8

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()


# Check if it's safe to place queen at board[row][col]
def is_safe(board, row, col):

    # Check same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Backtracking function
def solve_nqueens(board, row):

    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen

            if solve_nqueens(board, row + 1):
                return True

            board[row][col] = 0  # Backtrack

    return False


# Create empty board
board = [[0 for _ in range(N)] for _ in range(N)]

if solve_nqueens(board, 0):
    print("Solution Found:\n")
    print_board(board)
else:
    print("No Solution Exists")
