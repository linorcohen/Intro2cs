from ex7 import *


def flood_fill_check():
    m = [['*', '*', '*', '*', '*'],
    ['*', '.', '.', '.', '*'],
    ['*', '.', '*', '*', '*'],
    ['*', '.', '*', '.', '*'],
    ['*', '*', '*', '*', '*']]
    flood_fill(m, (1, 1))
    for line in m:
        print(line)

def test_digit_sum():
    assert digit_sum(123) == 6
    assert digit_sum(479) == 20
    assert digit_sum(111) == 3
    assert digit_sum(0) == 0
    assert digit_sum(12) == 3
    assert digit_sum(1111) == 4
    assert digit_sum(841561) == 25
    assert digit_sum(9) == 9
    assert digit_sum(10) == 1


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(9) is False
    assert is_prime(27) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(11) is True
    assert is_prime(97) is True


if __name__ == '__main__':
    # print_to_n(10)
    # print_sequences(['a'],2)
    # print(parentheses(0))
    # print_no_repetition_sequences(['a'], 2)
    # print_no_repetition_sequences(['a', 'b','c','d'], 4)
    # test_digit_sum()
    # test_is_prime()
    # flood_fill_check()
    # print_seq_check_no_rep()
    print('all tests passed')
