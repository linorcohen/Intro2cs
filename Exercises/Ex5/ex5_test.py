from wordsearch import *
import filecmp


def test_parameters_validity():
    assert check_input_args(['a', 'b', 'c']) == INVALID_NUM_OF_PARAMETERS_MASSAGE
    assert check_input_args(['a']) == INVALID_NUM_OF_PARAMETERS_MASSAGE
    assert check_input_args(['a', 'b']) == INVALID_NUM_OF_PARAMETERS_MASSAGE
    assert check_input_args(['a.txt', 'b', 'c', 'v']) == NO_FILE_MASSAGE
    assert check_input_args(['a.txt', 'b.txt', 'c', 'v']) == NO_FILE_MASSAGE
    assert check_input_args(['a', 'b.txt', 'c', 'v']) == NO_FILE_MASSAGE
    assert check_input_args(['exists.txt', 'exists.txt', 'c', 'u']) is None
    assert check_input_args(['exists.txt', 'a.txt', 'c', 'v']) == NO_FILE_MASSAGE
    assert check_input_args(['a.txt', 'exists.txt', 'c', 'v']) == NO_FILE_MASSAGE
    assert check_input_args(['exists.txt', 'exists.txt', 'a.txt', 'ud']) is None
    assert check_input_args(['exists.txt', 'exists.txt', 'a.txt', 'up']) == ILLEGAL_DIRECTIONS
    assert check_input_args(['exists.txt', 'exists.txt', 'a.txt', 'i']) == ILLEGAL_DIRECTIONS
    assert check_input_args(['exists.txt', 'exists.txt', 'a.txt', 'udwll']) is None
    assert check_input_args(['exists.txt', 'exists.txt', 'a.txt', 'udwlli']) == ILLEGAL_DIRECTIONS

# upper letter?


def test_contain_only_legal_directions():
    assert contain_only_legal_directions('udrl') is True
    assert contain_only_legal_directions('u') is True
    assert contain_only_legal_directions('udrlll') is True
    assert contain_only_legal_directions('ludrl') is True
    assert contain_only_legal_directions('udr4') is False
    assert contain_only_legal_directions('udr ') is False
    assert contain_only_legal_directions('udr#') is False
    assert contain_only_legal_directions('udrm') is False


def test_read_wordlist():
    print(read_wordlist('word_list_test_2.txt'))


def test_read_matrix():
    print(read_matrix('mat.txt'))


def test_count_words():
    dict1 = {}
    count_words(['astoee'], ['toe'], dict1)
    assert dict1 == {'toe': 1}
    dict2 = {'toe': 1}
    count_words(['astoee'], ['toe'], dict2)
    assert dict2 == {'toe': 2}
    dict3 = {'toe': 1}
    count_words(['astoee'], ['pop'], dict3)
    assert dict3 == {'toe': 1}


words_lst_test = read_wordlist('words_list_test.txt')
matrix_file_test = read_matrix('mat_test.txt')


def test_right():
    dict1 = {}
    lst = create_right_direction_list(matrix_file_test)
    count_words(lst, words_lst_test, dict1)
    assert dict1 == {'apple': 1}


def test_left():
    dict1 = {}
    lst = create_left_direction_list(matrix_file_test)
    count_words(lst, words_lst_test, dict1)
    assert dict1 == {'dog': 1, 'cat': 1}


def test_up():
    dict1 = {}
    lst = create_up_direction_list(matrix_file_test)
    count_words(lst, words_lst_test, dict1)
    assert dict1 == {'toe': 1}


def tes_down():
    dict1 = {}
    lst = create_down_direction_list(matrix_file_test)
    count_words(lst, words_lst_test, dict1)
    assert dict1 == {'poet': 1}


def test_diagonal_rise_right():  # ↗
    # print(diagonal_rise_right(matrix_file_test))
    dict1 = {}
    lst = diagonal_search(matrix_file_test, 'w')
    count_words(lst, words_lst_test, dict1)
    assert dict1 == {'cat': 1}


def test_diagonal_rise_left():  # ↖
    # print(diagonal_rise_left(matrix_file_test))
    dict1 = {}
    lst = diagonal_search(matrix_file_test, 'x')
    count_words(lst, words_lst_test, dict1)
    assert dict1 == {'crop': 1, 'can': 1}


def test_diagonal_decrease_left():  # ↙
    # print(diagonal_descends_left(matrix_file_test))
    dict1 = {}
    lst = diagonal_search(matrix_file_test, 'z')
    count_words(lst, words_lst_test, dict1)
    assert dict1 == {'long': 1}


def test_diagonal_decrease_right():  # ↘
    # print(diagonal_descends_right(matrix_file_test))
    dict1 = {}
    lst = diagonal_search(matrix_file_test, 'y')
    count_words(lst, words_lst_test, dict1)
    assert dict1 == {'ants': 1}


def test_find_words():
    assert find_words(words_lst_test, matrix_file_test, 'wl') == [('dog', 1), ('cat', 2)]


def test_write_output():
    write_output([('cat', 1), ('dog', 1)], 'output_file_test.txt')
    write_output([], 'output_file_test.txt')


def test_file_results():
    main(['word_list.txt', 'mat.txt', 'd', 'test_files/test_d.txt'])
    main(['word_list.txt', 'mat.txt', 'l', 'test_files/test_l.txt'])
    main(['word_list.txt', 'mat.txt', 'r', 'test_files/test_r.txt'])
    main(['word_list.txt', 'mat.txt', 'u', 'test_files/test_u.txt'])
    main(['word_list.txt', 'mat.txt', 'udlrwxyz', 'test_files/test_udlrwxyz.txt'])
    main(['word_list.txt', 'mat.txt', 'w', 'test_files/test_w.txt'])
    main(['word_list.txt', 'mat.txt', 'x', 'test_files/test_x.txt'])
    main(['word_list.txt', 'mat.txt', 'y', 'test_files/test_y.txt'])
    main(['word_list.txt', 'mat.txt', 'z', 'test_files/test_z.txt'])


def check_error_1():
    words_lst = read_wordlist('Ex5-Examples/words.txt')
    mat = read_matrix('Ex5-Examples/matrix.txt')
    print(find_words(words_lst, mat, 'd'))
    print(find_words(words_lst, mat, 'l'))
    print(find_words(words_lst, mat, 'r'))
    print(find_words(words_lst, mat, 'u'))
    print(find_words(words_lst, mat, 'w'))
    print(find_words(words_lst, mat, 'x'))
    print(find_words(words_lst, mat, 'y'))
    print(find_words(words_lst, mat, 'z'))


def test():
    assert find_words(['dog', 'god'], [['f', 'n','d','o','g','i']], 'rl') == [('god', 1), ('dog', 1)]
    assert find_words(['bob'], [['b'], ['o'], ['b'], ['o'], ['b']], 'u') == [('bob', 2)]
    assert find_words(['bob'], [['b'], ['o'], ['b'], ['o'], ['b']], 'ud') == [('bob', 4)]
    assert find_words(['bob','cat','bobcat'], [['b', 'o','b','c','a','t']], 'rl') == [('bob', 2),('cat',1),('bobcat',1)]
    assert find_words(['red'], [['d'], ['e'], ['r'], ['e'], ['d']], 'ud') == [('red', 2)]


if __name__ == '__main__':
    # test_parameters_validity()
    # test_contain_only_legal_directions()
    test_read_wordlist()
    # test_read_matrix()
    # test_matrix_to_list_of_str()
    # test_count_words()
    # test_right()
    # test_left()
    # tes_down()
    # test_up()
    # test_write_output()
    # test_diagonal_rise_left()
    # test_diagonal_rise_right()
    # test_diagonal_decrease_left()
    # test_diagonal_decrease_right()
    # test_find_words()
    # test_file_results()
    # check_error_1()
    # test()
    print('all tests passed')
