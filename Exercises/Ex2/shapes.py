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


def shape_area():
    """
    This function asks the user to choose a shape to calculate its area,
    and to provide the data for the calculation.
    :return: the area of the shape. else, return None.
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
    This function calculates the area of a circle by asking the user to input
    radios.
    :return: area of a circle
    :rtype: float
    """
    radios = float(input())
    return (radios ** 2) * math.pi


def rectangle_area():
    """
    This function calculates the area of a rectangle by asking the user to
    input the rectangle sides.
    :return: area of a rectangle
    :rtype: float
    """
    side_1 = float(input())
    side_2 = float(input())
    return side_1 * side_2


def triangle_area():
    """
    This function calculates the area of a equilateral triangle by asking the
    user to input the triangle side.
    :return: area of a triangle
    :rtype: float
    """
    side = float(input())
    return (math.sqrt(3) / 4) * (side ** 2)
