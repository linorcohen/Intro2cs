#################################################################
# FILE : car.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex9 2021
# DESCRIPTION: the class car for the game rush hour
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################


class Car:
    """
    The Car class.
    creates Car object.
    """
    HORIZONTAL = 1
    VERTICAL = 0
    MOVE_UP = "u"
    MOVE_DOWN = "d"
    MOVE_LEFT = "l"
    MOVE_RIGHT = "r"

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col)
        location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        if self.__orientation == self.HORIZONTAL:
            return [(self.__location[0], self.__location[1] + i) for i in
                    range(self.__length)]
        if self.__orientation == self.VERTICAL:
            return [(self.__location[0] + i, self.__location[1]) for i in
                    range(self.__length)]
        return []

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        if self.__orientation == self.HORIZONTAL:
            return {self.MOVE_LEFT: 'cause the car to move to the left',
                    self.MOVE_RIGHT: 'cause the car to move to the right'}
        if self.__orientation == self.VERTICAL:
            return {self.MOVE_UP: 'cause the car to move to up',
                    self.MOVE_DOWN: 'cause the car to move to down'}
        return {}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for
        this move to be legal.
        """
        current_locations = self.car_coordinates()
        if not current_locations:  # in case the car has no coordinates
            return []

        if self.__orientation == self.VERTICAL:
            if movekey == self.MOVE_DOWN:
                return [(current_locations[-1][0] + 1, current_locations[-1][1])]
            if movekey == self.MOVE_UP:
                return [(current_locations[0][0] - 1, current_locations[-1][1])]

        if self.__orientation == self.HORIZONTAL:
            if movekey == self.MOVE_RIGHT:
                return [(current_locations[-1][0], current_locations[-1][1] + 1)]
            if movekey == self.MOVE_LEFT:
                return [(current_locations[0][0], current_locations[0][1] - 1)]
        return []

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if self.__orientation == self.HORIZONTAL:
            if movekey is self.MOVE_LEFT:
                self.__location = self.movement_requirements(self.MOVE_LEFT)[0]
                return True
            if movekey is self.MOVE_RIGHT:
                self.__location = self.__location[0], self.__location[1] + 1
                return True
        if self.__orientation == self.VERTICAL:
            if movekey is self.MOVE_UP:
                self.__location = self.movement_requirements(self.MOVE_UP)[0]
                return True
            if movekey is self.MOVE_DOWN:
                self.__location = self.__location[0] + 1, self.__location[1]
                return True
        return False

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
