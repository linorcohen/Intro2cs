#################################################################
# FILE : code_3.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse lab5 2021
# DESCRIPTION: code 3
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
from code_2 import *


def fizzBuzz_3(num):
    """
    This function receives an int num and returns a string value based on the
    even/uneven number of reasons for num to have a “fizzBuzz” value:
    uneven number of reasons for "Fizz" number - return "Fizz", else return num
    uneven number of reasons for "Buzz" number - return "Buzz", else return num
    both uneven reasons for num to be “Fizz” and uneven reasons for num to be
    “Buzz” - return "FizzBuzz", else return num.
    :param num: a number
    :type num: int
    :return: a string "Fizz", "Buzz" or "FizzBuzz", else the num.
    :rtype: str or int
    """
    if fizzBuzz_2(num) == 'FizzBuzz':
        num_of_reasons = count(num)
        if num_of_reasons % 2 == 0:
            return 'FizzBuzz'
    elif fizzBuzz_2(num) == 'Fizz':
        num_of_reasons = count(num)
        if num_of_reasons % 2 != 0:
            return 'Fizz'
    elif fizzBuzz_2(num) == 'Buzz':
        num_of_reasons = count(num)
        if num_of_reasons % 2 != 0:
            return 'Buzz'
    return num


def count(num):
    """
    check conditions for a number and count them.
    :param num: a number
    :type num: int
    :return: the number of conditions the number passed.
    :rtype: int
    """
    count_condition = 0
    if num % 3 == 0:
        count_condition += 1
    if '3' in str(num):
        count_condition += 1
    if num % 5 == 0:
        count_condition += 1
    if '5' in str(num):
        count_condition += 1
    return count_condition
