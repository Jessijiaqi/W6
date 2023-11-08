from logic import check_winner


def get_empty_board():
    """
    row_1 = ['O', 'O', 'O']
    row_2 = ['O', 'O', 'O']
    row_3 = ['O', 'O', 'O']

    board = [row_1, row_2, row_3]
    """
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def print_board(board):
    for row in board:
        print(row)  # print will print the variable in a new line


def get_player_input(player_input):
    """
    input:
        row,col
    return:
        row: int -> the index of row
        col: int -> the index of column
    """
    row_col_list = player_input.split(",")  # ["1", "1"]
    row, col = [int(x) for x in row_col_list]  # [1,1]
    return row, col


def switch_player(current_player):
    if current_player == "X":
        return "O"
    return "X"


if __name__ == "__main__":
    current_player = "X"
    board = get_empty_board()  # get a empty board
    winner = None

    while winner is None:
        print_board(board)  # print the board
        player_input = input(f"player {current_player} > ")
        try:
            row, col = get_player_input(player_input)  # ask user input
        except ValueError:
            print("Invalid input, try again\n")
            continue

        if row >= len(board[0]) or col >= len(board):
            print(f"Out of bounds, try again\n")
            continue

        if board[row][col]:
            print(
                f"{row},{col} already has mark {board[row][col]}, please choose another place\n"
            )
            continue

        # mark the board
        board[row][col] = current_player

        # check for winner
        winner = check_winner(board)  # "O", "X" -> break out of the loop

        current_player = switch_player(current_player)
        print("\n")
        # current_player = "X" if current_player == "O" else "O"
    print_board(board)
    print(f"Winner is {winner}")