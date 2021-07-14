#################################################################
# FILE : largest_and_smallest.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that returns the largest and smallest
# numbers of three numbers given.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################

# I choose the input (0, 0, 0) to check what the function will do if she will
# get three identical numbers.
# I choose the input () to check

def largest_and_smallest(first_num, second_num, third_num):
    """
    This function get three numbers and returns the largest of them,
    and the smallest of them.
    :param first_num: a number
    :type: int or float
    :param second_num: a number
    :type: int or float
    :param third_num: a number
    :type: int or float
    :return: the largest and the smallest numbers of all three
    :rtype: int or float
    """
    largest_num = first_num
    if second_num > largest_num:
        largest_num = second_num
    if third_num > largest_num:
        largest_num = third_num

    smallest_num = first_num
    if second_num < smallest_num:
        smallest_num = second_num
    if third_num < smallest_num:
        smallest_num = third_num

    return largest_num, smallest_num


def check_largest_and_smallest():
    """
    This function checks the function largest_and_smallest() using corner cases
    :return: True if the function returned all the expected results.
    if at least one of the results is wrong, returns False.
    :rtype: bool
    """
    if (17, 1) != largest_and_smallest(17, 1, 6):
        return False
    elif (17, 1) != largest_and_smallest(1, 17, 6):
        return False
    elif (2, 1) != largest_and_smallest(1, 1, 2):
        return False
    elif (0, 0) != largest_and_smallest(0, 0, 0):
        return False
    elif (21, -21) != largest_and_smallest(-21, 0, 21):
        return False
    return True
