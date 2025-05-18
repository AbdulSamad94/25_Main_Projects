def Tic_Tac_Toe():
    board = [' ' for _ in range(9)]
    current_player = "X"
    condiion = True
    def show_board():
        print(f"\n{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    def winning_conditions():
        wining_combinaions = [
            (0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)
        ]
        for i in wining_combinaions:
            if board[i[0]] == board[i[1]] == board[i[2]] != ' ':
                return True
           
        return False
            
    def is_board_full():
        return ' ' not in board
    
    while condiion:
        show_board()
        choice = int(input(f"Player {current_player}, Enter your number between 1-9 according to the pattern: ")) - 1

        if(board[choice] == ' '):
            board[choice] = current_player
            if winning_conditions():
                show_board()
                print(f"\n{current_player} Wins!")
                break
            elif is_board_full():
                show_board()
                print("It's a Tie")
                break
            else:
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"
        

if __name__ == "__main__":
    Tic_Tac_Toe()