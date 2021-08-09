#
# def diagonal_raise(columns, matrix, columns_direction):
#     """
#     This function returns a list of organized matrix lines joined in the
#     direction of diagonal raise left or right according to the columns_direction.
#     :param columns: number of columns in matrix
#     :type columns: int
#     :param matrix: 2D list of the matrix letters
#     :type matrix: list[list[str]]
#     :param columns_direction: list of columns direction
#     :type columns_direction: list[int]
#     :return: list of organized matrix lines joined
#     :rtype: list[str]
#     """
#     # [1,2,3]      rise right                  rise left
#     # [4,5,6] ---> ['1','42','753','86','9'] / ['3','62','951','84','7']
#     # [7,8,9]
#     rows = len(matrix)
#     number_of_diagonals = rows + columns - 1
#     diagonal_matrix = [[] for i in range(number_of_diagonals)]
#     diagonal_matrix_index = 0
#     for column in columns_direction:
#         m = diagonal_matrix_index
#         for row in range(rows):
#             diagonal_matrix[m].append(matrix[row][column])
#             m += 1
#         diagonal_matrix_index += 1
#     return [''.join(lst) for lst in diagonal_matrix]

# def main_diagonal_search(matrix, direction):
#     columns = len(matrix[0])
#     if direction == 'w':  # ↗
#         columns_direction = range(columns)  # [0, 1, 2, 3]
#         return diagonal_raise(columns, matrix, columns_direction)
#     if direction == 'x':   # ↖
#         columns_direction = reversed(range(columns))  # [3, 2, 1, 0]
#         return diagonal_raise(columns, matrix, columns_direction)
#     if direction == 'z':  # ↙
#         columns_direction = range(columns)
#         raise_st = diagonal_raise(columns, matrix, columns_direction)
#         return diagonal_descends(raise_st)
#     if direction == 'y':  # ↘
#         columns_direction = reversed(range(columns))
#         raise_st = diagonal_raise(columns, matrix, columns_direction)
#         return diagonal_descends(raise_st)
#
#
# def diagonal_raise(columns, matrix, columns_direction):
#     rows = len(matrix)
#     diagonal_matrix = [[] for i in range(rows + columns - 1)]
#     n = 0
#     for i in columns_direction:
#         m = n
#         for j in range(rows):
#             diagonal_matrix[m].append(matrix[j][i])
#             m += 1
#         n += 1
#     return [''.join(lst) for lst in diagonal_matrix]
#
#
# def diagonal_descends(raise_list):
#     return [string[::-1] for string in raise_list]

