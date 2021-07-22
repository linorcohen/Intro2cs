from calculate_mathematical_expression import *
from largest_and_smallest import *
from quadratic_equation import *
from temperature import *


assert calculate_from_string("10 + 0") == 10.0
assert calculate_from_string("0 : 2") == 0
assert calculate_from_string("5 : 0") is None
assert calculate_from_string("5 / 2") is None
assert calculate_from_string("10 333 2") is None
assert calculate_from_string("10 ^ 2") is None


assert largest_and_smallest(5, 1, 10) == (10, 1)
assert largest_and_smallest(5, 10, 1) == (10, 1)
assert largest_and_smallest(1, 5, 10) == (10, 1)
assert largest_and_smallest(1, 10, 5) == (10, 1)
assert largest_and_smallest(10, 1, 5) == (10, 1)
assert largest_and_smallest(10, 5, 1) == (10, 1)


assert is_it_summer_yet(26, 38, 90.5, 20.5) is True
assert is_it_summer_yet(26, 20, 90, 38) is True
assert is_it_summer_yet(26, 38, 20, 90) is True
assert is_it_summer_yet(10, 11, 10, 11) is True
assert is_it_summer_yet(-1, -9, 0, 1) is True
assert is_it_summer_yet(0, 90, 0, 1) is True
assert is_it_summer_yet(26, 20, 90, 26) is False
assert is_it_summer_yet(10, 10, 10, 10) is False
assert is_it_summer_yet(26, 38, -14, 20) is False

print("All tests passed")
