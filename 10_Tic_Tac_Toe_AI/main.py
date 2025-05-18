import random


def print_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def is_board_full(board):
    return " " not in board


def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Invalid move. Try again.")
        except:
            print("Invalid input. Enter a number from 1 to 9.")


def ai_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)


def play_game():
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X'. Computer is 'O'.")

    print_board(board)

    while True:
        # Player move
        move = player_move(board)
        board[move] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("You win! 🎉")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # AI move
        print("Computer's move...")
        move = ai_move(board)
        board[move] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins! 😢")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
