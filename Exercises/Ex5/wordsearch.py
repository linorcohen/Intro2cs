import sys
from typing import List, Dict, Tuple, Set, Optional
import os.path
import copy


INVALID_NUM_MASSAGE: str = 'Invalid number of parameters.'
NO_FILE_MASSAGE: str = 'No words file was found.'
ILLEGAL_DIRECTIONS: str = 'Directions contain illegal characters. '
DIRECTIONS: Set[str] = {'u', 'd', 'r', 'l', 'w', 'x', 'y', 'z'}


def check_input_args(args: List[str]) -> Optional[str]:
    if len(args) != 4:
        return INVALID_NUM_MASSAGE
    if not os.path.isfile(args[0]) or not os.path.isfile(args[1]):
        return NO_FILE_MASSAGE
    if not contain_only_legal_directions(args[3]):
        return ILLEGAL_DIRECTIONS


def contain_only_legal_directions(directions: str) -> bool:
    for i in directions:
        if i not in DIRECTIONS:
            return False
    return True


def read_wordlist(filename: str) -> List[str]:
    file_content = file_content_list(filename)
    words_lst = [line.strip() for line in file_content]
    return words_lst


def file_content_list(filename: str) -> List[str]:
    with open(filename, 'r') as words_file:
        file_content = words_file.readlines()
        return file_content


def read_matrix(filename: str) -> List[List[str]]:
    file_content = file_content_list(filename)
    matrix = [(line.strip()).split(',') for line in file_content]
    return matrix


def find_words(word_list: List[str], matrix: List[List[str]], directions: str) -> List[Tuple[str, int]]:
    if len(word_list) == 0 or len(matrix) == 0:
        return []
    words_count_dict: Dict[str, int] = {}
    for direction in set(directions):
        matrix_copy = copy.deepcopy(matrix)
        lst = return_list_according_to_directions(direction, matrix_copy)
        count_words(lst, word_list, words_count_dict)
    # convert dictionary to tuple
    return [(k, v) for k, v in words_count_dict.items()]


def return_list_according_to_directions(direction, matrix_copy):
    if direction == 'u':  # ↑
        return up(matrix_copy)
    elif direction == 'd':  # ↓
        return down(matrix_copy)
    elif direction == 'r':  # →
        return right(matrix_copy)
    elif direction == 'l':  # ←
        return left(matrix_copy)
    if direction == 'w':  # ↗
        return diagonal_rise_right(matrix_copy)
    if direction == 'x':  # ↖
        return diagonal_rise_left(matrix_copy)
    if direction == 'y':  # ↘
        return diagonal_descends_right(matrix_copy)
    if direction == 'z':  # ↙
        return diagonal_descends_left(matrix_copy)


#  fix variables name:
def diagonal_rise_left(matrix: List[List[str]]) -> List[str]:  # ↖
    rows = len(matrix)
    columns = len(matrix[0])
    diagonal_matrix = [[] for i in range(rows + columns - 1)]
    n = 0
    for i in reversed(range(columns)):
        m = n
        for j in range(rows):
            diagonal_matrix[m].append(matrix[j][i])
            m += 1
        n += 1
    return [''.join(lst) for lst in diagonal_matrix]


# duplicate code
def diagonal_descends_right(matrix: List[List[str]]) -> List[str]:  # ↘
    return [string[::-1] for string in diagonal_rise_left(matrix)]


def diagonal_rise_right(matrix: List[List[str]]) -> List[str]:  # ↗
    rows = len(matrix)
    columns = len(matrix[0])
    diagonal_left_matrix = [[] for i in range(rows + columns - 1)]
    n = 0
    for i in range(columns):
        m = n
        for j in range(rows):
            diagonal_left_matrix[m].append(matrix[j][i])
            m += 1
        n += 1
    return [''.join(lst) for lst in diagonal_left_matrix]


def diagonal_descends_left(matrix: List[List[str]]) -> List[str]:  # ↙
    return [string[::-1] for string in diagonal_rise_right(matrix)]


def up(matrix: List[List[str]]) -> List[str]:  # ↑
    up_order_matrix = [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]
    return [''.join(lst) for lst in up_order_matrix]


def down(matrix: List[List[str]]) -> List[str]:  # ↓
    down_order_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    return [''.join(lst) for lst in down_order_matrix]


def right(matrix: List[List[str]]) -> List[str]:  # →
    return [''.join(lst) for lst in matrix]


def left(matrix: List[List[str]]) -> List[str]:  # ←
    return [''.join(lst[::-1]) for lst in matrix]


def count_words(strings_lst: List[str], words_lst: List[str], words_count_dict: Dict[str, int]) -> None:
    for word in words_lst:
        for string in strings_lst:
            count = len([i for i in range(len(string)) if string.startswith(word, i)])
            if count > 0:
                if word in words_count_dict:
                    words_count_dict[word] += count
                else:
                    words_count_dict[word] = count


def write_output(results: List[Tuple[str, int]], filename: str) -> None:
    with open(filename, 'w') as output_file:
        for couple in results:
            output_file.write(couple[0]+','+str(couple[1])+'\n')


def main(args) -> None:
    if check_input_args(args) is not None:
        print(check_input_args(args))
        return
    words_lst = read_wordlist(args[0])
    matrix = read_matrix(args[1])
    found_words_lst = find_words(words_lst, matrix, args[3])
    write_output(found_words_lst, args[2])


if __name__ == '__main__':
    main(sys.argv[1:])
