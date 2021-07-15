#################################################################
# FILE : largest_and_smallest.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that returns the largest and smallest numbers
# of three numbers given.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################

# inputs for check_largest_and_smallest():
# I choose the input (0, 0, 0) to check if the function can handle
# three identical numbers.
# I choose the input (-7, -1, -12) to check if the function can handle
# negative numbers while they are not sorted.


def largest_and_smallest(first_num, second_num, third_num):
    """
    This function get three numbers and returns the largest and the smallest
    of the them.
    :param first_num: a number
    :type first_num: int or float
    :param second_num: a number
    :type second_num: int or float
    :param third_num: a number
    :type third_num: int or float
    :return: the largest and the smallest numbers of all three
    :rtype: int or float
    """
    # the next lines evaluate the largest number
    largest_num = first_num
    if second_num > largest_num:
        largest_num = second_num
    if third_num > largest_num:
        largest_num = third_num

    # the next lines evaluate the smallest number
    smallest_num = first_num
    if second_num < smallest_num:
        smallest_num = second_num
    if third_num < smallest_num:
        smallest_num = third_num

    return largest_num, smallest_num


def check_largest_and_smallest():
    """
    This function checks the function largest_and_smallest().
    :return: True, if the function returned all the expected results.
    False, if at least one of the results is wrong.
    :rtype: bool
    """
    # the code below checks the outputs of the function calls
    if largest_and_smallest(17, 1, 6) != (17, 1):
        return False
    if largest_and_smallest(1, 17, 6) != (17, 1):
        return False
    if largest_and_smallest(1, 1, 2) != (2, 1):
        return False
    if largest_and_smallest(0, 0, 0) != (0, 0):
        return False
    if largest_and_smallest(-7, -1, -12) != (-1, -12):
        return False
    return True
