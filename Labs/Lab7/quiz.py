def exp_n_x(n, x):
    if n < 0:
        return None
    if n == 0:
        return 1
    return (x ** (n)) / factorial(n) + exp_n_x(n - 1, x)


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


DIRECTION = {'u': (0, 1), 'r': (1, 0)}


def up_and_right(n, k, lst):
    _up_and_right_helper((0, 0), n, k, lst, '')


def _up_and_right_helper(position, n, k, lst, path):
    if position[0] == n and position[1] == k:
        lst.append(path)
        return

    if position[0] > n or position[1] > k:
        return

    for direction in DIRECTION:
        path = path + direction
        new_position = move(position, DIRECTION[direction])
        _up_and_right_helper(new_position, n, k, lst, path)
        path = path[:-1]


def move(position, move):
    return position[0] + move[0], position[1] + move[1]


def count_sp_ways(x, n):
    print(_count_sp_ways_helper(x, n, 1, []))


def _count_sp_ways_helper(x, n, num, numbers):
    if num in numbers:
        return _count_sp_ways_helper(x, n, num + 1,
                                     numbers) + _count_sp_ways_helper(x, n,
                                                                      num + 1,
                                                                      [])
    sum_ = x - pow(num, n)
    if sum_ < 0:
        return 0

    if sum_ == 0:
        return 1

    return _count_sp_ways_helper(sum_, n, num + 1,
                                 numbers) + _count_sp_ways_helper(x, n,
                                                                  num + 1, [])


def all_paren(n, pairs):
    return _all_paren_helper(n, pairs, 0, [], [])


def _all_paren_helper(n, pairs, index, lst, comin):
    if n == 0:
        return ['']

    if ''.join(comin) in lst:
        return

    if len(comin) == n*2:
        lst.append(''.join(comin))
        return

    for pair in pairs:
        comin = comin[0:index] + list(pair) + comin[index:]
        _all_paren_helper(n, pairs, index+1, lst, comin)
        _all_paren_helper(n, pairs, index+1, lst, comin)

    return lst


if __name__ == '__main__':
    print(all_paren(2,['[]','{}']))

