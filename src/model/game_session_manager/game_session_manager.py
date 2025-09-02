from src.enums_and_types.enums import GameState


class GameStateManager:
    """ Handles game states and set up. """
    def __init__(self):
        """ Coordinates the state and the components of the game (Time, Turn, Player, and GameOver/GameStatus)"""
        # self.__state = GameState.INIT
        # self.health = 6 #TODO: replace with actual method/interface that get these values
        # self.attack = 1  #TODO: replace with actual method/interface that get these values
        # self.__room = "Foyer" #TODO: replace with actual method/interface that get these values
        # self.__current_state = GameState.INIT

    # def set_current_state(self, event):
    #     """ Event-driven command that updates game states"""
    #     if (event): #TODO: handle event properties and if-else to return appropriate states from enum
    #         # GameState.PAUSED
    #         return ""
    #     else:
    #         return ""

    def setup_game(self):
        """"""
        # set_current_state
        # set_game_time
        pass

    def start_game(self):
        """"""
        pass

    def end_game(self):
        """ Handles stopping game operations. """
        pass

    def reset_game(self):
        """ Handles cleaning up game environment. """
        # clear_tiles

    def save_game(self):
        """ Save game progress """
        pass

    def load_game(self):
        """ Restore saved game progress """
        pass