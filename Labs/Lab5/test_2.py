#################################################################
# FILE : test_2.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse lab5 2021
# DESCRIPTION: test for code 2
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
from code_2 import *


def test_fizzBuzz_2():
    """
    test for fizzBuzz_2()
    """
    assert fizzBuzz_2(3) == 'Fizz'
    assert fizzBuzz_2(6) == 'Fizz'
    assert fizzBuzz_2(13) == 'Fizz'
    assert fizzBuzz_2(-3) == 'Fizz'
    assert fizzBuzz_2(23) == 'Fizz'
    assert fizzBuzz_2(5) == 'Buzz'
    assert fizzBuzz_2(10) == 'Buzz'
    assert fizzBuzz_2(-5) == 'Buzz'
    assert fizzBuzz_2(52) == 'Buzz'
    assert fizzBuzz_2(300) == 'FizzBuzz'
    assert fizzBuzz_2(513) == 'FizzBuzz'
    assert fizzBuzz_2(4) == 4
    assert fizzBuzz_2(1111) == 1111


if __name__ == '__main__':
    test_fizzBuzz_2()