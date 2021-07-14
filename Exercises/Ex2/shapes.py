#################################################################
# FILE : shapes.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that calculate the area of a shape according to
# the user input.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
import math

PI = math.pi


def shape_area():
    """
    This function asks the user to choose a shape to calculate its area,
    and then to provide the data for the calculation.
    :return: the area of the shape. else, return none.
    :rtype: float
    """
    user_shape = float(input("Choose shape (1=circle, 2=rectangle,"
                             " 3=triangle): "))
    area = None
    if user_shape == 1:
        radios = float(input())
        area = radios ** 2 * PI
    elif user_shape == 2:
        first_side = float(input())
        second_side = float(input())
        area = first_side * second_side
    elif user_shape == 3:
        side = float(input())
        area = (math.sqrt(3) / 4) * (side ** 2)
    return area
