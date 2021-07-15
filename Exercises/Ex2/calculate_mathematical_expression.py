#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex2 2021
# DESCRIPTION: A simple program that calculates mathematical expressions
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################


def calculate_mathematical_expression(first_num, second_num, math_operator):
    """
    This function receives two numbers and one of the four
    mathematical operations ('-', '+', '*', ':') and returns the result
    of the calculation.
    :param first_num: a number
    :type first_num: int or float
    :param second_num: a number
    :type second_num: int or float
    :param math_operator: mathematical operator ('-', '+', '*', or ':')
    :type math_operator: str
    :return: the result of the calculation. else, returns None.
    :rtype: int or float
    """
    solution = None

    # the code below calculates the mathematical solution according
    # to the mathematical operator
    if math_operator == '+':
        solution = first_num + second_num
    elif math_operator == '-':
        solution = first_num - second_num
    elif math_operator == '*':
        solution = first_num * second_num
    elif math_operator == ':' and second_num != 0:  # division by zero illegal
        solution = first_num / second_num
    return solution


def calculate_from_string(math_expression):
    """
    This function receives a string of mathematical expression
    contain two numbers separated by one mathematical
    operator ('-', '+', '*', ':').
    :param math_expression: mathematical expression
    :type math_expression: str
    :return: solution of the mathematical expression. else, returns None.
    :rtype: int or float
    """
    # the code below separates the string and calculate the solution
    # of the expression
    math_expression_list = math_expression.split(' ')
    first_num = float(math_expression_list[0])
    math_operator = math_expression_list[1]
    second_num = float(math_expression_list[2])
    return calculate_mathematical_expression(first_num, second_num,
                                             math_operator)
