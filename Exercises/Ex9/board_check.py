from board import *
from car import Car
VERTICAL = 0
HORIZONTAL = 1
MOVE_UP = "u"
MOVE_DOWN = "d"
MOVE_LEFT = "l"
MOVE_RIGHT = "r"

if __name__ == '__main__':
    # board = [['' for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    # # print(board)
    # board = Board()
    # # print(str(board))
    # board_cell_lst = [(row, col) for row in range(BOARD_SIZE) for col in range(BOARD_SIZE)]
    # board_cell_lst.append((3,7))
    # print(board_cell_lst)
    # board = Board()
    # board.cell_content((3, 7))
    # print(board.cell_list())
    # print(str(board))
    m = [['_' for _ in range(7+1)] if i == 3 else
         ['_' for _ in range(7)]
         for i in range(7)]
    for row in m:
        print(row)

    result = ''
    for row in m:
        for item in range(len(row)):
            if item != 7:
                result += ' ' + row[item] + ' '
        result += '\n'
    print(result)

