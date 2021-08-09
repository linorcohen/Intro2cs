#################################################################
# FILE : wordsearch.py
# WRITER : Linor Cohen , linorcohen
# EXERCISE : intro2cse ex5 2021
# DESCRIPTION: A simple program that finds words in a letters matrix.(Tifzoret)
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: https://stackoverflow.com/questions/4664850/how-to-find-all
# -occurrences-of-a-substring
# NOTES: NONE
#################################################################
import sys
import os.path


INVALID_NUM_OF_PARAMETERS_MASSAGE: str = 'Invalid number of parameters.'
NO_FILE_MASSAGE: str = 'No words file was found.'
ILLEGAL_DIRECTIONS: str = 'Directions contain illegal characters. '


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
        return INVALID_NUM_OF_PARAMETERS_MASSAGE
    if not os.path.isfile(args[0]) or not os.path.isfile(args[1]):
        return NO_FILE_MASSAGE
    if not contain_only_legal_directions(args[3]):
        return ILLEGAL_DIRECTIONS


def contain_only_legal_directions(directions):
    """
    This function checks if the given directions contains only legal directions
    characters.
    :param directions: directions
    :type directions: str
    :return: False if found illegal directions characters, else True.
    :rtype: bool
    """
    legal_directions = {'u', 'd', 'r', 'l', 'w', 'x', 'y', 'z'}
    for char in directions:
        if char not in legal_directions:
            return False
    return True


def read_wordlist(filename):
    """
    This function opens and reads the words file and returns a list of words.
    :param filename: words file path
    :type filename: str
    :return: list of words
    :rtype: list[str]
    """
    with open(filename, 'r') as words_file:
        return [line.strip() for line in words_file.readlines()]


def read_matrix(filename: str):
    """
    This function opens and reads the matrix file and returns a 2D list of the
    matrix letters.
    :param filename: matrix file path
    :type filename: str
    :return: matrix
    :rtype: list[list[str]]
    """
    with open(filename, 'r') as matrix_file:
        return [line.strip().split(',') for line in matrix_file.readlines()]


def find_words(word_list, matrix, directions):
    """
    This function search and counts the number of words from the words list
    found in the matrix according to the directions given and returns them in a
    list of couples (word, count) where word is a word that appears in the
    matrix, and count is the times the same word was found.
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
        directions_lst = return_list_according_to_directions(direction, matrix)
        count_words(directions_lst, word_list, words_count_dict)
    # convert dictionary to list of tuples:
    return [(word, count) for word, count in words_count_dict.items()]


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
        return create_up_direction_list(matrix)
    if direction == 'd':  # ↓
        return create_down_direction_list(matrix)
    if direction == 'r':  # →
        return create_right_direction_list(matrix)
    if direction == 'l':  # ←
        return create_left_direction_list(matrix)
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
        return create_diagonal_raise_direction_list(columns, matrix,
                                                    columns_direction)
    if direction == 'z':  # ↙
        columns_direction = list(range(columns))
        return create_diagonal_descend_direction_list(columns, matrix,
                                                      columns_direction)
    if direction == 'x':   # ↖
        columns_direction = list(reversed(range(columns)))  # [..., 3, 2, 1, 0]
        return create_diagonal_raise_direction_list(columns, matrix,
                                                    columns_direction)
    if direction == 'y':  # ↘
        columns_direction = list(reversed(range(columns)))
        return create_diagonal_descend_direction_list(columns, matrix,
                                                      columns_direction)


def create_diagonal_raise_direction_list(columns, matrix, columns_direction):
    """
    This function returns a list of organized matrix lines joined in the
    direction of diagonal raise left or right according to columns_direction.
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
    number_of_diagonals = rows + columns - 1
    diagonal_matrix = ['' for i in range(number_of_diagonals)]
    # the code below runs on all the columns in the matrix and adds the letters
    # to diagonal_matrix for the right diagonal they belong:
    curr_index = 0   # current index in diagonal_matrix
    for column in columns_direction:
        # start adding letters from rows of that column to diagonal_matrix:
        curr_add_index = curr_index
        for row in range(rows):
            diagonal_matrix[curr_add_index] += (matrix[row][column])
            curr_add_index += 1
        curr_index += 1  # go to next index in diagonal_matrix for next column

    return diagonal_matrix


def create_diagonal_descend_direction_list(columns, matrix, columns_direction):
    """
    This function returns a list of organized matrix lines joined in the
    direction of diagonal descend left or right according to columns_direction.
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
    return [string[::-1] for string in
            create_diagonal_raise_direction_list(columns, matrix,
                                                 columns_direction)]


def create_up_direction_list(matrix):  # ↑
    """
    This function returns a list of organized matrix lines joined in the
    up direction.
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :return: a list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]
    # [4,5,6] ---> ['741', '852', '963']
    # [7,8,9]
    return [''.join([row[i] for row in matrix[::-1]]) for i in
            range(len(matrix[0]))]


def create_down_direction_list(matrix):  # ↓
    """
    This function returns a list of organized matrix lines joined in the
    down direction.
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :return: a list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]
    # [4,5,6] ---> ['147', '258', '369']
    # [7,8,9]
    return [''.join([row[i] for row in matrix]) for i in range(len(matrix[0]))]


def create_right_direction_list(matrix):  # →
    """
    This function returns a list of organized matrix lines joined in the
    right direction.
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :return: a list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]
    # [4,5,6] ---> ['123', '456', '789']
    # [7,8,9]
    return [''.join(lst) for lst in matrix]


def create_left_direction_list(matrix):  # ←
    """
    This function returns a list of organized matrix lines joined in the
    left direction.
    :param matrix: 2D list of the matrix letters
    :type matrix: list[list[str]]
    :return: a list of organized matrix lines joined
    :rtype: list[str]
    """
    # [1,2,3]
    # [4,5,6] ---> ['321', '654', '987']
    # [7,8,9]
    return [''.join(lst[::-1]) for lst in matrix]


def count_words(lines_lst, words_lst, words_count_dict):
    """
    This function get a list of matrix lines joined and counts the number of
    times a word from the words list is shown, and updates the dictionary.
    :param lines_lst: list of matrix lines joined
    :type lines_lst: list[str]
    :param words_lst: list of words
    :type words_lst: list[str]
    :param words_count_dict: dictionary that stores the words and their counts
    :type words_count_dict: dict[str,int]
    """
    for word in words_lst:
        for line in lines_lst:
            count = len(
                [i for i in range(len(line)) if line.startswith(word, i)])
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
    Gets list of args [word_file, matrix_file, output_file, directions],
    search words in matrix according to the directions and write the results
    to a file.
    :param args: list of args
    :type args: list[str]
    """
    if check_input_args(args) is not None:
        print(check_input_args(args))
        return
    words_file = args[0]
    matrix_file = args[1]
    output_file = args[2]
    directions = args[3]
    words_lst = read_wordlist(words_file)
    matrix = read_matrix(matrix_file)
    found_words_lst = find_words(words_lst, matrix, directions)
    write_output(found_words_lst, output_file)


if __name__ == '__main__':
    main(sys.argv[1:])
