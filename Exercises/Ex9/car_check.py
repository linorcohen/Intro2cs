from car import *


def check_car_move():
    car = Car("test", 2, (1,4), VERTICAL)
    coords0 = car.car_coordinates()
    print('0-', coords0)
    assert car.move(MOVE_UP)
    coords1 = car.car_coordinates()
    print('1-', coords1)

    print([(row-1, col) for row, col in sorted(coords0)])
    print(sorted(coords1))
    assert [(row-1, col) for row, col in sorted(coords0)] == sorted(coords1)
    assert car.move(MOVE_DOWN)
    coords2 = car.car_coordinates()
    assert coords2 == coords0


def check_cat_cor():
    car = Car("test", 4, (2,2), VERTICAL)
    car2 = Car("test", 4, (2,2), HORIZONTAL)
    assert sorted([
        (2,2), (3,2), (4,2), (5,2)
    ]) == sorted(car.car_coordinates())
    assert sorted([
        (2,2), (2,3), (2,4), (2,5)
    ]) == sorted(car2.car_coordinates())

def check_move_req():
    car = Car("oki", 2, (2,4), HORIZONTAL)
    print(car.movement_requirements(MOVE_RIGHT))
    assert sorted([(2,6)]) == sorted(car.movement_requirements(MOVE_RIGHT))
    print(car.movement_requirements(MOVE_LEFT))
    assert sorted([(2,3)]) == sorted(car.movement_requirements(MOVE_LEFT))

    car = Car("oki", 2, (2,4), VERTICAL)
    assert sorted([(1,4)]) == sorted(car.movement_requirements(MOVE_UP))
    assert sorted([(4,4)]) == sorted(car.movement_requirements(MOVE_DOWN))


if __name__ == '__main__':
    # x = [(0, 0), (0, 1), (0, 2)]
    # y = [(3, 0), (2, 0)]
    # location = (0,0)
    # length = 3
    # lst1 = [(location[0], location[1] + i) for i in range(length)]
    # location = (1,1)
    # length = 2
    # lst2 = [(location[0], location[1] + i) for i in range(length)]
    # location = (1,1)
    # length = 2
    # lst3 = [(location[0]+ i, location[1] ) for i in range(length)]
    # print(lst3)
    # check_car_move()
    # check_cat_cor()
    check_move_req()