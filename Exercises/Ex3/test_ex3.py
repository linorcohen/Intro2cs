import time

from ex3 import *

if __name__ == '__main__':
    # print(input_list())

    assert inner_product([1, 2, 3, 0], [1, 2, 3, 0]) == 14
    assert inner_product([1, 2, 3], [1, 2, 3]) == 14
    assert inner_product([1, 2, 3], [10.5, -2, 0]) == 6.5
    assert inner_product([1, 2, 3], []) is None
    assert inner_product([0], [0]) == 0
    assert inner_product([-10], [-5]) == 50
    assert inner_product([], [1]) is None
    assert inner_product([], []) == 0

    assert (sequence_monotonicity([1, 2, 3, 4, 5, 6, 7, 8])
            == [True, True, False, False])

    assert (sequence_monotonicity([1, 2, 2, 3])
            == [True, False, False, False])

    assert (sequence_monotonicity([1, 1, 1, 1])
            == [True, False, True, False])

    assert (sequence_monotonicity([3, 2, 1, 1])
            == [False, False, True, False])

    assert (sequence_monotonicity([7.5, 4, 3.141, 0.111])
            == [False, False, True, True])

    assert (sequence_monotonicity([1, 0, -1, 1])
            == [False, False, False, False])

    assert (sequence_monotonicity([])
            == [True, True, True, True])

    assert (sequence_monotonicity([100])
            == [True, True, True, True])

    assert (sequence_monotonicity([-10])
            == [True, True, True, True])

    assert (sequence_monotonicity([0])
            == [True, True, True, True])

    bool_def = [True, True, False, False]
    assert sequence_monotonicity(monotonicity_inverse(bool_def)) == bool_def

    bool_def = [False, False, True, True]
    assert sequence_monotonicity(monotonicity_inverse(bool_def)) == bool_def

    bool_def = [True, False, True, False]
    assert sequence_monotonicity(monotonicity_inverse(bool_def)) == bool_def

    bool_def = [True, False, False, False]
    assert sequence_monotonicity(monotonicity_inverse(bool_def)) == bool_def

    bool_def = [False, False, True, False]
    assert sequence_monotonicity(monotonicity_inverse(bool_def)) == bool_def

    bool_def = [False, False, False, False]
    assert sequence_monotonicity(monotonicity_inverse(bool_def)) == bool_def

    bool_def = [False, True, False, False]
    assert monotonicity_inverse(bool_def) is None

    bool_def = [False, False, False, True]
    assert monotonicity_inverse(bool_def) is None

    bool_def = [True, True, True, True]
    assert monotonicity_inverse(bool_def) is None

    bool_def = [False, True, True, False]
    assert monotonicity_inverse(bool_def) is None

    bool_def = [True, False, False, True]
    assert monotonicity_inverse(bool_def) is None

    assert monotonicity_inverse([True, True, True, True]) is None

    assert primes_for_asafi(0) == []
    assert primes_for_asafi(1) == [2]
    assert primes_for_asafi(2) == [2, 3]
    assert primes_for_asafi(7) == [2, 3, 5, 7, 11, 13, 17]
    assert primes_for_asafi(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                    41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                                    89, 97, 101, 103, 107, 109, 113, 127, 131,
                                    137, 139, 149, 151, 157, 163, 167, 173,
                                    179,
                                    181, 191, 193, 197, 199, 211, 223, 227,
                                    229]

    assert sum_of_vectors([[1, 1], [1, 3]]) == [2, 4]

    assert sum_of_vectors([[1, 1, 1], [1, 0, 0], [0, 0, 100]]) == [2, 1, 101]

    assert sum_of_vectors([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [2, 2, 2, 2, 2]

    assert sum_of_vectors([[], []]) == []

    assert sum_of_vectors([]) is None

    assert num_of_orthogonal([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3

    assert num_of_orthogonal([[0, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3

    assert num_of_orthogonal([[0, 0], [1, 2], [10, 5]]) == 2

    assert num_of_orthogonal([[1, 1, 1, 1],
                              [2, 1, 3, 3],
                              [0, 0, 100, 33],
                              [8, 8, 8, 1.5],
                              [9, 9, 9, 9]]) == 0

    assert num_of_orthogonal([[0], [0], [0], [0]]) == 6
    # start = time.process_time()
    # primes_for_asafi(50000)
    # end = time.process_time()
    # print(end-start)
    # start_2 = time.process_time()
    # primes_for_asafi(50000)
    # end_2 = time.process_time()
    # print(end_2 - start_2)

print('all tests passed')
