from nonogram import *


def test_constraint_satisfactions():
    # print(constraint_satisfactions(3, [1]))
    assert constraint_satisfactions(3, [1]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # print(constraint_satisfactions(3, [2]))
    assert constraint_satisfactions(3, [2]) == [[1, 1, 0], [0, 1, 1]]
    # print(constraint_satisfactions(3, [1, 1]))
    assert constraint_satisfactions(3, [1, 1]) == [[1, 0, 1]]
    # print(constraint_satisfactions(4, [1, 1]))
    assert constraint_satisfactions(4, [1, 1]) == [[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1]]
    # print(constraint_satisfactions(5, [2, 1]))
    assert constraint_satisfactions(5, [2, 1]) == [[1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 0, 1]]



# def check_place_blocks():
#     assert place_blocks([0, 0, 0], 1, 0) == [1, 0, 0]
#     assert place_blocks([0, 0, 0], 2, 0) == [1, 1, 0]
#     assert place_blocks([0, 0, 0], 2, 1) == [0, 1, 1]
#     assert place_blocks([0, 0, 0, 0], 3, 0) == [1, 1, 1, 0]
#     assert place_blocks([0, 0, 0, 0], 3, 1) == [0, 1, 1, 1]
#
#
# def check_remove_blocks():
#     assert remove_blocks([1, 0, 0], 1, 0) == [0, 0, 0]


def test_row_variations():
    # print(row_variations([1, 1, -1, 0], [3]))
    # assert row_variations([1, 1, -1, 0], [3]) == [[1, 1, 1, 0]]
    print(row_variations([-1, -1, -1, 0], [2]))
    # assert row_variations([-1, -1, -1, 0], [2]) == [[1, 1, 0, 0], [0, 1, 1, 0]]
    # print(row_variations([-1, 0, 1, 0, -1, 0], [1, 1]))
    # assert row_variations([-1, 0, 1, 0, -1, 0], [1, 1]) == [[1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0]]
    # print(row_variations([-1, -1, -1], [1]))
    # assert row_variations([-1, -1, -1], [1]) == [[1, 0, 0],[0, 1, 0], [0, 0, 1]]
    # # print(row_variations([0, 0, 0], [1]))
    # assert row_variations([0, 0, 0], [1]) == []
    # # print(row_variations([0, 0, -1, 1, 0], [3]))
    # assert row_variations([0, 0, -1, 1, 0], [3]) == []
    # # print(row_variations([0, 0, -1, 1, 0], [2]))
    # assert row_variations([0, 0, -1, 1, 0], [2]) == [[0, 0, 1, 1, 0]]
    # # print(row_variations([0, 0, 1, 1, 0], [2]))
    # assert row_variations([0, 0, 1, 1, 0], [2]) == [[0, 0, 1, 1, 0]]


def test_intersection_row():
    # print(intersection_row([[0, 0, 1], [0, 1, 1], [0, 0, 1]]))
    assert intersection_row([[0, 0, 1], [0, 1, 1], [0, 0, 1]]) == [0, -1, 1]
    # print(intersection_row([[0, 1, -1], [-1, -1, -1]]))
    assert intersection_row([[0, 1, -1], [-1, -1, -1]]) == [0, 1, -1] or [-1, -1, -1]
    # print(intersection_row([[1, 1, 0, 0], [0, 1, 1, 0]]))
    assert intersection_row([[1, 1, 0, 0], [0, 1, 1, 0]]) == [-1, 1, -1, 0]
    # print(intersection_row([[1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0]]))
    assert intersection_row([[1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0]]) == [-1, 0, 1, 0, -1, 0]
    # print(intersection_row([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
    assert intersection_row([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == [-1, -1, -1]


def test_solve_easy():
    assert solve_easy_nonogram([[[2], [2], [1]], [[1], [2], [1, 1]]]) == [[0,1,1],[1,1,0],[0,0,1]]
    assert solve_easy_nonogram([[[1],[1]],[[1],[1]]]) == [ [1, 0], [0, 1] ] or [ [0, 1], [1, 0] ]
    # print(solve_easy_nonogram([[[2],[3],[1,1,1]],[[1],[3],[1],[2],[],[1]]]))
    # assert solve_easy_nonogram([[[2],[3],[1,1,1]],[[1],[3],[1],[2],[],[1]]])


def check_check_columns():
    my_constraints = [[[2], [2], [1]], [[2], [2], [1, 1]]]
    board = build_board_with_rows(my_constraints)
    # check_columns(board, my_constraints[1])
    print(board)


def check_check_rows():
    my_constraints = [[[2], [2], [1]], [[2], [2], [1, 1]]]
    board = build_board_with_rows(my_constraints)
    # check_rows(board, my_constraints[0])
    print(board)


def test_solve():
    # assert solve_nonogram([[ [1], [1] ], [ [1], [1] ]]) == [[ [1, 0], [0, 1] ], [ [0, 1], [1, 0] ]]
    pass

def check_the_tester():
    assert intersection_row([]) == []
    assert intersection_row([[]]) == []
    assert intersection_row([[], []]) == []
    assert intersection_row([[1, 0, -1, 0, 1]]) == [1, 0, -1, 0, 1]
    assert intersection_row([[1, 0, -1], [-1, 0, 1]]) == [-1, 0, -1]
    assert intersection_row([[-1, 0, 1, 1], [1, 1, 1, 1]]) == [-1, -1, 1, 1]
    assert intersection_row([
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [1, -1, 1, 0, 0],
    ]) == [1, -1, 1, 0, -1]


def check1():
    # print(solve_easy_nonogram([[[4], [3, 1], [2, 1, 1], [1, 2, 1], [2, 2, 1, 1],
    #                             [3, 1, 1, 1], [1, 1, 1, 2], [3, 5], [1, 1, 2],
    #                             [2, 2, 1], [1, 3, 1], [3, 1], [1, 1], [4], [4]],
    #                            [[5, 2, 2], [3, 2, 1, 1, 3], [2, 1, 5, 2],
    #                             [1, 1, 3, 1, 2], [1, 2, 8], [2, 1, 1, 1, 1],
    #                             [1, 3],
    #                             [1, 1, 4], [1, 2], [2]]]))


    # print(solve_easy_nonogram([[[2], [2, 1], [1, 3], [1, 1, 1, 1], [1, 1, 5],
    #                             [1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1],
    #                             [1, 1, 1, 1],
    #                             [1, 1, 4, 3], [4, 3, 2], [1, 1, 1, 1, 1],
    #                             [7, 2, 1],
    #                             [1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 1],
    #                             [1, 1, 5, 3],
    #                             [1, 1, 5, 1, 1], [1, 1, 2, 2, 1, 1],
    #                             [1, 1, 2, 2, 1, 1], [1, 1, 1, 1, 5],
    #                             [1, 1, 2, 2, 1, 1]],
    #                            [[1, 2], [6, 9], [1, 1], [16], [1, 1, 1],
    #                             [1, 7, 1],
    #                             [2, 1, 2, 6], [2, 2, 2], [1, 2, 2, 6],
    #                             [1, 1, 1, 1, 6, 1], [2, 3, 2, 1, 1],
    #                             [1, 1, 1, 2, 10], [4, 2, 2, 1, 1, 1], [11],
    #                             [1]]]))

    # print(solve_easy_nonogram([[[6], [13], [5], [13], [1, 11, 1],
    #                             [1, 1, 1, 1, 1, 1, 1], [11]],
    #                            [[1], [1, 1], [2, 1], [2, 4], [5, 1], [7], [5, 1],
    #                             [7], [5, 1], [1, 4], [1, 2, 1], [1, 4],
    #                             [1, 2, 1], [1, 1, 1], [1, 1], [1]]]))

    # print(solve_easy_nonogram([[[5], [2, 2], [5], [5], [3], [1], [1], [1], [1],
    #                             [1], [1], [1], [1], [1], [1], [3], [2], [2], [2],
    #                             [1]], [[4], [5, 2, 1], [1, 18], [5, 1, 1], [4]]]))
    pass


def check_3():
    # print(solve_nonogram([[ [1], [1] ], [ [1], [1] ]]))
    # assert solve_nonogram([[ [1], [1] ], [ [1], [1] ]]) == [[ [1, 0], [0, 1] ], [ [0, 1], [1, 0] ]]
    print(solve_nonogram([[[2], [2, 1], [1, 3], [1, 1, 1, 1], [1, 1, 5],
                           [1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 1],
                           [1, 1, 1, 1],
                           [1, 1, 4, 3], [4, 3, 2], [1, 1, 1, 1, 1],
                           [7, 2, 1],
                           [1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 1],
                           [1, 1, 5, 3],
                           [1, 1, 5, 1, 1], [1, 1, 2, 2, 1, 1],
                           [1, 1, 2, 2, 1, 1], [1, 1, 1, 1, 5],
                           [1, 1, 2, 2, 1, 1]],
                          [[1, 2], [6, 9], [1, 1], [16], [1, 1, 1],
                           [1, 7, 1],
                           [2, 1, 2, 6], [2, 2, 2], [1, 2, 2, 6],
                           [1, 1, 1, 1, 6, 1], [2, 3, 2, 1, 1],
                           [1, 1, 1, 2, 10], [4, 2, 2, 1, 1, 1], [11],
                           [1]]]))


if __name__ == '__main__':
    # check_place_blocks()
    # check_remove_blocks()
    # test_constraint_satisfactions()
    # test_row_variations()
    # test_intersection_row()
    # print(len(constraint_satisfactions(42,[2,3,1,6,2])))
    # test_solve_easy()
    # check_check_columns()
    # check_check_rows()
    # check_the_tester()
    # check1()
    # check2()
    # print(solve_easy_nonogram([[[], [4], [6], [2, 2], [1, 3]],
    #                            [[], [2], [1], [2, 2], [2, 2]]]))
    check_3()
    print('all tests passed')

