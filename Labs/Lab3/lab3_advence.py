def all_ways_to_cut(sequence, words):
    partial_cuts = [[sequence]]
    for _ in range(words-1):
        partial_cuts = cut_last_word(partial_cuts)
    return partial_cuts


def cut_a_word_once(word):
    result = []
    for i in range(1,len(word)):
        result.append([word[:i], word[i:]])
    return result


def cut_last_word(list_of_partial_cuts):
    result = []
    for partial_cut in list_of_partial_cuts:
        cut = partial_cut[:-1]
        all_ways_to_expand = cut_a_word_once(partial_cut[-1])
        for expansion in all_ways_to_expand:
            result.append(cut + expansion)
    return result


all_ways = all_ways_to_cut("doggy", 2)
print(sorted(all_ways))
