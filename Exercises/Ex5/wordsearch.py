import sys
from typing import List, Dict, Tuple, Set, Optional
import os.path
import copy


INVALID_NUM_MASSAGE: str = 'Invalid number of parameters.'
NO_FILE_MASSAGE: str = 'No words file was found.'
ILLEGAL_DIRECTIONS: str = 'Directions contain illegal characters. '
DIRECTIONS: Set[str] = {'u', 'd', 'r', 'l', 'w', 'x', 'y', 'z'}


def check_input_args(args):
    """
    This function checks if the input arguments are valid to use.
    if not valid - returns an informative massage accordingly.
    if valid - returns None.
    :param args: list of arguments
    :type args: list[str]
    :return: massage, else None.
    :rtype: str or None
    """
    if len(args) != 4:
        return INVALID_NUM_MASSAGE
    if not os.path.isfile(args[0]) or not os.path.isfile(args[1]):
        return NO_FILE_MASSAGE
    if not contain_only_legal_directions(args[3]):
        return ILLEGAL_DIRECTIONS


def contain_only_legal_directions(directions):
    """
    This function checks if the directions contains only legal directions.
    :param directions: matrix search directions
    :type directions: str
    :return: False if found illegal directions, else True.
    :rtype: bool
    """
    for i in directions:
        if i not in DIRECTIONS:
            return False
    return True


def read_wordlist(filename):
    """
    This function open and reads the words file and returns a list of words.
    :param filename: words file path
    :type filename: str
    :return: list of words
    :rtype: list[str]
    """
    with open(filename, 'r') as words_file:
        return [line.strip() for line in words_file.readlines()]


def read_matrix(filename: str):
    """
    This function open and reads the matrix file and returns a list of lists
    of letters.
    :param filename: matrix file path
    :type filename: str
    :return: 2D list of the matrix letters
    :rtype: list[list[str]]
    """
    with open(filename, 'r') as words_file:
        return [line.strip().split(',') for line in words_file.readlines()]


def find_words(word_list, matrix, directions):
    """
    This function search and counts the number of words is the matrix according
    to the directions given and returns them in a list of couples (word, count)
    where word is a word that appears in the matrix, and count is the times the
    same word was found.
    :param word_list: list of words
    :type word_list: list[str]
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :param directions: directions to search through
    :type directions: str
    :return: list of couples (word, count)
    :rtype: list[tuple[str,int]]
    """
    if len(word_list) == 0 or len(matrix) == 0:
        return []  # in case of empty matrix or words list
    words_count_dict = {}
    for direction in set(directions):
        matrix_copy = copy.deepcopy(matrix)  # so we won't change the original matrix
        directions_lst = return_list_according_to_directions(direction, matrix_copy)
        count_words(directions_lst, word_list, words_count_dict)
    # convert dictionary to list of tuples:
    return [(k, v) for k, v in words_count_dict.items()]


def return_list_according_to_directions(direction, matrix):
    """
    This function checks the direction of the search and returns a list of
    organized matrix lines joined according to that direction.
    :param direction: direction to search through
    :type direction: str
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :return: list of organized matrix lines joined
    :rtype: list[str]
    """
    if direction == 'u':  # ↑
        return up(matrix)
    if direction == 'd':  # ↓
        return down(matrix)
    if direction == 'r':  # →
        return right(matrix)
    if direction == 'l':  # ←
        return left(matrix)
    return diagonal_search(matrix, direction)  # in case of diagonal direction


def diagonal_search(matrix, direction):
    """
    This function checks the direction of diagonal search and returns a list of
    organized matrix lines joined according to that diagonal direction.
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :param direction: diagonal direction to search through
    :type direction: str
    :return: list of organized matrix lines joined
    :rtype: list[str]
    """
    columns = len(matrix[0])
    if direction == 'w':  # ↗
        columns_direction = list(range(columns))  # [0, 1, 2, 3, ...]
        return diagonal_raise(columns, matrix, columns_direction)
    if direction == 'z':  # ↙
        columns_direction = list(range(columns))
        return diagonal_descends(columns, matrix, columns_direction)
    if direction == 'x':   # ↖
        columns_direction = list(reversed(range(columns)))  # [..., 3, 2, 1, 0]
        return diagonal_raise(columns, matrix, columns_direction)
    if direction == 'y':  # ↘
        columns_direction = list(reversed(range(columns)))
        return diagonal_descends(columns, matrix, columns_direction)


def diagonal_raise(columns, matrix, columns_direction):
    """
    This function returns a list of organized matrix lines joined in the
    direction of diagonal raise left or right according to the columns_direction.
    :param columns: number of columns in matrix
    :type columns: int
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :param columns_direction: list of columns direction
    :type columns_direction: list[int]
    :return: list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]      rise right                  rise left
    # [4,5,6] ---> ['1','42','753','86','9'] / ['3','62','951','84','7']
    # [7,8,9]
    rows = len(matrix)
    diagonal_matrix = [[] for i in range(rows + columns - 1)]
    diagonal_matrix_index = 0
    for i in columns_direction:
        m = diagonal_matrix_index
        for j in range(rows):
            diagonal_matrix[m].append(matrix[j][i])
            m += 1
        diagonal_matrix_index += 1
    return [''.join(lst) for lst in diagonal_matrix]


def diagonal_descends(columns, matrix, columns_direction):
    """
    This function returns a list of organized matrix lines joined in the
    direction of diagonal descend left or right according to the columns_direction.
    :param columns: number of columns in matrix
    :type columns: int
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :param columns_direction: list of columns direction
    :type columns_direction: list[int]
    :return: list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]      descend left                descend right
    # [4,5,6] ---> ['1','24','357','68','9'] / ['3','26','159','48','7']
    # [7,8,9]
    return [string[::-1] for string in diagonal_raise(columns, matrix, columns_direction)]


def up(matrix):  # ↑
    """
    This function returns a list of organized matrix lines joined in the up direction.
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :return: a list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]      ['741']
    # [4,5,6] ---> ['852']
    # [7,8,9]      ['963']
    return [''.join([row[i] for row in matrix[::-1]]) for i in range(len(matrix[0]))]


def down(matrix):  # ↓
    """
    This function returns a list of organized matrix lines joined in the down direction.
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :return: a list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]      ['147']
    # [4,5,6] ---> ['258']
    # [7,8,9]      ['369']
    return [''.join([row[i] for row in matrix]) for i in range(len(matrix[0]))]


def right(matrix):  # →
    """
    This function returns a list of organized matrix lines joined in the right direction.
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :return: a list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]      ['123']
    # [4,5,6] ---> ['456']
    # [7,8,9]      ['789']
    return [''.join(lst) for lst in matrix]


def left(matrix):  # ←
    """
    This function returns a list of organized matrix lines joined in the left direction.
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :return: a list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]      ['321']
    # [4,5,6] ---> ['654']
    # [7,8,9]      ['987']
    return [''.join(lst[::-1]) for lst in matrix]


def count_words(lines_lst, words_lst, words_count_dict):
    """
    This function get a list of lines and counts the number of times a word
    from the words list is shown, and then updates the dictionary.
    :param lines_lst: list of matrix lines joined
    :type lines_lst: list[str]
    :param words_lst: list of words
    :type words_lst: list[str]
    :param words_count_dict: dictionary that stores the words and their counts
    :type words_count_dict: dict[str,int]
    """
    for word in words_lst:
        for line in lines_lst:
            count = len([i for i in range(len(line)) if line.startswith(word, i)])
            if count > 0:
                if word in words_count_dict:
                    words_count_dict[word] += count
                else:
                    words_count_dict[word] = count


def write_output(results, filename):
    """
    This function write to file the results of the words search in the matrix.
    :param results: list of couples of (word, count)
    :type results: list[tuple[str,int]]
    :param filename: file path to write the results to
    :type filename: str
    """
    with open(filename, 'w') as output_file:
        for couple in results:
            output_file.write(couple[0]+','+str(couple[1])+'\n')


def main(args):
    """
    This function gets list of args [word_file, matrix_file, output_file, directions],
    search words in matrix according to the directions and write
    the results to a file.
    :param args: list of args
    :type args: list[str]
    """
    if check_input_args(args) is not None:
        print(check_input_args(args))
        return
    words_lst = read_wordlist(args[0])
    matrix = read_matrix(args[1])
    found_words_lst = find_words(words_lst, matrix, args[3])
    write_output(found_words_lst, args[2])


if __name__ == '__main__':
    main(sys.argv[1:])
