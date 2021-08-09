#################################################################
# FILE : test_3.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse lab5 2021
# DESCRIPTION: test to code 3
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
from code_3 import *


def test_fizzBuzz_3():
    """
    test for fizzBuzz_3()
    """
    assert fizzBuzz_3(3) == 3
    assert fizzBuzz_3(13) == 'Fizz'
    assert fizzBuzz_3(331) == 'Fizz'
    assert fizzBuzz_3(9) == 'Fizz'
    assert fizzBuzz_3(42) == 'Fizz'
    assert fizzBuzz_3(25) == 25
    assert fizzBuzz_3(7) == 7
    assert fizzBuzz_3(-5) == -5
    assert fizzBuzz_3(52) == 'Buzz'
    assert fizzBuzz_3(10) == 'Buzz'
    assert fizzBuzz_3(5581) == 'Buzz'
    assert fizzBuzz_3(300) == 300
    assert fizzBuzz_3(513) == 513
    assert fizzBuzz_3(53) == 'FizzBuzz'
    assert fizzBuzz_3(523) == 'FizzBuzz'
    assert fizzBuzz_3(720) == 'FizzBuzz'
    assert fizzBuzz_3(60) == 'FizzBuzz'


if __name__ == '__main__':
    test_fizzBuzz_3()
