from src.model.game_pieces import GamePieces
from src.model.player import Player
from src.model.turn import Turn
from src.view.mock_ui import UserInterface

class GameController:
    def __init__(self):
        self.game_running = True
        self.the_turn = None

    def set_up(self):
        # a little bit hacky way to get stuff running just for now
        the_game_pieces = GamePieces()
        the_player = Player()
        the_ui = UserInterface()

        self.the_turn = Turn.create(the_game_pieces, the_player, the_ui)



    def begin_game(self):
        print("Game has begun")

        #a little bit hacky way to get stuff running just for now
        game_running = True
        self.the_turn.start_turn()

        while game_running:
            if not self.the_turn.is_wait_for_input():
                self.the_turn.continue_turn()
            # Else wait for a callback