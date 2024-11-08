import random

def initialize_game():
    print("Welcome to Sudoku!")
    print("Select difficulty level:")
    print("1. Very Easy (20x20)")
    print("2. Easy (35x35)")
    print("3. Intermediate (50x50)")
    print("4. Hard (60x60)")
    print("5. Very Hard (75x75)")
    
    difficulty_levels = {
        1: 20,
        2: 35,
        3: 50,
        4: 60,
        5: 75
    }
    
    try:
        difficulty = int(input("Enter difficulty level (1-5): "))
        grid_size = difficulty_levels[difficulty]
    except (ValueError, KeyError):
        print("Invalid choice. Defaulting to 'Very Easy' with a 20x20 grid.")
        grid_size = 20
    
    return grid_size

def generate_board(grid_size):
    board = [[0] * grid_size for _ in range(grid_size)]
    for _ in range(int(grid_size * 1.5)):
        row = random.randint(0, grid_size - 1)
        col = random.randint(0, grid_size - 1)
        num = random.randint(1, grid_size)
        board[row][col] = num
    return board

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in (board[i][col] for i in range(len(board))):
        return False
    
    grid_size = int(len(board) ** 0.5)
    start_row, start_col = row - row % grid_size, col - col % grid_size
    for i in range(grid_size):
        for j in range(grid_size):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def player_move(board):
    try:
        row = int(input("Enter row (1-{}): ".format(len(board)))) - 1
        col = int(input("Enter column (1-{}): ".format(len(board)))) - 1
        num = int(input("Enter number (1-{}): ".format(len(board))))
        
        if is_valid(board, row, col, num):
            board[row][col] = num
            print("Number added successfully!")
        else:
            print("Invalid move. Try again.")
    except ValueError:
        print("Invalid input. Enter numbers only.")

def start_game():
    grid_size = initialize_game()
    board = generate_board(grid_size)
    
    print("\nStarting your Sudoku game!")
    print_board(board)
    
    while True:
        player_move(board)
        print_board(board)


start_game()
