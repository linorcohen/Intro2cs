#################################################################
# FILE : math_print.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A simple program that prints math functions.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: https://docs.python.org/3/library/math.html
# NOTES: NONE
#################################################################
import math


def golden_ratio():
    """
    This function prints the calculation of the Golden Ratio.
    """
    print((1 + math.sqrt(5)) / 2)


def six_squared():
    """
    This function prints the calculation of the number 6 squared.
    """
    print(math.pow(6, 2))


def hypotenuse():
    """
    This function prints the calculation of the hypotenuse of a right
    angle triangle with legs length of 12 and 5.
    """
    print(math.sqrt((math.pow(5, 2) + math.pow(12, 2))))


def pi():
    """
    This function prints the number pi.
    """
    print(math.pi)


def e():
    """
    This function prints the number e.
    """
    print(math.e)


def squares_area():
    """
    This function prints the areas of squares with the ribs length
    of 1 to 10 (including 1 and 10)
    """
    print(1 * 1, 2 * 2, 3 * 3, 4 * 4, 5 * 5, 6 * 6, 7 * 7, 8 * 8, 9 * 9,
          10 * 10)


if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()
