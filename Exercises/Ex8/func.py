# def row_variations(row, blocks):
#     variations = []
#     _row_variations_helper(row, blocks, variations, [], 0, 0)
#     return variations[::-1]
#
#
# def _row_variations_helper(row, blocks, variations, temp_lst,row_index, block_index):
#     if row_index >= len(row):
#         if block_index >= len(blocks) or (block_index == len(blocks) - 1 and blocks[block_index] == 0) :
#             variations.append(temp_lst[:])
#         return
#
#     if row[row_index] == 0:
#         temp_lst.append(0)
#         _row_variations_helper(row, blocks, variations, temp_lst, row_index + 1, block_index)
#         temp_lst.pop()
#         return
#
#     if row[row_index] == 1:
#         if block_index >= len(blocks) or blocks[block_index] < 1:
#             return
#
#         temp_lst.append(1)
#         blocks[block_index] -= 1
#         if blocks[block_index] <= 0:
#             new_index = block_index + 1
#         if blocks[block_index] > 0:
#             new_index = block_index
#         _row_variations_helper(row, blocks, variations, temp_lst, row_index + 1, new_index)
#         blocks[block_index] += 1
#         temp_lst.pop()
#         return
#
#     temp_lst.append(0)
#     _row_variations_helper(row, blocks, variations, temp_lst, row_index + 1, block_index)
#     temp_lst.pop()
#
#     if block_index < len(blocks) and row_index <= len(row) - blocks[block_index]:
#         is_valid = True
#         for i in range(row_index, row_index+blocks[block_index]):
#             if row[i] == 0:
#                 is_valid = False
#                 break
#
#         is_last_block = block_index == len(blocks) - 1
#         if not is_last_block:
#             if row_index > len(row) - (blocks[block_index] + 1) or row[row_index + blocks[block_index]] == 1:
#                 is_valid = False
#
#         if is_valid:
#             for i in range(0, blocks[block_index]):
#                 temp_lst.append(1)
#
#             if not is_last_block:
#                 temp_lst.append(0)
#
#             if is_last_block:
#                 row_index = row_index + blocks[block_index]
#             if not is_last_block:
#                 row_index = row_index + blocks[block_index] + 1
#             _row_variations_helper(row,blocks,variations,temp_lst, row_index, block_index+1)
#
#             for i in range(0, blocks[block_index]):
#                 temp_lst.pop()
#
#             if not is_last_block:
#                 temp_lst.pop()





# if __name__ == '__main__':
#     # print(row_variations([1, 1, -1, 0], [3]))
#     assert row_variations([1, 1, -1, 0], [3]) == [[1, 1, 1, 0]]
#     print(row_variations([-1, -1, -1, 0], [2]))
#     assert row_variations([-1, -1, -1, 0], [2]) == [[1, 1, 0, 0],[0, 1, 1, 0] ]
#     print(row_variations([-1, 0, 1, 0, -1, 0], [1, 1]))
#     assert row_variations([-1, 0, 1, 0, -1, 0], [1, 1]) == [[1, 0, 1, 0, 0, 0],[0, 0, 1, 0, 1, 0] ]
#     # # print(row_variations([-1, -1, -1], [1]))
#     assert row_variations([-1, -1, -1], [1]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#     # # print(row_variations([0, 0, 0], [1]))
#     assert row_variations([0, 0, 0], [1]) == []
#     # # print(row_variations([0, 0, -1, 1, 0], [3]))
#     assert row_variations([0, 0, -1, 1, 0], [3]) == []
#     # # print(row_variations([0, 0, -1, 1, 0], [2]))
#     assert row_variations([0, 0, -1, 1, 0], [2]) == [[0, 0, 1, 1, 0]]
#     # # print(row_variations([0, 0, 1, 1, 0], [2]))
#     assert row_variations([0, 0, 1, 1, 0], [2]) == [[0, 0, 1, 1, 0]]
#     # print(row_variations([-1, -1, -1, -1, -1, -1, -1, -1], [1, 2, 1]))
#     print(row_variations([ -1, 1, 0, -1],[2]))
#     # print(row_variations([-1, -1, -1, -1, -1, -1, -1, -1], [1, 2, 1]))
#     assert row_variations([-1, -1, -1, -1, -1, -1, -1, -1], [1, 2, 1]) == [
#         [1, 0, 1, 1, 0, 1, 0, 0],
#         [1, 0, 1, 1, 0, 0, 1, 0],
#         [1, 0, 1, 1, 0, 0, 0, 1],
#         [1, 0, 0, 1, 1, 0, 1, 0],
#         [1, 0, 0, 1, 1, 0, 0, 1],
#         [1, 0, 0, 0, 1, 1, 0, 1],
#         [0, 1, 0, 1, 1, 0, 1, 0],
#         [0, 1, 0, 1, 1, 0, 0, 1],
#         [0, 1, 0, 0, 1, 1, 0, 1],
#         [0, 0, 1, 0, 1, 1, 0, 1],
#     ]