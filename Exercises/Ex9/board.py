#################################################################
# FILE : board.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex9 2021
# DESCRIPTION: the class board for the game rush hour
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################


class Board:
    """
    The class Board.
    creates Board object.
    """
    BOARD_SIZE = 7

    def __init__(self):
        self.__board = [['_' for _ in range(self.BOARD_SIZE+1)] if i == 3 else
                        ['_' for _ in range(self.BOARD_SIZE)]
                        for i in range(self.BOARD_SIZE)]
        self.__cars = {}

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        result = ''
        for row in self.__board:
            for item in range(len(row)):
                result += ' ' + row[item] + ' '
            result += '\n'
        return result

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        board_cell_lst = [(row, col) for row in range(self.BOARD_SIZE) for col
                          in range(self.BOARD_SIZE)]
        board_cell_lst.append((3, 7))
        return board_cell_lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        possible_moves_lst = []
        for car_name, car in self.__cars.items():
            car_possible_moves = car.possible_moves()
            for move in car_possible_moves.keys():
                possible_cell = car.movement_requirements(move)
                if possible_cell[0] in self.cell_list() and \
                        self.cell_content(possible_cell[0]) is None:
                    desc = f'car can move in the {move} direction'
                    possible_moves_lst.append((car_name, move, desc))
        return possible_moves_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return 3, 7

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        cell_content = self.__board[coordinate[0]][coordinate[1]]
        if cell_content == '_':
            return None
        return cell_content

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # Remember to consider all the reasons adding a car can fail.
        # You may assume the car is a legal car object following the API.
        car_coordinates = car.car_coordinates()
        if not car_coordinates:
            return False
        # check if car already exists on board:
        if car.get_name() in self.__cars or car.get_name() == '_':
            return False
        # check if can place car in her coordinates:
        for coordinate in car_coordinates:
            if coordinate not in self.cell_list() or \
                    self.cell_content(coordinate) is not None:
                return False
        # adding car to dictionary of all cars in board:
        self.__cars[car.get_name()] = car
        # placing car in new coordinates:
        for coordinate in car_coordinates:
            self.__board[coordinate[0]][coordinate[1]] = car.get_name()
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        possible_moves_lst = self.possible_moves()
        for move in possible_moves_lst:
            if move[0] == name and move[1] == movekey:
                car = self.__cars[name]
                for coordinate in car.car_coordinates():
                    self.__board[coordinate[0]][coordinate[1]] = '_'
                car.move(movekey)
                for coordinate in car.car_coordinates():
                    self.__board[coordinate[0]][coordinate[1]] = name
                return True
        return False
