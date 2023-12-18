class Car:
    """
    Add class description here
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
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        self.__name = name
        self.__length = length
        self.__location = location
        # bad = need to check outside/ raise needed
        if orientation is self.HORIZONTAL or orientation is self.VERTICAL:
            self.__orientation = orientation
        else:
            raise ValueError("bad value")

    def get_o(self):
        return self.__orientation


car1 = Car('n', 4, (1,2), 3)
car1.get_o()

