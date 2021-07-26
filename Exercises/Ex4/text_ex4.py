from hangman import *


def test_update_word_pattern():
    assert update_word_pattern('apple', '___l_', 'p') == '_ppl_'
    assert update_word_pattern('apple', '___l_', 'a') == 'a__l_'
    assert update_word_pattern('apple', '___l_', 'm') == '___l_'


def test_check_letter_validity():
    assert check_letter_validity('rr') is False
    assert check_letter_validity('r') is True
    assert check_letter_validity('!') is False
    assert check_letter_validity('3') is False
    assert check_letter_validity('') is False
    assert check_letter_validity('A') is False
    assert check_letter_validity(' ') is False


def test_check_letter_already_picked():
    assert check_letter_already_picked('t', ['t', 'i'], '__r_') is True
    assert check_letter_already_picked('t', ['i'], '__t_') is True
    assert check_letter_already_picked('t', ['i'], '__o_') is False
    assert check_letter_already_picked('t', [], '__') is False


def test_update_score():
    assert update_score(50, 1) == 51
    assert update_score(1, 2) == 4
    assert update_score(10, 0) == 10


def test_update_wrong_hints():
    lst = []
    update_wrong_hints(lst, 't')
    assert lst == ['t']
    update_wrong_hints(lst,'r')
    assert lst == ['t', 'r']


def test_check_if_win_or_lose():
    assert check_if_win_or_lose('pool', 'pool') == WIN_MASSAGE
    assert check_if_win_or_lose('pool', 'cool') == LOSE_MASSAGE + 'cool'
    assert check_if_win_or_lose('_ool', 'pool') == LOSE_MASSAGE + 'pool'
    assert check_if_win_or_lose('pool ', 'pool') == LOSE_MASSAGE + 'pool'


def test_word_input():
    assert word_input('poo_', 51, 'pool', 'pool') == ('pool', 51)
    assert word_input('poo_', 1, 'pool', 'pool') == ('pool', 1)
    assert word_input('poo_', 51, 'cool', 'pool') == ('poo_', 50)
    assert word_input('poo_', 1, 'l', 'pool') == ('poo_', 0)


def test_check_letter():
    assert check_if_letter_can_be_used('l', ['r'], '___') == GENERAL_MASSAGE
    assert check_if_letter_can_be_used('l', ['r'], '_l_') == LETTER_ALREADY_PICKED_MESSAGE
    assert check_if_letter_can_be_used('y', ['y'], '___') == LETTER_ALREADY_PICKED_MESSAGE
    assert check_if_letter_can_be_used('', ['y'], '__') == LETTER_INVALID_MASSAGE
    assert check_if_letter_can_be_used('3', ['y'], '__') == LETTER_INVALID_MASSAGE
    assert check_if_letter_can_be_used(' ', ['y'], '__') == LETTER_INVALID_MASSAGE
    assert check_if_letter_can_be_used('55', ['y'], '__') == LETTER_INVALID_MASSAGE
    assert check_if_letter_can_be_used('hh', ['y'], '__') == LETTER_INVALID_MASSAGE


def test_letter_input():
    assert letter_input(10, 'l', 'home', '____', ['r']) == ('____', 9)
    assert letter_input(10, 'l', 'lome', '____', ['r']) == ('l___', 10)
    assert letter_input(10, 'h', 'home', 'h___', ['r']) == ('h___', 10)
    assert letter_input(10, 'y', 'rome', '____', ['y']) == ('____', 9)
    assert letter_input(1, 'y', 'rome', '____', ['i']) == ('____', 0)
    assert letter_input(1, 'y', 'your', '____', ['t']) == ('y___', 1)


def test_initial_the_game():
    assert initial_the_game(10, 'home') == ([], GENERAL_MASSAGE, '____', 10)
    assert initial_the_game(1, 'home') == ([], GENERAL_MASSAGE, '____', 1)
    assert initial_the_game(1, '') == ([], GENERAL_MASSAGE, '', 1)


def test_hint_input():
    pass


def test_filter_wrong_letters():
    assert filter_wrong_letters(['lo', 've'], ['r', 'f']) == ['lo', 've']
    assert filter_wrong_letters(['lo', 've'], ['o', 'f']) == ['ve']


def main():
    test_update_word_pattern()
    test_check_letter_validity()
    test_check_letter_already_picked()
    test_update_score()
    test_update_wrong_hints()
    test_check_if_win_or_lose()
    test_word_input()
    test_check_letter()
    test_letter_input()
    test_initial_the_game()
    test_hint_input()
    test_filter_wrong_letters()
    print('all tests passed')


if __name__ == '__main__':
    main()
