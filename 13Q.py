# Minimax Algorithm for Tic Tac Toe

import math

# Print Board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()


# Check Winner
def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


# Check if moves left
def is_moves_left(board):
    for row in board:
        if " " in row:
            return True
    return False


# Minimax Function
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)

    if winner == "O":  # AI
        return 1
    elif winner == "X":  # Human
        return -1
    elif not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best = min(best, score)
        return best


# Find Best Move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False)
                board[i][j] = " "

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move


# Main Game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("You are X, AI is O\n")

    while True:
        print_board(board)

        # Player move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] != " ":
            print("Invalid move!")
            continue

        board[row][col] = "X"

        if check_winner(board) == "X":
            print_board(board)
            print("You win!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("Draw!")
            break

        # AI move
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = "O"

        if check_winner(board) == "O":
            print_board(board)
            print("AI wins!")
            break

        if not is_moves_left(board):
            print_board(board)
            print("Draw!")
            break


# Run Game
play_game()
