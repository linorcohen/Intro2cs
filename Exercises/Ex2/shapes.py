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
    and to provide the data for the calculation.
    :return: the area of the shape. else, return none.
    :rtype: float
    """
    user_shape = int(input("Choose shape (1=circle, 2=rectangle,"
                           " 3=triangle): "))
    area = None
    # the code below calculates the area of the shape that was chosen
    if user_shape == 1:
        area = circle_area()
    elif user_shape == 2:
        area = rectangle_area()
    elif user_shape == 3:
        area = triangle_area()
    return area


def circle_area():
    """
    This function calculates the area of a circle
    :return: area of a circle
    :rtype: float
    """
    radios = float(input())
    return (radios ** 2) * PI


def rectangle_area():
    """
    This function calculates the area of a rectangle
    :return: area of a rectangle
    :rtype: float
    """
    first_side = float(input())
    second_side = float(input())
    return first_side * second_side


def triangle_area():
    """
    This function calculates the area of a triangle
    :return: area of a triangle
    :rtype: float
    """
    side = float(input())
    return (math.sqrt(3) / 4) * (side ** 2)
