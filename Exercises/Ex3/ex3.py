#################################################################
# FILE : ex3.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex3 2021
# DESCRIPTION: A simple program ...
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: https://encyclopediaofmath.org/wiki/Monotone_function
# NOTES: NONE
#################################################################

def input_list():
    """
    This function gets numbers from the user and put them in a list
    with the sum of them.
    :return: list of all the numbers, and their sum as the last item.
    :rtype: list of float or int
    """
    num_list = []
    list_sum = 0
    while True:
        user_input = input()
        if user_input == '':  # '' represents end of input/loop
            break
        # the code below adds the number to the list and to the sum
        num_list.append(float(user_input))
        list_sum += float(user_input)
    num_list.append(list_sum)  # adds the sum to the end of the list
    return num_list


def inner_product(vec_1, vec_2):
    """
    This function calculates the inner product of two lists.
    :param vec_1: a lists of numbers
    :type vec_1: list of int or float
    :param vec_2: a lists of numbers
    :type vec_2: list of int or float
    :return: inner product
    :rtype: int or float
    """
    inner_product_result = 0
    if len(vec_1) == len(vec_2):
        # the code below adds to the inner product result the products of the
        # coordinates with same index
        for index in range(len(vec_1)):
            inner_product_result += vec_1[index] * vec_2[index]
        return inner_product_result
    return  # returns None in case the lists are not the same length


def sequence_monotonicity(sequence):
    """
    This function gets a list of a sequence of numbers and returns a 4 boolean
    items list if the sequence meets the conditions:
    [ if increasing, if very increasing, if decreasing, if very decreasing]
    :param sequence: a sequence of numbers
    :type sequence:list of int or float
    :return: list of 4 boolean items: for each - True if the sequence meets the
    condition, else False.
    :rtype: list of bool
    """
    monotonicity_list = [True, True, True, True]
    # the code below sets the monotonicity of the sequence
    monotonicity_list[0] = check_increasing(sequence)
    monotonicity_list[1] = check_very_increasing(sequence)
    monotonicity_list[2] = check_decreasing(sequence)
    monotonicity_list[3] = check_very_decreasing(sequence)

    return monotonicity_list


def check_increasing(sequence):
    """
    This function checks if a sequence is monotonically increasing.
    :param sequence: a sequence of numbers
    :type sequence:list of int or float
    :return: True if the sequence is monotonically increasing, else False.
    :rtype: bool
    """
    for index in range(len(sequence) - 1):
        if not sequence[index] <= sequence[index + 1]:
            return False
    return True


def check_very_increasing(sequence):
    """
    This function checks if a sequence is monotonically very increasing.
    :param sequence: a sequence of numbers
    :type sequence:list of int or float
    :return: True if the sequence is monotonically very increasing, else False.
    :rtype: bool
    """
    for index in range(len(sequence) - 1):
        if not sequence[index] < sequence[index + 1]:
            return False
    return True


def check_decreasing(sequence):
    """
    This function checks if a sequence is monotonically decreasing.
    :param sequence: a sequence of numbers
    :type sequence:list of int or float
    :return: True if the sequence is monotonically decreasing, else False.
    :rtype: bool
    """
    for index in range(len(sequence) - 1):
        if not sequence[index] >= sequence[index + 1]:
            return False
    return True


def check_very_decreasing(sequence):
    """
    This function checks if a sequence is monotonically very decreasing.
    :param sequence: a sequence of numbers
    :type sequence:list of int or float
    :return: True if the sequence is monotonically very decreasing, else False.
    :rtype: bool
    """
    for index in range(len(sequence) - 1):
        if not sequence[index] > sequence[index + 1]:
            return False
    return True


def monotonicity_inverse(def_bool):
    """
    This function gets a list of 4 boolean values, represents the monotonicity
    of a sequence, and returns a sequence that meets the conditions depending
    on where True is in the input.
    [ if increasing, if very increasing, if decreasing, if very decreasing]
    :param def_bool: list of 4 boolean items
    :type def_bool: list of bool
    :return: list of 4 numbers
    :rtype: list of int
    """
    if def_bool == [True, True, False, False]:
        return [1, 2, 3, 4]
    if def_bool == [True, False, False, False]:
        return [1, 2, 2, 3]
    if def_bool == [True, False, True, False]:
        return [1, 1, 1, 1]
    if def_bool == [False, False, True, True]:
        return [8, 5, 3, 0]
    if def_bool == [False, False, True, False]:
        return [4, 2, 1, 1]
    if def_bool == [False, False, False, False]:
        return [1, 0, -2, 1]
    return  # None if there is on sequence that meets the conditions


def primes_for_asafi(n):
    """
    This function that receives an integer n and returns a list of the first n
    prime numbers in order, starting with 2 (including).
    :param n: the number of prime numbers to return
    :type n: int
    :return: list of first n prime numbers
    :rtype: list of int
    """
    primes = []
    index = 2
    while len(primes) < n:
        if is_num_prime(index):
            primes.append(index)
        index += 1
    return primes


def is_num_prime(num):
    """
    This function checks if a number is a prime number.
    :param num: a number
    :type num: int
    :return: True if prime, else False.
    :rtype: bool
    """
    for divisor in range(2, int(num**(1/2)) + 1):
        if num % divisor == 0:
            return False
    return True


def sum_of_vectors(vec_lst):
    """
    This function that receives a list of vectors (i.e. a list of lists) and
    returns their vector sum.
    :param vec_lst: a list of lists (list of vectors)
    :type vec_lst: list of lists of int or float
    :return: list of the vectors sum
    :rtype: list of int or float
    """
    vectors_sum = []
    if vec_lst != [[]]:  # one empty list is not allowed
        for index in range(len(vec_lst[0])):
            vec_sum = 0
            for vec_num in range(len(vec_lst)):
                vec_sum += vec_lst[vec_num][index]
            vectors_sum.append(vec_sum)
        return vectors_sum
    return


def num_of_orthogonal(vectors):
    """
    A function that receives a list of vectors (i.e. a list of lists) and
    returns the number of pairs of lists that are perpendicular to each other.
    :param vectors: a list of lists (list of vectors)
    :type vectors: list of lists of int or float
    :return: number of pairs of lists that are perpendicular to each other.
    :rtype: int
    """
    orthogonal_sum = 0
    for vec_index in range(len(vectors)):
        for vec in vectors[vec_index + 1:]:
            if inner_product(vectors[vec_index], vec) == 0:
                orthogonal_sum += 1
    return orthogonal_sum



















