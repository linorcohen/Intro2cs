#################################################################
# FILE : quadratic_equation.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that returns the solutions (if there are any)
# of a quadratic equation.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: https://en.wikipedia.org/wiki/Quadratic_equation
# NOTES: NONE
#################################################################
import math


def quadratic_equation(a, b, c):
    """
    This function gets three coefficients of a quadratic equation and returns
    the solutions (if there are any) of the equation.
    :param a: quadratic coefficient
    :type a: int or float
    :param b: linear coefficient
    :type b: int or float
    :param c: free term
    :type c: int or float
    :return: the solutions of the quadratic equation
    :rtype: int or float, else, returns none.
    """
    discriminant = (b ** 2) - (a * c * 4)
    denominator = a * 2
    first_solution = None
    second_solution = None
    if discriminant > 0:
        first_solution = (-b + math.sqrt(discriminant)) / denominator
        second_solution = (-b - math.sqrt(discriminant)) / denominator
    elif discriminant == 0:
        first_solution = -b / denominator
        second_solution = None
    return first_solution, second_solution


def quadratic_equation_user_input():
    """
    This function asks from the user to input coefficients of a quadratic
    equation and prints the solutions of that equation.
    :return: print of the quadratic equation solutions
    :rtype: str
    """
    user_coefficients = input("insert coefficients a, b, and c: ")
    user_coefficients_list = user_coefficients.split(' ')
    b = float(user_coefficients_list[1])
    c = float(user_coefficients_list[2])
    a = float(user_coefficients_list[0])
    if a == 0:
        print("The parameter 'a' may not equal 0")
        return

    first_solution, second_solution = quadratic_equation(a, b, c)
    if first_solution is None and second_solution is None:
        print("The equation has no solutions")
        return
    if first_solution is not None and second_solution is None:
        print("The equation has 1 solutions: " + str(first_solution))
        return
    print("The equation has 2 solutions: " + str(first_solution) + " and " +
          str(second_solution))
    # return
