def find_ltr_diagonal_1(the_sorted_words, matrix, the_outcomes, toward):
    num_of_row = len(matrix)
    num_of_col = len(matrix[0])
    string_from_diagonal = ""
    for j in range(1, num_of_col):
        count3 = num_of_row - 1
        count4 = j
        while count3 >= 0 and count4 < num_of_col :
            string_from_diagonal += matrix[count3][count4]
            count3 -= 1
            count4 += 1
        print(string_from_diagonal)
        if toward == "w":
            the_outcomes = find_and_count(string_from_diagonal, the_sorted_words, the_outcomes)
        if toward == "z":
            the_outcomes = find_and_count(string_from_diagonal[::-1], the_sorted_words, the_outcomes)
        string_from_diagonal = ""

    return the_outcomes


def find_and_count(the_string, dictionary_of_words, finding_list):
    for i in range(len(the_string)):
        if the_string[0] in dictionary_of_words:
            for word in dictionary_of_words[the_string[0]]:
                if the_string.startswith(word):
                    if word not in finding_list:
                        finding_list[word] = 1
                    else:
                        finding_list[word] += 1
        the_string = the_string[1:]
    return finding_list



if __name__ == '__main__':
    print(find_ltr_diagonal_1(['753'],[['1','2','3'],['4','5','6'],['7','8','9']],[],'w'))