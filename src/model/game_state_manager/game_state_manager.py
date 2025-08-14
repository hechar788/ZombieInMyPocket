from src.enums_and_types.enums import GameState


class GameStateManager:
    """ Handles game states and set up. """
    def __init__(self):
        """ Coordinates the state and the components of the game (Time, Turn, Player, and GameOver/GameStatus)"""
        self.__state = GameState.INIT
        self.health = 6 #TODO: replace with actual method/interface that get these values
        self.attack = 1  #TODO: replace with actual method/interface that get these values
        self.__room = "Foyer" #TODO: replace with actual method/interface that get these values
        self.__current_state = GameState.INIT

    def set_current_state(self, event):
        """ Event-driven command that updates game states"""
        if (event): #TODO: handle event properties and if-else to return appropriate states from enum
            # GameState.PAUSED
            return

    def stop_game(self):
        """ Handles stopping game operations. """
        pass

    def reset_game(self):
        """ Handles cleaning up game environment. """
        pass

    # def clear_tiles(self):
    #     """ Remove all tiles (indoor and outdoor tiles) during reset & start of the game """
    #     pass
    #     # self.__tile_sequence = []
    #

    # def changed_room(self, tile, x_location, y_location, rotation):
    #     """ Tile is placed on valid orientation, player enters the current room """
    #     # tile -> Tile object
    #     # x & y location -> int
    #     # rotation -> enum 0 | 90 | 180 | 360
    #     pass
    #
    # def start_game(self):
    #
    # def end_game(self):
    #
    # def reset_game(self):
    #
    # def set_game_time(self):
    #     pass
    #
    # def setup_game(self):
    #     pass
    #