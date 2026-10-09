from termcolor import colored, cprint


def cell(mark: str):
    if mark == "X":
        return colored(mark, "red")
    else:
        return colored(mark, "green")


def print_with_spaces(value: str, spaces=10):
    indent = " " * spaces
    print(indent + value)


def print_cell_with_spaces(col_num: int, value: str):
    indent = " " * 7
    print(indent + f" {col_num} " + value)


def print_board(board: list):
    column_headers = " 0   1   2 "
    line = "---+---+---"
    print_with_spaces(column_headers)
    print_with_spaces(line)
    for idx, row in enumerate(board):
        print(" " * 7 + f" {idx} ", end="")
        cprint(f" {cell(row[0])} | {cell(row[1])} | {cell(row[2])} ")
        print_with_spaces(line)


def update_board(board: list, current_player: str, move: tuple[int, int]):
    board[move[0]][move[1]] = current_player


def get_move(board: list, current_player: str):
    print(f"Player {current_player}'s turn.")
    while True:
        row = get_position("Enter row number[0-2]: ")
        column = get_position("Enter column number[0-2]: ")

        if board[row][column] == " ":
            return row, column

        print("This position is already taken. Try again.")


def get_position(prompt: str):
    while True:
        try:
            position = int(input(prompt))
            if position < 0 or position > 2:
                raise ValueError
            return position
        except ValueError:
            print("Invalid input. Try again.")


def check_winner(board: list):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != " ":
            return True

    # check diagonal
    if (
        board[0][0] == board[1][1] == board[2][2] != " "
        or board[0][2] == board[1][1] == board[2][0] != " "
    ):
        return True

    return False


def is_full(board: list):
    for row in board:
        if " " in row:
            return False
    return True


# Declare the game board
# Print the board
# Select current player
# Start game loop
#   Get current player move
#   Mark the board with current player move
#   Check the winner
#       If winner, declare winner and break loop
#   Check if board is full
#       If full, print message and break


def main():
    print(colored("X", "green"))
    game_board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    print_board(game_board)
    current_player = "X"
    while True:
        move = get_move(game_board, current_player)
        update_board(game_board, current_player, move)
        print_board(game_board)

        if check_winner(game_board):
            print(f"Player {current_player} wins!")
            break

        if is_full(game_board):
            print("Game Over! Board is full!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
