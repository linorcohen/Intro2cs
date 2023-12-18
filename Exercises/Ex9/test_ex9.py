from car import Car
from board import Board
from game import Game

MIN_LENGTH = 2
MAX_LENGTH = 4
HORIZONTAL = 1
VERTICAL = 0
MOVE_UP = "u"
MOVE_DOWN = "d"
MOVE_LEFT = "l"
MOVE_RIGHT = "r"


def test_1():
    car1 = Car("test", 4, (2, 2), VERTICAL)
    car2 = Car("test", 4, (2, 2), HORIZONTAL)
    assert car1.car_coordinates() == [(2, 2), (3, 2), (4, 2), (5, 2)]
    assert car2.car_coordinates() == [(2, 2), (2, 3), (2, 4), (2, 5)]
    car3 = Car('test', 2, (-1, -1), HORIZONTAL)
    car4 = Car('test', 2, (-1, -1), VERTICAL)
    assert car3.car_coordinates() == [(-1, -1), (-1, 0)]
    assert car4.car_coordinates() == [(-1, -1), (0, -1)]
    car5 = Car('test', 0, (0, 0), HORIZONTAL)
    car6 = Car('test', 3, (0, 0), 3)
    assert car5.car_coordinates() == []
    assert car6.car_coordinates() == []

    horizontal_move = {'l': 'cause the car to move to the left',
                       'r': 'cause the car to move to the right'}
    vertical_moves = {'u': 'cause the car to move to up',
                      'd': 'cause the car to move to down'}
    assert car1.possible_moves() == vertical_moves
    assert car2.possible_moves() == horizontal_move
    assert car3.possible_moves() == horizontal_move
    assert car4.possible_moves() == vertical_moves
    assert car5.possible_moves() == horizontal_move
    assert car6.possible_moves() == {}

    assert car1.movement_requirements('u') == [(1, 2)]
    assert car1.movement_requirements('d') == [(6, 2)]
    assert car1.movement_requirements('l') == []
    assert car2.movement_requirements('u') == []
    assert car2.movement_requirements('l') == [(2, 1)]
    assert car2.movement_requirements('r') == [(2, 6)]
    assert car3.movement_requirements('u') == []
    assert car5.movement_requirements('r') == []

    car = Car("woot", 2, (0, 0), HORIZONTAL)
    assert car.move(MOVE_LEFT)
    assert sorted([(0, -1), (0, 0)]) == sorted(car.car_coordinates())


def test_2():
    board1 = Board()
    car1 = Car("a", 4, (2, 2), VERTICAL)
    car2 = Car("b", 4, (2, 3), HORIZONTAL)
    car3 = Car('c', 2, (-1, -1), HORIZONTAL)
    car4 = Car('d', 2, (-1, -1), VERTICAL)
    car5 = Car('e', 0, (0, 0), HORIZONTAL)
    # car6 = Car('f', 3, (0, 0), 3)
    car7 = Car("a", 2, (7, 0), VERTICAL)
    assert board1.add_car(car1)
    assert board1.add_car(car2)
    assert not board1.add_car(car3)
    assert not board1.add_car(car4)
    assert not board1.add_car(car5)
    # assert not board1.add_car(car6)
    assert not board1.add_car(car7)
    # print(board1)
    assert 'a' == board1.cell_content((2,2))
    assert 'b' == board1.cell_content((2,3))
    assert None is board1.cell_content((0,0))


def test_3():
    car1 = Car("Y",3,(0,3), 0)
    car2 = Car("G", 3, (3,1), 1)
    car3 = Car("R", 3,(3,0), 0)
    car4 = Car("W", 2, (2,0), 1)
    board1 = Board()
    assert board1.add_car(car1)
    assert board1.add_car(car2)
    assert board1.add_car(car3)
    assert board1.add_car(car4)
    print(board1)
    assert board1.move_car('R','d')
    assert board1.move_car('G','r')


