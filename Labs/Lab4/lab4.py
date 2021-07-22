#################################################################
# FILE : lab4.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse lab4 2021
# DESCRIPTION: A simple program that operates the game Nim.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################

BOARD_ROWS = 5


def init_board():
    """
    This function creates the board game.
    :return: list of numbers in ascending order
    :rtype: list of int
    """
    return [i+1 for i in range(0, BOARD_ROWS)]


def get_next_player(player):
    """
    This function returns the next player.
    :param player: the current player value
    :type player: str
    :return: the next player
    :rtype: str
    """
    if player == '1':
        return '2'
    return '1'


def print_board(board):
    """
    This function prints the board game to the screen.
    :param board: list of numbers
    :type board: list of int
    """
    print('--- Board ---')
    for row in range(len(board)):
        print(f'{row+1}: {board[row] *"*"}')
    print('-------------')


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
    and returns them.
    :param board: list of numbers
    :type board: list of int
    :return: row number, matches number
    :rtype: (int, int)
    """
    row = get_row_input(board)
    num_matches = get_matches_to_remove_input(row, board)
    return row, num_matches


def get_row_input(board):
    """
    This function ask the player to enter a row number, check their validity
    if row number invalid, ask until get a valid input.
    :param board: list of numbers
    :type board: list of int
    :return: row number
    :rtype: int
    """
    row = int(input('Enter row number: '))
    while check_row_number_validity(row, board) is False:
        print('illegal row number')
        row = int(input('Enter row number: '))
    return row


def get_matches_to_remove_input(row, board):
    """
    This function ask the player to enter a matches number, check their
    validity if matches number invalid, ask until get a valid input.
    :param row: number of row
    :type row: int
    :param board: list of numbers
    :type board: list of int
    :return: matches number
    :rtype: int
    """
    num_matches = int(input('Enter number of matches to remove: '))
    while check_amount_taken(row, num_matches, board) is False:
        print('illegal matches number')
        num_matches = int(input('Enter number of matches to remove: '))
    return num_matches


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
    if row > len(board) or row <= 0 or board[row - 1] == 0:
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
    :return: True if number of matches to remove is valid, else False.
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
    player = '2'
    while is_board_empty(board) is False:  # until the board is empty
        player = get_next_player(player)  # get the next player
        print(f'player {player} turn:')
        print_board(board)
        row, num_matches = get_input(board)
        update_board(row, num_matches, board)
    print(f'player {player} Won!')  # determine who win


if __name__ == "__main__":
    run_game()
