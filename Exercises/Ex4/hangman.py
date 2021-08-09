#################################################################
# FILE : hangman.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex4 2021
# DESCRIPTION: A simple program that operates the game hangman.
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
import hangman_helper as helper

EMPTY_MASSAGE = ''
WIN_MASSAGE = 'You won the game!'
LOSE_MASSAGE = 'You lost the game. The word was '
LETTER_INVALID_MASSAGE = 'The letter you entered is invalid.'
LETTER_ALREADY_PICKED_MASSAGE = 'The letter you entered was already chosen.'
PLAY_AGAIN_MASSAGE = 'Number of games so far: {} . Your current score: {}. Want to continue?'
START_OVER_MASSAGE = 'Number of games survived: {}. Start a new series of games?'


def run_single_game(words_list, score):
    """
    This function operates a single game of hangman.
    :param words_list: a list of words to pick
    :type words_list: list of str
    :param score: the initial score
    :type score: int
    :return: final score from a single game
    :rtype: int
    """
    word = helper.get_random_word(words_list)
    wrong_guess_lst, msg, pattern, points = initialize_the_game(score, word)

    while pattern != word and points > 0:
        helper.display_state(pattern, wrong_guess_lst, points, msg)
        type_input, user_input = helper.get_input()  # get input from the user
        msg = EMPTY_MASSAGE
        # user choose to get hint:
        if type_input == helper.HINT:
            points -= 1  # decrease a point for asking hint
            hints_words_list = create_hints_words_list(pattern, words_list, wrong_guess_lst)
            helper.show_suggestions(hints_words_list)
        # user choose word to guess:
        elif type_input == helper.WORD:
            points -= 1  # decrease a point for guessing a word
            pattern, points = process_word_input(pattern, points, user_input, word)
        # user choose to guess letter:
        elif type_input == helper.LETTER:
            msg = check_if_letter_can_be_used(user_input, wrong_guess_lst, pattern)
            if msg == EMPTY_MASSAGE:  # letter can be used
                points -= 1  # decrease a point for guessing a letter
                pattern, points = process_letter_input(points, user_input, word,
                                                       pattern, wrong_guess_lst)
    # end of a single game
    msg = check_if_win_or_lose(pattern, word)
    helper.display_state(pattern, wrong_guess_lst, points, msg)
    return points


def main():
    """
    This function operates the game hangman. runs a single game as long as
    the user chooses to continue play.
    """
    words_list = helper.load_words('words.txt')
    game_status = True  # game is active
    while game_status:
        points = run_single_game(words_list, helper.POINTS_INITIAL)  # first game
        num_of_games = 1

        # plays a series of single games until the player has 0 points:
        while points > 0:
            # player decide if to play another game:
            if not helper.play_again(PLAY_AGAIN_MASSAGE.format(num_of_games, points)):
                game_status = False  # game is no longer active
                break
            num_of_games += 1
            points = run_single_game(words_list, points)

        # player got to 0 points and asked if wants to start over the game:
        if points == 0:
            game_status = helper.play_again(START_OVER_MASSAGE.format(num_of_games))


def update_word_pattern(word, pattern, letter):
    """
    This function updates the pattern according to the letter given.
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
    :param wrong_guess_lst: list of wrong guesses
    :type wrong_guess_lst: list of str
    :param pattern: the current pattern
    :type pattern: str
    :return: True if letter was already picked, else False.
    :rtype: bool
    """
    if letter in wrong_guess_lst or letter in pattern:
        return True
    return False


def returns_points_calculation(points, n):
    """
    This function returns the calculation of the players points by the number
    of letters match.
    :param points: the current points
    :type points: int
    :param n: number of letters match
    :type n: int
    :return: the updated points
    :rtype: int
    """
    return points + (n * (n + 1) // 2)


def check_if_win_or_lose(pattern, word):
    """
    This function checks if the player won or lost and returns a massage
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


def process_word_input(pattern, points, word_guessed, word):
    """
    This function checks if the guessed word is correct.
    if correct - returns the word and the new points of the player.
    if not correct - returns the pattern, and points without a change.
    :param pattern: the current pattern
    :type pattern: str
    :param points: the current points
    :type points: int
    :param word_guessed: user guessed word
    :type word_guessed: str
    :param word: word to guess
    :type word: str
    :return: pattern, points
    :rtype: (str,int)
    """
    if word_guessed == word:
        n = pattern.count('_')
        new_points = returns_points_calculation(points, n)
        return word, new_points
    return pattern, points


def check_if_letter_can_be_used(letter, wrong_guess_lst, pattern):
    """
    This function checks if the given letter is valid or already picked and
    returns a massage accordingly. else, returns empty string.
    :param letter: a letter
    :type letter: str
    :param wrong_guess_lst: list of wrong guesses
    :type wrong_guess_lst: list of str
    :param pattern: the current pattern
    :type pattern: str
    :return: massage
    :rtype: str
    """
    msg = EMPTY_MASSAGE
    if check_letter_validity(letter) is False:
        msg = LETTER_INVALID_MASSAGE
    elif check_letter_already_picked(letter, wrong_guess_lst, pattern):
        msg = LETTER_ALREADY_PICKED_MASSAGE
    return msg


def process_letter_input(points, letter, word, pattern, wrong_guess_lst):
    """
    This function check if the letter is in the word:
    if letter in word - returns new pattern, and the new points of the player.
    if letter not in word - add letter to wrong_guess_lst and returns the
    pattern and points unchanged.
    :param points: the current points
    :type points: int
    :param letter: a letter
    :type letter: str
    :param word: word to guess
    :type word: str
    :param pattern: the current pattern
    :type pattern: str
    :param wrong_guess_lst: list of wrong guesses
    :type wrong_guess_lst: list of str
    :return: pattern, points
    :rtype: (str, int)
    """
    if letter in word:
        n = word.count(letter)
        new_points = returns_points_calculation(points, n)
        new_pattern = update_word_pattern(word, pattern, letter)
        return new_pattern, new_points
    wrong_guess_lst.append(letter)
    return pattern, points


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    This function filters from the list of words given only the words that can
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
    that are in the same length as the pattern.
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
    that has the same letters in the same index as the pattern.
    :param pattern: the current pattern
    :type pattern: str
    :param words_lst: a list of words
    :type words_lst: list of str
    :return: list of words with the same letters in the same index as the pattern
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
    that don't contain letters from the wrong_guess_lst.
    :param words_lst: a list of words
    :type words_lst: list of str
    :param wrong_guess_lst: list of wrong guessed letters
    :type wrong_guess_lst: list of str
    :return: list of words that don't contain letters from wrong guess lst
    :rtype: list of str
    """
    return [word for word in words_lst if
            any(i for i in word if i in wrong_guess_lst) is False]


def initialize_the_game(score, word):
    """
    This function initialize the game start values.
    :param score: the initial score
    :type score: int
    :param word: the word to guess
    :type word: str
    :return: wrong guess list, massage, word pattern, points
    :rtype: (list, str, str, int)
    """
    wrong_guess_lst = []
    msg = EMPTY_MASSAGE
    pattern = '_' * len(word)
    return wrong_guess_lst, msg, pattern, score


def create_hints_words_list(pattern, hints_words_list, wrong_guess_lst):
    """
    This function returns a list of three (or less) hints words that can
    fit the pattern.
    :param pattern: the current pattern
    :type pattern: str
    :param hints_words_list: a list of words
    :type hints_words_list: list of str
    :param wrong_guess_lst: list of wrong guessed letters
    :type wrong_guess_lst: list of str
    :return: a list of three (or less) optional words
    :rtype: list of str
    """
    hints_words_list = filter_words_list(hints_words_list, pattern, wrong_guess_lst)
    if len(hints_words_list) > helper.HINT_LENGTH:
        n = len(hints_words_list)
        hints_words_list = [hints_words_list[i * n // helper.HINT_LENGTH]
                            for i in range(helper.HINT_LENGTH)]
    return hints_words_list


if __name__ == '__main__':
    main()
