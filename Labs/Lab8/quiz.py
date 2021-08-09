def permutations_dist(word, dist):
    lst = []
    _permutations_dist_helper(word, dist, lst, [])
    return len(lst)


def _permutations_dist_helper(word, dist, lst , seq):
    if len(seq) > 1:
        if abs((ord(seq[-1]) - ord(seq[-2]))) > dist:
            return

        if seq[-1] in seq[:-1]:
            return

    if len(seq) == len(word):
        lst.append(seq)
        print(''.join(seq))
        return

    for letter in word:
        seq.append(letter)
        _permutations_dist_helper(word, dist, lst, seq)
        seq.pop()


print(permutations_dist('abcz', 23))