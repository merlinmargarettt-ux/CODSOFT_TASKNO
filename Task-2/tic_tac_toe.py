import math

board = [" " for _ in range(9)]


def print_board():
    print()
    print("-------------")
    for i in range(3):
        print(
            "| " + board[i * 3] +
            " | " + board[i * 3 + 1] +
            " | " + board[i * 3 + 2] + " |"
        )
        print("-------------")


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def board_full():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def ai_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number from 1 to 9.")
                continue

            position = move - 1

            if board[position] != " ":
                print("That position is already occupied.")
                continue

            board[position] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")


print("================================")
print("       TIC-TAC-TOE AI")
print("================================")
print()
print("You are X.")
print("AI is O.")
print()
print("Board positions:")
print()
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

while True:

    print_board()

    human_move()

    if check_winner("X"):
        print_board()
        print("\nCongratulations! You won!")
        break

    if board_full():
        print_board()
        print("\nThe game is a draw!")
        break

    print("\nAI is thinking...")
    ai_move()

    if check_winner("O"):
        print_board()
        print("\nAI wins! Better luck next time.")
        break

    if board_full():
        print_board()
        print("\nThe game is a draw!")
        break