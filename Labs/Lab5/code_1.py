#################################################################
# FILE : code_1.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse lab5 2021
# DESCRIPTION: code 1
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################

def fizzBuzz_1(num):
    """
    This function receives an int num and returns:
    “Fizz” - if the number num is a multiple of 3
    “Buzz” - if the number num is a multiple of 5
    “FizzBuzz” - if the number num is a multiple of both 5 and 3
    else, returns num.
    :param num: a number
    :type num: int
    :return: a string "Fizz", "Buzz" or "FizzBuzz", else the num.
    :rtype: str or int
    """
    if num % 15 == 0:  # divide in 3 and 5 must divide 3*5 =15
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return num
