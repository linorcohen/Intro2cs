# from typing import List
#
# def return_list_according_to_directions(direction: str, matrix_copy: List[List[str]]) -> List[str]:
#     if direction == 'u':  # ↑
#         return up(matrix_copy)
#     if direction == 'd':  # ↓
#         return down(matrix_copy)
#     if direction == 'r':  # →
#         return right(matrix_copy)
#     if direction == 'l':  # ←
#         return left(matrix_copy)
#     if direction == 'w':  # ↗
#         return diagonal_rise_right(matrix_copy)
#     if direction == 'x':  # ↖
#         return diagonal_rise_left(matrix_copy)
#     if direction == 'y':  # ↘
#         return diagonal_descends_right(matrix_copy)
#     if direction == 'z':  # ↙
#         return diagonal_descends_left(matrix_copy)
#
#
# def diagonal_rise_left(matrix: List[List[str]]) -> List[str]:  # ↖
#     rows = len(matrix)
#     columns = len(matrix[0])
#     diagonal_matrix = [[] for i in range(rows + columns - 1)]
#     n = 0
#     for i in reversed(range(columns)):
#         m = n
#         for j in range(rows):
#             diagonal_matrix[m].append(matrix[j][i])
#             m += 1
#         n += 1
#     return [''.join(lst) for lst in diagonal_matrix]
#
#
# # duplicate code
# def diagonal_descends_right(matrix: List[List[str]]) -> List[str]:  # ↘
#     return [string[::-1] for string in diagonal_rise_left(matrix)]
#
#
# def diagonal_rise_right(matrix: List[List[str]]) -> List[str]:  # ↗
#     rows = len(matrix)
#     columns = len(matrix[0])
#     diagonal_left_matrix = [[] for i in range(rows + columns - 1)]
#     n = 0
#     for i in range(columns):
#         m = n
#         for j in range(rows):
#             diagonal_left_matrix[m].append(matrix[j][i])
#             m += 1
#         n += 1
#     return [''.join(lst) for lst in diagonal_left_matrix]
#
#
# def diagonal_descends_left(matrix: List[List[str]]) -> List[str]:  # ↙
#     return [string[::-1] for string in diagonal_rise_right(matrix)]
#
#
# def up(matrix: List[List[str]]) -> List[str]:  # ↑
#     up_order_matrix = [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]
#     return [''.join(lst) for lst in up_order_matrix]
#
#
# def down(matrix: List[List[str]]) -> List[str]:  # ↓
#     down_order_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
#     return [''.join(lst) for lst in down_order_matrix]
#
#
# def right(matrix: List[List[str]]) -> List[str]:  # →
#     return [''.join(lst) for lst in matrix]
#
#
# def left(matrix: List[List[str]]) -> List[str]:  # ←
#     return [''.join(lst[::-1]) for lst in matrix]
