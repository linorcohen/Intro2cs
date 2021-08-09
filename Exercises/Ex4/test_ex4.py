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
    assert returns_points_calculation(50, 1) == 51
    assert returns_points_calculation(1, 2) == 4
    assert returns_points_calculation(10, 0) == 10


def test_check_if_win_or_lose():
    assert check_if_win_or_lose('pool', 'pool') == WIN_MASSAGE
    assert check_if_win_or_lose('pool', 'cool') == LOSE_MASSAGE + 'cool'
    assert check_if_win_or_lose('_ool', 'pool') == LOSE_MASSAGE + 'pool'
    assert check_if_win_or_lose('pool ', 'pool') == LOSE_MASSAGE + 'pool'


def test_word_input():
    assert process_word_input('poo_', 51, 'pool', 'pool') == ('pool', 52)
    assert process_word_input('poo_', 1, 'pool', 'pool') == ('pool', 2)
    assert process_word_input('poo_', 51, 'cool', 'pool') == ('poo_', 51)
    assert process_word_input('poo_', 1, 'l', 'pool') == ('poo_', 1)


def test_check_letter():
    assert check_if_letter_can_be_used('l', ['r'], '___') == EMPTY_MASSAGE
    assert check_if_letter_can_be_used('l', ['r'], '_l_') == LETTER_ALREADY_PICKED_MASSAGE
    assert check_if_letter_can_be_used('y', ['y'], '___') == LETTER_ALREADY_PICKED_MASSAGE
    assert check_if_letter_can_be_used('', ['y'], '__') == LETTER_INVALID_MASSAGE
    assert check_if_letter_can_be_used('3', ['y'], '__') == LETTER_INVALID_MASSAGE
    assert check_if_letter_can_be_used(' ', ['y'], '__') == LETTER_INVALID_MASSAGE
    assert check_if_letter_can_be_used('55', ['y'], '__') == LETTER_INVALID_MASSAGE
    assert check_if_letter_can_be_used('hh', ['y'], '__') == LETTER_INVALID_MASSAGE


def test_letter_input():
    assert process_letter_input(10, 'l', 'home', '____', ['r']) == ('____', 10)
    assert process_letter_input(10, 'l', 'lome', '____', ['r']) == ('l___', 11)
    assert process_letter_input(10, 'h', 'home', 'h___', ['r']) == ('h___', 11)
    assert process_letter_input(10, 'y', 'rome', '____', ['y']) == ('____', 10)
    assert process_letter_input(1, 'y', 'rome', '____', ['i']) == ('____', 1)
    assert process_letter_input(1, 'y', 'your', '____', ['t']) == ('y___', 2)


def text_filter_words_list():
    assert filter_words_list(['love', 'home'], '____', ['r']) == ['love', 'home']
    assert filter_words_list(['love', 'home'], '____', ['m']) == ['love']
    assert filter_words_list(['love', 'home'], '____', ['l']) == ['home']
    assert filter_words_list(['love', 'hove'], '___', ['r']) == []


def test_filter_no_same_length_words():
    assert filter_no_same_length_words('____', ['love', 'home']) == ['love', 'home']
    assert filter_no_same_length_words('___', ['love', 'home']) == []
    assert filter_no_same_length_words('__', ['lo', 'home']) == ['lo']
    assert filter_no_same_length_words('_g__', ['love', 'home']) == ['love', 'home']
    assert filter_no_same_length_words('_g__', []) == []


def test_filter_incorrect_index_words():
    assert filter_incorrect_index_words('r__f', ['roof', 'mall']) == ['roof']
    assert filter_incorrect_index_words('r__f', ['roof', 'rorf']) == ['roof']
    assert filter_incorrect_index_words('___f', ['roof', 'loof']) == ['roof','loof']
    assert filter_incorrect_index_words('____', ['roof', 'mall']) == ['roof','mall']
    assert filter_incorrect_index_words('_t__', ['toof', 'malt']) == []


def test_create_pattern_from_word():
    assert create_pattern_from_word({'a', 'p'}, 'apple') == 'app__'
    assert create_pattern_from_word({'e', 'p'}, 'apple') == '_pp_e'
    assert create_pattern_from_word({'a', 'p'}, 'room') == '____'
    assert create_pattern_from_word({'f', 'p'}, 'apple') == '_pp__'
    assert create_pattern_from_word({'a', 'p', 'l', 'e'}, 'apple') == 'apple'


def test_filter_wrong_letters():
    assert filter_wrong_letters(['lo', 've'], ['r', 'f']) == ['lo', 've']
    assert filter_wrong_letters(['lo', 've'], ['o', 'f']) == ['ve']


def test_initial_the_game():
    assert initialize_the_game(10, 'home') == ([], EMPTY_MASSAGE, '____', 10)
    assert initialize_the_game(1, 'home') == ([], EMPTY_MASSAGE, '____', 1)
    assert initialize_the_game(1, '') == ([], EMPTY_MASSAGE, '', 1)


def test_process_hint_input():
    assert create_hints_words_list('__m_', ['love', 'home'], ['f']) == ['home']
    assert create_hints_words_list('__v_', ['love', 'home'], ['f']) == ['love']
    assert create_hints_words_list('____', ['lofe', 'hofe'], ['f']) == []
    assert create_hints_words_list('____', ['love', 'home'], ['l']) == ['home']


def main():
    test_update_word_pattern()
    test_check_letter_validity()
    test_check_letter_already_picked()
    test_update_score()
    test_check_if_win_or_lose()
    test_word_input()
    test_check_letter()
    test_letter_input()
    text_filter_words_list()
    test_filter_no_same_length_words()
    test_filter_incorrect_index_words()
    test_create_pattern_from_word()
    test_process_hint_input()
    test_initial_the_game()
    test_filter_wrong_letters()
    print('all tests passed')


if __name__ == '__main__':
    main()
