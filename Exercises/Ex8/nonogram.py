#################################################################
# FILE : nonogram.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex8 2021
# DESCRIPTION: A simple program that to solves nonogram.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
import copy


# comment for intersection_row():
# while checking the rows if the current place im checking is colored 1 or 0:
# if the main row i'm compering is -1 , set the main row to that color and
# continue to check the other rows in te same place but:
# once my function find a conflict between the main row i'm checking -
# my main row has 1 or 0 and the row im currently checking has a 0 or 1
# (opposite) - I determine the main row current place to be -1 and move
# to the next place ( without checking the other rows)
# i decided that method so i can place a color that matched all the rows
# until i find a conflict, and if so i place -1 and continue,
# if not i prefer to have a color there.


def constraint_satisfactions(n, blocks):
    """
    This function gets the parameter n which represent the row length and
    blocks constraints list, and returns all color options of row with length
    of n.
    :param n: length of row
    :type n: int
    :param blocks: block sizes in the row in order
    :type blocks: list[int]
    :return: list of all possible coloring in lenght of n with values 0 or 1
    according to the list of constraints blocks.
    :rtype: list[list[int]]
    """
    row = [0 for i in range(n)]
    possible_rows = []
    _constraint_satisfactions_helper(n, blocks, row, possible_rows, 0, 0)
    return possible_rows


def _constraint_satisfactions_helper(n, blocks, row, possible_rows, index,
                                     blocks_index):
    """
    Helper function for the function constraint_satisfactions():
    find all color options of row with length of n according to the blocks
    given, in a recursive way.
    :param n: length of row
    :type n: int
    :param blocks: block sizes in the row in order
    :type blocks: list[int]
    :param row: initial row fill with 0
    :type row: list[int]
    :param possible_rows: list of possible rows
    :type possible_rows: list[list[int]]
    :param index: next index to search from
    :type index: int
    :param blocks_index: current block index
    :type blocks_index: int
    """
    if sum(row) == sum(blocks):
        possible_rows.append(row[:])
        return

    for i in range(index, n):
        if i > n - blocks[blocks_index]:   # if cant input any more blocks:
            continue
        if is_valid_to_place(row, i):
            row = place_color_according_to_block(row, blocks[blocks_index], i,
                                                 1)
            _constraint_satisfactions_helper(n, blocks, row, possible_rows, i,
                                             blocks_index + 1)
            row = place_color_according_to_block(row, blocks[blocks_index], i,
                                                 0)


def place_color_according_to_block(row, block, i, color):
    """
    This function color (1 or 0) the current row according to the color given
    and the block given.
    :param row: initial row fill with 0
    :type row: list[int]
    :param block: amount of color
    :type block: int
    :param i: index to color from in the row
    :type i: int
    :param color: what to color (1 or 0)
    :type color: int
    :return: row after color
    :rtype: list[int]
    """
    for j in range(block):
        row[i] = color
        i += 1
    return row


def is_valid_to_place(row, index):
    """
    This function determine if its valid to input a color in the current index.
    :param row: initial row fill with 0
    :type row: list[int]
    :param index: current index
    :type index: int
    :return: True if valid to place, else False.
    :rtype: bool
    """
    if row[index] == 1 or 0 < index and row[index-1] == 1 \
            or index < len(row)-1 and row[index+1] == 1:
        return False
    return True


def row_variations(row, blocks):
    """
    This function receives a given row in the board and a list of constraints
    (a list of block sizes) and returns a list of all the options for
    completing the line coloring so that the coloring will meet the constraints
    :param row: list of partial coloring of a row (list with values (1, -0, 1)
    :type row: list[int]
    :param blocks: block sizes in the row in order
    :type blocks: list[int]
    :return: list of all options for coloring the row
    :rtype: list[list[int]]
    """
    variations = []
    _row_variations_helper(row, blocks, variations, [], 0, 0)
    return variations[::-1]


def _row_variations_helper(row, blocks, variations, temp_lst, row_index,
                           block_index):
    """
    Helper function for the function row_variations():
    This function find in a recursive way all the possible options to color the
    partial row with the givem blocks.
    :param row: list of partial coloring of a row (list with values (1, -0, 1)
    :type row: list[int]
    :param blocks: block sizes in the row in order
    :type blocks: list[int]
    :param variations: all possible variations to color the row
    :type variations: list[list[int]]
    :param temp_lst: temporary row
    :type temp_lst: list[int]
    :param row_index: current row index
    :type row_index: int
    :param block_index: current block index
    :type block_index: int
    """
    if row_index >= len(row):
        if block_index >= len(blocks):
            variations.append(temp_lst[:])
        return

    if row[row_index] == 0 or row[row_index] == -1:
        temp_lst.append(0)
        _row_variations_helper(row, blocks, variations, temp_lst,
                               row_index + 1, block_index)
        temp_lst.pop()

    if (row[row_index] == -1 or row[row_index] == 1) and block_index < len(
            blocks) and row_index <= len(row) - blocks[block_index]:
        #  check current sequence validity to continue:
        is_last_block, is_valid = is_sequence_valid(block_index, blocks, row,
                                                    row_index)

        if is_valid:
            add_sequence(block_index, blocks, is_last_block, temp_lst)

            # determine the next index:
            next_index = row_index + blocks[
                block_index] if is_last_block else row_index + blocks[
                block_index] + 1
            _row_variations_helper(row, blocks, variations, temp_lst,
                                   next_index, block_index + 1)

            remove_sequence(block_index, blocks, is_last_block, temp_lst)


def remove_sequence(block_index, blocks, is_last_block, temp_lst):
    """
    This function remove all the coloring frpm temp_lst according to the
    current block.
    :param block_index: current block index
    :type block_index: int
    :param blocks: block sizes in the row in order
    :type blocks: list[int]
    :param is_last_block: determine if last block
    :type is_last_block: bool
    :param temp_lst: temporary row
    :type temp_lst: list[int]
    """
    for i in range(0, blocks[block_index]):
        temp_lst.pop()
    if not is_last_block:
        temp_lst.pop()


def add_sequence(block_index, blocks, is_last_block, temp_lst):
    """
    This function add all the coloring to temp_lst according to the current
    block.
    :param block_index: current block index
    :type block_index: int
    :param blocks: block sizes in the row in order
    :type blocks: list[int]
    :param is_last_block: determine if last block
    :type is_last_block: bool
    :param temp_lst: temporary row
    :type temp_lst: list[int]
    """
    for i in range(0, blocks[block_index]):
        temp_lst.append(1)
    if not is_last_block:
        temp_lst.append(0)


def is_sequence_valid(block_index, blocks, row, row_index):
    """
    This function checks if the current sequence is valid to continue,
    and check if its the last row.
    :param block_index: current block index
    :type block_index: int
    :param blocks: block sizes in the row in order
    :type blocks: list[int]
    :param row: list of partial coloring of a row (list with values (1, -0, 1)
    :type row: list[int]
    :param row_index: current row index
    :type row_index: int
    :return: if is last block, if is valid to continue.
    :rtype: bool
    """
    is_valid = True
    for i in range(row_index, row_index + blocks[block_index]):
        if row[i] == 0:
            is_valid = False
            break

    is_last_block = block_index == len(blocks) - 1
    # if not last block - check again if its valid to continue:
    if not is_last_block:
        if row_index > len(row) - (blocks[block_index] + 1) or \
                row[row_index + blocks[block_index]] == 1:
            is_valid = False

    return is_last_block, is_valid


def intersection_row(rows):
    """
    This function gets a list of rows and returns the combine lines of them all
    meaning - a row in which (1 or 0) is painted only if each row in the
    given rows is painted like that, the rest are neutral( with -1)
    :param rows: a list of rows in the same length.
    :type rows: list[list[int]]
    :return: a row that comine all the given rows.
    :rtype: list[int]
    """
    if len(rows) == 0:
        return rows

    result = rows[0][:]  # check rows according to the first row in them
    for index in range(len(result)):
        for row in rows[1:]:
            if row[index] == result[index] and result[index] != -1 or \
                    result[index] != row[index] and row[index] == -1:
                continue
            if row[index] != result[index] and result[index] == -1:
                result[index] = row[index]
                continue
            result[index] = -1  # set -1 for when we have a conflict in place
            break  # found a conflict no need to check the other rows place
    return result


def solve_easy_nonogram(constraints):
    """
    This function gets a nonogram board constraints and return a solved board.
    if can't solver all the  board - returns it as is it ( not finished).
    if can't solve the board at all returns None.
    :param constraints: nonogram board constraints
    :type constraints: list[list[list[int]]]
    :return: solved board
    :rtype: list[list[int]]
    """
    board = []
    is_board_valid = build_board_with_rows(board, constraints)
    if is_board_valid is False:
        return
    filled_rows = []
    filled_cols = []
    changed_state = True
    while changed_state:
        # check columns and set the changed:
        is_board_valid = check_columns(board, filled_rows, constraints[1])
        if is_board_valid is False:
            return
        board_copy = copy.deepcopy(board)  # copy board to see if changed after
        #  changed board rows:
        is_board_valid = check_current_rows_in_board(board, filled_cols,
                                                     constraints[0])
        if is_board_valid is False:
            return
        #  check if board was changed:
        changed_state = check_board_changed_status(board_copy, board)
    return board


def check_board_changed_status(before_board, after_board):
    """
    This function checks if the board was changed.
    :param before_board: board before the rows change.
    :type before_board: list[list[int]]
    :param after_board: board after the rows change
    :type after_board: list[list[int]]
    :return: True if changed,else False
    :rtype: bool
    """
    if before_board == after_board:
        return False
    return True


def check_current_rows_in_board(rows_to_check, filled, constraints):
    """
    This function checks if its valid to input a new row to the
    board, if so, add the intrensection of that row to board. if invalid stops
    the check and returns False. else, returns True.
    :param rows_to_check: rows from board to check
    :type rows_to_check: list[list[int]]
    :param filled: list of already filled rows that dont need to check/change
    :type filled: list[int]
    :param constraints: current constraints
    :type constraints: list[list[int]]
    :return: True if all changed and was valid, else False.
    :rtype: bool
    """
    for row in range(len(rows_to_check)):
        if row in filled:
            continue
        variations = row_variations(rows_to_check[row], constraints[row])
        if not variations:  # if cant find a variations the board is invalid
            return False
        if len(variations) == 1:
            rows_to_check[row] = variations[0]
            filled.append(row)
            continue
        rows_to_check[row] = intersection_row(variations)
    return True


def check_columns(board, filled, columns_constraints):
    """
    This function checks the columns in board.
    :param board: the current board
    :type board: list[list[int]]
    :param filled: list of already filled rows that dont need to check/change
    :type filled: list[int]
    :param columns_constraints: columns constraints
    :type columns_constraints: list[list[int]]
    :return: True if all changed and was valid, else False.
    :rtype: bool
    """
    # collect the columns from the board:
    columns_as_rows = [[row[i] for row in board] for i in range(len(board[0]))]
    value = check_current_rows_in_board(columns_as_rows, filled,
                                        columns_constraints)
    # set the new columns to the board:
    set_columns_to_board(board, columns_as_rows)
    return value


def set_columns_to_board(board, columns):
    """
    This function set the changed columns back to the current board.
    :param board: the current board
    :type board: list[list[int]]
    :param columns: given columns after changed
    :type columns: list[list[int]]
    """
    for i in range(len(board[0])):
        for row in range(len(board)):
            board[row][i] = columns[i][row]


def build_board_with_rows(board, constraints):
    """
    This function build the initial board of the game according to the rows
    constraints, and check if can build the board.
    :param board: an empty list that represent the board.
    :type board: list
    :param constraints: the constraints
    :type constraints: list[list[list[int]]]
    :return: True if can build a board, else False.
    :rtype: bool
    """
    for row in constraints[0]:
        row_constraint = constraint_satisfactions(len(constraints[1]), row)
        #  cant build board if row does not have row_constraint
        if not row_constraint:
            return False
        if len(row_constraint) == 1:
            board.append(row_constraint[0])
            continue
        row_intersection = intersection_row(row_constraint)
        board.append(row_intersection)
    return True


def solve_nonogram(constraints):
    """
    This function solves the nonogram based on the given constraints.
    :param constraints: nonogram board constraints
    :type constraints: list[list[list[int]]]
    :return: list of all possible solutions for the game.
    :rtype: list[list[int]]
    """
    board_options = []
    initial_board = solve_easy_nonogram(constraints)
    _solve_nonogram_helper(constraints[0], constraints[1], initial_board, 0,
                           board_options)
    return board_options


def _solve_nonogram_helper(rows_constraints, col_constraints, board, row_index
                           , board_options):
    """
    Helper function for the function solve_nonogram():
    This function finds in a recursive way all the possible solutions for the
    nonogram game.
    :param rows_constraints: rows constraints
    :type rows_constraints: list[list[int]]
    :param col_constraints: columns constraints
    :type col_constraints: list[list[int]]
    :param board: current board
    :type board: list[list[int]]
    :param row_index: current row index
    :type row_index: int
    :param board_options: all possible solutions for board
    :type board_options: list[list[list[int]]]
    """
    if row_index == len(col_constraints) and \
            check_columns_in_board(col_constraints, board):
        board_options.append(copy.deepcopy(board))
        return

    if row_index < len(rows_constraints):
        row_options = row_variations(board[row_index],
                                     rows_constraints[row_index])

        option_board = copy.deepcopy(board)
        for row in row_options:
            option_board[row_index] = row

            _solve_nonogram_helper(rows_constraints, col_constraints,
                                   option_board, row_index + 1,
                                   board_options)

        option_board[row_index] = board[row_index]


def check_columns_in_board(col_constraints, board):
    """
    This function checks the current board by checking if all columns
    constraints are valid. if valid return True, else False.
    :param col_constraints: columns constraints
    :type col_constraints: list[list[int]]
    :param board: current board
    :type board: list[list[int]]
    :return: True if board is valid, else False.
    :rtype: bool
    """
    for i in range(len(col_constraints)):
        curr_column = [row[i] for row in board]
        checked_column = row_variations(curr_column, col_constraints[i])
        #  if row_variations didnt find any possible variation:
        if not checked_column:
            return False
    return True















