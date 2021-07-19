from calculate_mathematical_expression import *
from largest_and_smallest import *
from shapes import *
from quadratic_equation import *
from temperature import *

if __name__ == '__main__':

    assert calculate_mathematical_expression(10, 6, '-') == 4
    assert calculate_mathematical_expression(6, 5, '*') == 30
    assert calculate_mathematical_expression(5, 4, ':') == 1.25
    assert calculate_mathematical_expression(10, 2, ':') == 5
    assert calculate_mathematical_expression(10, 0, ':') is None
    assert calculate_mathematical_expression(10, 0.0, ':') is None
    assert calculate_mathematical_expression(10, 4, '%') is None

    assert calculate_from_string('2 - 7') == -5
    assert calculate_from_string('0 - -3') == 3
    assert calculate_from_string('7 - 2') == 5
    assert calculate_from_string('4 : 10') == 0.4
    assert calculate_from_string('10 : 4') == 2.5
    assert calculate_from_string('2.4 - 0.4') == 2.0
    assert calculate_from_string('1 : 0') is None
    assert calculate_from_string('1 $ 0') is None

    assert largest_and_smallest(5, 1, 10) == (10, 1)
    assert largest_and_smallest(8, 2, 7.3) == (8, 2)
    assert largest_and_smallest(1, 1, 10) == (10, 1)
    assert largest_and_smallest(-5, -1, -13) == (-1, -13)

    assert quadratic_equation(1, 1.5, -1) == (0.5, -2)
    assert quadratic_equation(1, -8, 16) == (4, None)
    assert quadratic_equation(1, -2, 34.5) == (None, None)
    assert quadratic_equation(1, 2, -8) == (2.0, -4.0)
    assert quadratic_equation(1, 0, -4) == (2.0, -2.0)
    assert quadratic_equation(1, -1, 0) == (1.0, 0.0)
    assert quadratic_equation(1, 0, 0) == (0.0, None)

    # quadratic_equation_user_input()
    # print(shape_area())

    assert is_it_summer_yet(19, 22, 21, 20) is True
    assert is_it_summer_yet(20, 22, 21, 20) is True
    assert is_it_summer_yet(7, 5, -2, 11) is False

    assert is_it_summer_yet(10, 0.2, 2, -7) is False
    assert is_it_summer_yet(-5, 0, 0, 0) is True
    assert is_it_summer_yet(0, 0, 0, 0) is False
    assert is_it_summer_yet(0.2, 0.1, 0.5, 6.7) is True

    assert largest_and_smallest(17, 1, 6) == (17, 1)
    assert largest_and_smallest(1, 17, 6) == (17, 1)
    assert largest_and_smallest(1, 1, 2) == (2, 1)
    assert largest_and_smallest(1, 2, 3) == (3, 1)
    # drive tester:
    assert calculate_from_string("10 : 2") == 5.0
    assert calculate_from_string("10 : -2") == -5.0
    assert calculate_from_string("-10 : -2") == 5.0
    assert calculate_from_string("-10 : 2") == -5.0
    assert calculate_from_string("10 + 2") == 12.0
    assert calculate_from_string("100 - 39.3") == 60.7
    assert calculate_from_string("5 : 2") == 2.5
    assert calculate_from_string("5 : 0") is None
    assert calculate_from_string("10 333 2") is None
    assert calculate_from_string("10 ^ 2") is None

    assert largest_and_smallest(5, 1, 10) == (10, 1)
    assert largest_and_smallest(2.5, 2.5, 7) == (7, 2.5)
    assert largest_and_smallest(7, 2.5, 2.5) == (7, 2.5)
    assert largest_and_smallest(-5, -5, -5) == (-5, -5)
    assert largest_and_smallest(10, 0, -2) == (10, -2)
    assert check_largest_and_smallest() is True

    assert quadratic_equation(1, 1.5, -1) == (0.5, -2)
    assert quadratic_equation(1, -8, 16) == (4, None)
    assert quadratic_equation(1, -2, 34.5) == (None, None)
    assert quadratic_equation(4, -12, 9) == (3 / 2, None)

    assert is_it_summer_yet(26, 38, 90, 20) is True
    assert is_it_summer_yet(10, 10, 10, 10) is False
    assert is_it_summer_yet(10, 11, 10, 11) is True
    assert is_it_summer_yet(-1, -9, 0, 1) is True
    assert is_it_summer_yet(0, 90, 0, 1) is True

    print("All tests passed")
