#################################################################
# FILE : hangman_dict.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex4 2021
# DESCRIPTION: A simple program that operates the game hangman.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
from hangman_helper import *

GENERAL_MASSAGE = ''
WIN_MASSAGE = 'You won the game!'
LOSE_MASSAGE = 'You lost the game. The word was '
LETTER_INVALID_MASSAGE = 'The letter you entered is invalid.'
LETTER_ALREADY_PICKED_MESSAGE = 'The letter you entered was already chosen.'
PLAY_AGAIN_MASSAGE = 'Number of games so far: {} . ' \
                     'Your current score: {}. Want to continue?'
START_OVER_MASSAGE = 'Number of games survived: {}. ' \
                     'Start a new series of games?'


def run_single_game(words_list, score):
    """
    This function operates the a single game of hangman.
    :param words_list: a list of words to pick
    :type words_list: list of str
    :param score: the initial score
    :type score: int
    :return: final score
    :rtype: int
    """
    word = get_random_word(words_list)
    wrong_guess_lst, msg, pattern, points = initial_the_game(score, word)
    while pattern != word and points > 0:
        display_state(pattern, wrong_guess_lst, points, msg)
        type_input, user_input = get_input()
        msg = GENERAL_MASSAGE
        if type_input == HINT:
            points, hint_lst = hint_input(points, words_list, pattern,
                                          wrong_guess_lst)
            show_suggestions(hint_lst)
        elif type_input == WORD:
            pattern, points = word_input(pattern, points, user_input, word)
        elif type_input == LETTER:
            msg = check_if_letter_can_be_used(user_input, wrong_guess_lst, pattern)
            if msg == GENERAL_MASSAGE:
                pattern, points = letter_input(points, user_input, word,
                                               pattern, wrong_guess_lst)
    msg = check_if_win_or_lose(pattern, word)
    display_state(pattern, wrong_guess_lst, points, msg)
    return points


def main():
    """
    This function operates the game hangman. runs the single game as long as
    the user chooses.
    """
    words_list = load_words('words.txt')
    game_status = True
    while game_status:
        initial_score = POINTS_INITIAL
        num_of_games = 1
        points = run_single_game(words_list, initial_score)
        while points > 0:
            if play_again(PLAY_AGAIN_MASSAGE.format(num_of_games, points)) is False:
                game_status = False
                break
            num_of_games += 1
            points = run_single_game(words_list, points)

        if points == 0:
            game_status = play_again(START_OVER_MASSAGE.format(num_of_games))


def update_word_pattern(word, pattern, letter):
    """
    This function update the pattern according to the letter given.
    :param word: word to guess
    :type word: str
    :param pattern: the current pattern
    :type pattern: str
    :param letter: letter to update
    :type letter: str
    :return: pattern updated with the letter
    :rtype: str
    """
    new_pattern = list(pattern)
    for i in range(len(word)):
        if word[i] == letter:
            new_pattern[i] = letter
    return ''.join(new_pattern)


def check_letter_validity(letter):
    """
    This function checks if the given letter is valid.
    :param letter: a letter
    :type letter: str
    :return: True if the letter is valid, else False.
    :rtype: bool
    """
    if len(letter) > 1 or not letter.isalpha() or letter.isupper():
        return False
    return True


def check_letter_already_picked(letter, wrong_guess_lst, pattern):
    """
    This function checks if the given letter was already picked.
    :param letter: a letter
    :type letter: str
    :param wrong_guess_lst: list of wrong hints
    :type wrong_guess_lst: list of str
    :param pattern: the current pattern
    :type pattern: str
    :return: True if letter was already picked, else False.
    :rtype: bool
    """
    if letter in wrong_guess_lst or letter in pattern:
        return True
    return False


def update_score(points, n):
    """
    This function updates the score or the player with the number of
    letters match.
    :param points: the current score
    :type points: int
    :param n: number of letters match
    :type n: int
    :return: the updated score
    :rtype: int
    """
    return points + (n * (n + 1) // 2)


def update_wrong_hints(wrong_guess_lst, letter):
    """
    This function updates the wrong hints list.
    :param wrong_guess_lst: list of wrong hints
    :type wrong_guess_lst: list of str
    :param letter: a letter
    :type letter: str
    """
    wrong_guess_lst.append(letter)


def check_if_win_or_lose(pattern, word):
    """
    This function checks if the player won or lost and returns a message
    accordingly.
    :param pattern: the current pattern
    :type pattern: str
    :param word: the word to guess
    :type word: str
    :return: win massage, else lose massage
    :rtype: str
    """
    if pattern == word:
        return WIN_MASSAGE
    return LOSE_MASSAGE + word


def word_input(pattern, points, word_guessed, word):
    """
    This function updates the pattern and points according to the guessed word.
    :param pattern: the current pattern
    :type pattern: str
    :param points: the current score
    :type points: int
    :param word_guessed: user guessed word
    :type word_guessed: str
    :param word: word to guess
    :type word: str
    :return: updated pattern, updated points
    :rtype: (str,int)
    """
    points -= 1
    if word_guessed == word:
        n = pattern.count('_')
        points = update_score(points, n)
        pattern = word
    return pattern, points


def check_if_letter_can_be_used(letter, wrong_guess_lst, pattern):
    """
    This function checks if the given letter is valid or already picked returns
    a massage accordingly.
    :param letter: a letter
    :type letter: str
    :param wrong_guess_lst: list of wrong hints
    :type wrong_guess_lst: list of str
    :param pattern: the current pattern
    :type pattern: str
    :return: massage
    :rtype: str
    """
    msg = GENERAL_MASSAGE
    if check_letter_validity(letter) is False:
        msg = LETTER_INVALID_MASSAGE
    elif check_letter_already_picked(letter, wrong_guess_lst, pattern):
        msg = LETTER_ALREADY_PICKED_MESSAGE
    return msg


def letter_input(points, letter, word, pattern, wrong_guess_lst):
    """
    This function updates the pattern and points according to the guessed
    letter. if the letter is incorrect, updates the wrong hints list.
    :param points: the current score
    :type points: int
    :param letter: a letter
    :type letter: str
    :param word: word to guess
    :type word: str
    :param pattern: the current pattern
    :type pattern: str
    :param wrong_guess_lst: list of wrong hints
    :type wrong_guess_lst: list of str
    :return: updated pattern, updated points
    :rtype: (str, int)
    """
    points -= 1
    if letter in word:
        n = word.count(letter)
        points = update_score(points, n)
        pattern = update_word_pattern(word, pattern, letter)
        return pattern, points
    update_wrong_hints(wrong_guess_lst, letter)
    return pattern, points


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    This function filters from the words given only the words that can
    fit the pattern and returns them in a list.
    :param words: a list of words
    :type words: list of str
    :param pattern: the current pattern
    :type pattern: str
    :param wrong_guess_lst: list of wrong guessed letters
    :type wrong_guess_lst: list of str
    :return: list of filtered words
    :rtype: list of str
    """
    same_length_lst = filter_no_same_length_words(pattern, words)
    same_index_lst = filter_incorrect_index_words(pattern, same_length_lst)
    no_guess_letter_lst = filter_wrong_letters(same_index_lst, wrong_guess_lst)
    return no_guess_letter_lst


def filter_no_same_length_words(pattern, words_lst):
    """
    This function returns a list of all the words from the given words list
    that are in the same length of the pattern.
    :param pattern: the current pattern
    :type pattern: str
    :param words_lst: a list of words
    :type words_lst: list of str
    :return: list of words in the same length of the pattern
    :rtype: list of str
    """
    return [word for word in words_lst if len(word) == len(pattern)]


def filter_incorrect_index_words(pattern, words_lst):
    """
    This function returns a list of all the words from the given words list
    that has the same letters as the pattern and in the same place.
    :param pattern: the current pattern
    :type pattern: str
    :param words_lst: a list of words
    :type words_lst: list of str
    :return: list of words with the same letters in the same place as the pattern
    :rtype: list of str
    """
    set_letters = set(pattern.replace('_', ''))  # letters shown in the pattern
    return [word for word in words_lst if
            create_pattern_from_word(set_letters, word) == pattern]


def create_pattern_from_word(letters_set, word):
    """
    This function creates a pattern from the given word with only the letters
    from the letters_set are shown.
    :param letters_set: a set of letters
    :type letters_set: set of str
    :param word: a word
    :type word: str
    :return: pattern po the word
    :rtype: str
    """
    pattern = ['_' if letter not in letters_set else letter for letter in word]
    return ''.join(pattern)


def filter_wrong_letters(words_lst, wrong_guess_lst):
    """
    This function returns a list of all the words from the given words list
    that don't contain letters from wrong guess lst.
    :param words_lst: a list of words
    :type words_lst: list of str
    :param wrong_guess_lst: list of wrong letters
    :type wrong_guess_lst: list of str
    :return: list of words that don't contain letters from wrong guess lst
    :rtype: list of str
    """
    return [word for word in words_lst if
            any(i for i in word if i in wrong_guess_lst) is False]


def initial_the_game(score, word):
    """
    This function initials the game start values.
    :param score: the initial score
    :type score: int
    :param word: the word to guess
    :type word: str
    :return: wrong hints, massage, word pattern, points
    :rtype: (list, str, str, int)
    """
    wrong_guess_lst = []
    msg = GENERAL_MASSAGE
    pattern = '_' * len(word)
    points = score
    return wrong_guess_lst, msg, pattern, points


def hint_input(points, words_lst, pattern, wrong_guess_lst):
    """
    This function decrease one pont from the player points and returns
    optional list of words.
    :param points: the current score
    :type points: int
    :param words_lst: a list of words
    :type words_lst: list of str
    :param pattern: the current pattern
    :type pattern: str
    :param wrong_guess_lst: list of wrong letters
    :type wrong_guess_lst: list of str
    :return: updated points, list of hints words
    :rtype: (int, list or str)
    """
    points -= 1
    optional_words_lst = create_optional_list(pattern, words_lst, wrong_guess_lst)
    return points, optional_words_lst


def create_optional_list(pattern, words_lst, wrong_guess_lst):
    """
    This function returns a list of three (or less) optional words that can
    fit the pattern.
    :param pattern: the current pattern
    :type pattern: str
    :param words_lst: a list of words
    :type words_lst: list of str
    :param wrong_guess_lst: list of wrong letters
    :type wrong_guess_lst: list of str
    :return: a list of three (or less) optional words
    :rtype: list of str
    """
    words_lst = filter_words_list(words_lst, pattern, wrong_guess_lst)
    if len(words_lst) > HINT_LENGTH:
        n = len(words_lst)
        words_lst = [words_lst[i * n // HINT_LENGTH] for i in range(HINT_LENGTH)]
    return words_lst


if __name__ == '__main__':
    main()
