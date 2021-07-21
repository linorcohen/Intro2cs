#################################################################
# FILE : lab4.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse lab4 2021
# DESCRIPTION: A simple program that operates the game Nim.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################


def init_board():
    """
    This function set the board game.
    :return: list of numbers in ascending order
    :rtype: list of int
    """
    return [i for i in range(1, 7)]


def get_next_player(player):
    """
    This function prints the current player, and returns the next player.
    :param player: the current player value
    :type player: str
    :return: the next player
    :rtype: str
    """
    print(f'player {player}')
    if player == '1':
        return '2'
    return '1'


def print_board(board):
    """
    This function prints the board game to the screen.
    :param board: list of numbers
    :type board: list of int
    """
    for row in board:
        print(row)


def is_board_empty(board):
    """
    This function checks if the board is empty.
    :param board: list of numbers
    :type board: list of int
    :return: True if the board is empty, else False.
    :rtype: bool
    """
    if sum(board) == 0:
        return True
    return False


def get_input(board):
    """
    This function ask the player to input row number and number of matches,
    check their validity and returns them.
    :param board: list of numbers
    :type board: list of int
    :return: row number, matches number
    :rtype: int, int
    """
    # the code below ask the player to enter a row number, if row number
    # invalid, ask until get a valid input
    row = int(input('Enter row number: '))
    while check_row_number_validity(row, board) is False:
        row = int(input('Enter row number: '))

    # the code below ask the player to enter a matches number, if matches
    # number invalid, ask until get a valid input
    num_matches = int(input('Enter number of matches to remove: '))
    while check_amount_taken(row, num_matches, board) is False:
        num_matches = int(input('Enter number of matches to remove: '))

    return row, num_matches


def check_row_number_validity(row, board):
    """
    This function checks the validity of row.
    :param row: number of row
    :type row: int
    :param board: list of numbers
    :type board: list of int
    :return: True if row is valid, else False.
    :rtype: bool
    """
    if row > len(board) or row <= 0:
        return False
    return True


def check_amount_taken(row, num_matches, board):
    """
    This function checks the validity of the number of matches to remove in
    the row.
    :param row: number of row
    :type row: int
    :param num_matches: number of matches to remove from a row
    :type num_matches: int
    :param board: list of numbers
    :type board: list of int
    :return: True if valid number of matches to remove is valid, else False.
    :rtype: bool
    """
    if num_matches > board[row - 1] or num_matches < 1:
        return False
    return True


def update_board(row, num_matches, board):
    """
    This function update the board game according to the matches to remove
    from a row.
    :param row: number of row
    :type row: int
    :param num_matches: number of matches to remove from a row
    :type num_matches: int
    :param board: list of numbers
    :type board: list of int
    """
    board[row - 1] -= num_matches


def run_game():
    """
    This function runs the game Nim.
    """
    board = init_board()  # initialize the board
    player = '1'
    while not is_board_empty(board):  # until the board is empty
        player = get_next_player(player)  # get the next player
        print_board(board)
        row, num_matches = get_input(board)
        update_board(row, num_matches, board)
    print(f'player {player} Won!')  # determine who win


if __name__ == "__main__":
    run_game()
