#################################################################
# FILE : game.py
# WRITER : Linor Cohen , linorcohen , 318861226
# EXERCISE : intro2cse ex9 2021
# DESCRIPTION: the class game for the game rush hour
# STUDENTS I DISCUSSED THE EXERCISE WITH: NONE
# WEB PAGES I USED: NONE
# NOTES: NONE
#################################################################
import sys
from board import Board
from car import Car
import helper


class Game:
    """
    The class Game.
    this class operates the game rush hour.
    """
    POSSIBLE_CAR_NAMES = {'Y', 'B', 'O', 'G', 'W', 'R'}
    POSSIBLE_MOVES = {'u', 'd', 'l', 'r'}
    MIN_LENGTH = 2
    MAX_LENGTH = 4
    HORIZONTAL = 1
    VERTICAL = 0

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(str(self.__board))
        while not self.__check_if_won():
            user_input = input('Please enter your input (Car,Move):')
            if user_input == '!':
                break
            if not self.__check_input_valid(user_input):
                print('Input is invalid')
                continue
            input_name, input_move = user_input.split(',')
            if not self.__board.move_car(input_name, input_move):
                print(f"can't move car {input_name} in {input_move} direction")
                continue
            print(str(self.__board))

    def __check_input_valid(self, user_input):
        """
        This function checks the input of the user if legal to use.
        :param user_input: string of the input
        :return: True if input legal, else False.
        """
        if len(user_input.split(',')) != 2:
            return False
        input_name, input_move = user_input.split(',')
        if input_name not in self.POSSIBLE_CAR_NAMES:
            return False
        if input_move not in self.POSSIBLE_MOVES:
            return False
        return True

    def __check_if_won(self):
        """
        This function checks if the player won the game by placing a car in
        the target location of the board.
        :return: True, if target_location has a car, else False.
        """
        if self.__board.cell_content(
                self.__board.target_location()) is not None:
            print('*** YOU WIN ***')
            return True
        return False


if __name__ == "__main__":
    board_game = Board()
    json_dict = helper.load_json(sys.argv[1])
    for car_name, car_values in json_dict.items():
        # check if valid to add car to board:
        if Game.MIN_LENGTH <= car_values[0] <= Game.MAX_LENGTH and \
                (car_values[2] is Game.HORIZONTAL or
                 car_values[2] is Game.VERTICAL) and \
                car_name in Game.POSSIBLE_CAR_NAMES:
            # add car to board:
            car = Car(car_name, car_values[0], car_values[1], car_values[2])
            board_game.add_car(car)

    game = Game(board_game)
    game.play()
