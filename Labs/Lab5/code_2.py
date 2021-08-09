#################################################################
# FILE : code_2.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse lab5 2021
# DESCRIPTION: code 2
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################

def fizzBuzz_2(num):
    """
    This function receives an int num and returns:
    “Fizz” - if the number num is a multiple of 3 or it has a 3 in it
    "Buzz” - if the number num is a multiple of 5 or it has a 5 in it
    “FizzBuzz” - if the number num is "Fizz” and “Buzz”
    else, returns num.
    :param num: a number
    :type num: int
    :return: a string "Fizz", "Buzz" or "FizzBuzz", else the num.
    :rtype: str or int
    """
    if num % 3 == 0 or '3' in str(num):
        if num % 5 == 0 or '5' in str(num):
            return 'FizzBuzz'
        return 'Fizz'
    if num % 5 == 0 or '5' in str(num):
        return 'Buzz'
    return num
