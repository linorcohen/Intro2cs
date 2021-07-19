#################################################################
# FILE : ex3.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex3 2021
# DESCRIPTION: A simple program that practices
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: https://encyclopediaofmath.org/wiki/Monotone_function
# NOTES: NONE
#################################################################

def input_list():
    """
    This function gets numbers from the user and put them in a list
    with their sum in the end.
    :return: list of all the numbers, and their sum in the end.
    :rtype: list of float or int
    """
    list_num = []
    list_sum = 0
    while True:
        user_input = input()
        if user_input == '':  # '' represents end of input/loop
            break
        # the code below adds the number to the list and to the sum
        list_num.append(float(user_input))
        list_sum += float(user_input)
    list_num.append(list_sum)  # adds the sum to the end of the list
    return list_num


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
        # the code below adds to the inner_product_result the products of the
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
    :type sequence: list of int or float
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
    :type sequence: list of int or float
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
    :type sequence: list of int or float
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
    :type sequence: list of int or float
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
    :type sequence: list of int or float
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
    on where True is in the list:
    [ if increasing, if very increasing, if decreasing, if very decreasing]
    :param def_bool: list of 4 boolean items
    :type def_bool: list of bool
    :return: list of 4 numbers
    :rtype: list of int
    """
    lst_of_monotonic_sequences = [[1, 2, 3, 4], [1, 2, 2, 3], [1, 1, 1, 1],
                                  [8, 5, 3, 0], [4, 2, 1, 1], [1, 0, -2, 1]]
    for sequence in lst_of_monotonic_sequences:
        if sequence_monotonicity(sequence) == def_bool:
            return sequence
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
    check_num = 2  # starts from the first prime number
    while len(primes) < n:  # check numbers until get list of n primes numbers
        if is_num_prime(check_num):
            primes.append(check_num)
        check_num += 1
    return primes


def is_num_prime(num):
    """
    This function checks if a number is a prime number.
    :param num: a number
    :type num: int
    :return: True if prime, else False.
    :rtype: bool
    """
    # the code below check if the number has a divisor until number square root
    for divisor in range(2, int(num ** (1 / 2)) + 1):
        if num % divisor == 0:
            return False
    return True


def sum_of_vectors(vec_lst):
    """
    This function receives a list of vectors (i.e. a list of lists) and
    returns their vector sum.
    :param vec_lst: a list of lists (list of vectors)
    :type vec_lst: list of lists of int or float
    :return: list of the vectors sum
    :rtype: list of int or float
    """
    vectors_sum = []
    if vec_lst != [[]]:
        # the code below adds to the vectors sum the sum of coordinates with
        # same index
        for index in range(len(vec_lst[0])):
            vec_index_sum = 0
            for vec_num in range(len(vec_lst)):
                vec_index_sum += vec_lst[vec_num][index]
            vectors_sum.append(vec_index_sum)
        return vectors_sum
    return  # return None in case of one empty list received


def num_of_orthogonal(vectors):
    """
    This function receives a list of vectors (i.e. a list of lists) and
    returns the number of pairs of lists that are perpendicular to each other.
    :param vectors: a list of lists (list of vectors)
    :type vectors: list of lists of int or float
    :return: number of pairs of lists that are perpendicular to each other.
    :rtype: int
    """
    pairs_sum = 0
    # the code below check for each vector the inner product with the vectors
    # after it in the list (to prevent duplicates)
    for vec_index in range(len(vectors)):
        for vec in vectors[vec_index + 1:]:
            # if pair is perpendicular adds it to the pairs_sum
            if inner_product(vec, vectors[vec_index]) == 0:
                pairs_sum += 1
    return pairs_sum
