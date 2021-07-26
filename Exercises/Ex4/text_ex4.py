from hangman import *

if __name__ == '__main__':
    def test_update_word_pattern():
        assert update_word_pattern('apple', '___l_', 'p') == '_ppl_'
        assert update_word_pattern('apple', '___l_', 'a') == 'a__l_'
        assert update_word_pattern('apple', '___l_', 'm') == '___l_'


def main():
    test_update_word_pattern()
    print('all tests passed')


if __name__ == '__main__':
    main()
