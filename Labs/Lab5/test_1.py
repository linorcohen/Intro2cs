#################################################################
# FILE : test_1.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse lab5 2021
# DESCRIPTION: test for code 1
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
from code_1 import *


def test_fizzBuzz_1():
    """
    test for fizzBuzz_1()
    """
    assert fizzBuzz_1(3) == 'Fizz'
    assert fizzBuzz_1(6) == 'Fizz'
    assert fizzBuzz_1(-3) == 'Fizz'
    assert fizzBuzz_1(5) == 'Buzz'
    assert fizzBuzz_1(10) == 'Buzz'
    assert fizzBuzz_1(300) == 'FizzBuzz'
    assert fizzBuzz_1(15) == 'FizzBuzz'
    assert fizzBuzz_1(4) == 4
    assert fizzBuzz_1(2) == 2


if __name__ == '__main__':
    test_fizzBuzz_1()
