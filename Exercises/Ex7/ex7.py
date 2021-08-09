#################################################################
# FILE : ex7.py
# WRITER : Linor Cohen , linorcohen, 318861226
# EXERCISE : intro2cse ex7 2021
# DESCRIPTION: A simple program practice recursion.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: https://en.wikipedia.org/wiki/Tower_of_Hanoi
# NOTES: NONE
#################################################################
from typing import Any, List, Tuple

FILL_MOVES = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}


def print_to_n(n: int) -> None:
    """
    This function receives the number n and prints the numbers
    from 1 to n (including n) in ascending order.
    :param n: a number
    :type n: int
    """
    if n < 1:
        return
    print_to_n(n - 1)
    print(n)


def digit_sum(n: int) -> int:
    """
    This function receives the non-negative number n and returns the amount of
    the digits of n.
    :param n: a number
    :type n: int
    :return: sum of the digits of n
    :rtype: int
    """
    if 0 <= n < 10:
        return n
    # n % 10 - returns the leftover digits
    # n - (n % 2)) // 10 - return the first digit from left
    return n % 10 + digit_sum((n - (n % 2)) // 10)


def is_prime(n: int) -> bool:
    """
    This function receives the number n and returns True if n a prime number,
    if not - returns False.
    :param n: a number
    :type n: int
    :return: True if n prime, else False.
    :rtype: bool
    """
    if n <= 1:
        return False
    return not has_divisor_smaller_than(n, n - 1)


def has_divisor_smaller_than(n: int, i: int) -> bool:
    """
    This function checks if a number n has a divisor smaller then him and
    returns True if n has a divisor, if not - returns False.
    :param n: a number
    :type n: int
    :param i: smaller number then n
    :type i: int
    :return: True if n has a divisor, else False
    :rtype: bool
    """
    if i == 1:
        return False
    if n % i == 0:
        return True
    return has_divisor_smaller_than(n, i - 1)


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """
    This function solves the hanoi game: move n disks in order of decreasing
    size from the source rod to one of the other two rods - in order of
    decreasing size, without putting a disk above a smaller one.
    :param hanoi: the graphic game
    :type: any
    :param n: number of disks in the game
    :type n: int
    :param src: the source rod of the disks
    :type: any
    :param dst: the destination rod of the disks
    :type: any
    :param temp: the temporary rod
    :type: any
    """
    if n <= 0:
        return
    _play_hanoi_helper(hanoi, n, (0, 1, 2), (src, temp, dst))


def _play_hanoi_helper(hanoi: Any, n: int, rods: Tuple[int, int, int],
                       hanoi_moves: Tuple[Any, Any, Any]) -> None:
    """
    Helper function for the function play_hanoi():
    This function recursively solves the hanoi game.
    receives rods in positions of - (src, dst, temp) and hanoi_moves that
    operates the graphic game according to the robs number in that position.
    :param hanoi: the graphic game
    :type: any
    :param n: number of disks in the game
    :type n: int
    :param hanoi_moves: graphical moves in the game
    :type hanoi_moves: tuple[any,any,any]
    :param rods: rods in positions of - (src, dst, temp)
    :type rods: tuple[int,int,int]
    """
    if n == 1:
        hanoi.move(hanoi_moves[rods[0]], hanoi_moves[rods[1]])
        return
    # call to the function to solve n - 1 hanoi disks to temporary rod:
    new_rods = rods[0], rods[2], rods[1]  # src -> temp
    _play_hanoi_helper(hanoi, n - 1, new_rods, hanoi_moves)
    # call to the function to move the biggest disk to destination rob:
    _play_hanoi_helper(hanoi, 1, rods, hanoi_moves)  # src -> dst
    # call again to the function to solve n - 1 hanoi disks to destination rob:
    new_rods = rods[2], rods[1], rods[0]  # temp -> dst
    _play_hanoi_helper(hanoi, n - 1, new_rods, hanoi_moves)


def print_sequences(char_list: List[str], n: int) -> None:
    """
    This function receives a list of characters (char_list) and prints all The
    possible combinations in length of n characters from the list.
    :param char_list: a list of characters
    :type char_list: List[str]
    :param n: length of the sequence combinations
    :type n: int
    """
    _print_sequences_helper(char_list, n, [])


def _print_sequences_helper(char_list: List[str], n: int,
                            seq: List[str]) -> None:
    """
    Helper function for the function print_sequences():
    The function finds in a recursive way all the possible combinations
    in length of n characters from the list and prints them.
    :param char_list: a list of characters
    :type char_list: List[str]
    :param n: length of the sequence combinations
    :type n: int
    :param seq: current sequence list
    :type seq: List[str]
    """
    if len(seq) == n:
        print(''.join(seq))
        return

    for letter in char_list:
        seq.append(letter)
        _print_sequences_helper(char_list, n, seq)
        seq.pop()


def print_no_repetition_sequences(char_list: List[str], n: int) -> None:
    """
    This function receives a list of characters (char_list) and prints all
    possible combinations in length of n characters from the list, without
    repetitions (same character can't appear more than once in the sequence).
    :param char_list: a list of characters
    :type char_list: List[str]
    :param n: length of the sequence combinations
    :type n: int
    """
    _print_no_repetition_sequences(char_list, n, [])


def _print_no_repetition_sequences(char_list: List[str], n: int,
                                   seq: List[str]) -> None:
    """
    Helper function for the function print_no_repetition_sequences():
    The function finds in a recursive way all the possible combinations in
    length of n characters from  the list, without repetitions of characters in
    a sequence, and prints them.
    :param char_list: a list of characters
    :type char_list: List[str]
    :param n: length of the sequence combinations
    :type n: int
    :param seq: current sequence of combination list
    :type seq: List[str]
    """
    if len(seq) > 1 and seq[-1] in seq[:-1]:
        return

    if len(seq) == n:
        print(''.join(seq))
        return

    for letter in char_list:
        seq.append(letter)
        _print_no_repetition_sequences(char_list, n, seq)
        seq.pop()


def parentheses(n: int) -> List[str]:
    """
    This function receives a number n and returns a list with all the strings
    combinations with n valid (every opening brackets has closing brackets)
    pairs of parenthesis.
    :param n: number of brackets
    :type n: int
    :return: list of all combinations with n valid pairs of parenthesis.
    :rtype: list[str]
    """
    results: List[str] = []
    _parentheses_helper(n, [], 0, 0, results)
    return results


def _parentheses_helper(n: int, seq: List[str], num_open: int,
                        num_close: int, results: List[str]) -> None:
    """
    Helper function for the function parentheses():
    This function finds in a recursive way all the possible combinations
    with n valid pairs of parenthesis, and update the list of results.
    :param n: number of brackets
    :type n: int
    :param seq: current sequence of combination list
    :type seq: List[str]
    :param num_open: number of opening brackets
    :type num_open: int
    :param num_close: number of closing brackets
    :type num_close: int
    :param results: combinations results list
    :type results: List[str]
    """
    if ''.join(seq) in results:
        return

    if num_close + num_open == n * 2:  # when left == n, right == n .
        results.append(''.join(seq))
        return

    for i in ['(', ')']:
        seq.append(i)
        # add opening brackets as long as number of opening brackets
        # smaller than n:
        if num_open < n:
            if i == '(':
                _parentheses_helper(n, seq, num_open + 1, num_close, results)
        # add closing brackets as long as number of brackets smaller than
        # number of opening brackets:
        if num_open > num_close:
            if i == ')':
                _parentheses_helper(n, seq, num_open, num_close + 1, results)
        seq.pop()


def flood_fill(image: List[List[str]], start: Tuple[int, int]) -> None:
    """
    This function receives an image of 2D List filled with the characters
    '.'(=empty cell) or '*'(=full cell), and a start position and recursively
    fills an empty cells if it is the cell marked start, or only if the empty
    cell is next to the cell which was filled earlier.
    :param image: 2D list of characters ('.' or '*')
    :type image: List[List[str]]
    :param start: start position
    :type start: Tuple[int,int]
    """
    if image[start[0]][start[1]] == '*':
        return

    if image[start[0]][start[1]] == '.':
        image[start[0]][start[1]] = '*'

    for move in FILL_MOVES:
        new_position = start[0] + FILL_MOVES[move][0], start[1] + \
                       FILL_MOVES[move][1]
        flood_fill(image, new_position)
        start = new_position[0] - FILL_MOVES[move][0], new_position[1] - \
                FILL_MOVES[move][1]
