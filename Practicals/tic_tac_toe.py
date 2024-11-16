
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_patterns = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6]   # Diagonal 2
    ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False
def check_draw(board):
    return all(space != ' ' for space in board)

def play_game():
    board = [' ' for _ in range(9)] 
    current_player = 'X'  
    game_over = False

    while not game_over:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        move = int(input(f"Enter a position (1-9) to place {current_player}: ")) - 1

        if 0 <= move < 9 and board[move] == ' ':
            board[move] = current_player
        else:
            print("Invalid move. Please try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'


play_game()
