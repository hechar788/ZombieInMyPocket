from typing import Any
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class MovePlayer(State):
    """Moves the player
    expected previous state:
         check_new_tile
         place_tile
    """
    def __init__(self, name=StateNames.MOVE_PLAYER):
        super().__init__(name)
        #self.the_tile = None
        #self.selected_exit = None


    def enter(
            self,
            a_tile,
            #selected_exit
    ):
        self.trigger = Triggers.START_ENCOUNTERS
        self.result = a_tile
        #self.the_tile = a_tile
        #self.selected_exit = selected_exit



    def get_tile_position(self, a_tile):
        #return 1, 0
        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.GET_TILE_POSITION,
            a_tile
        )
        #error with get_tile_position


    def move_player(self, position):
        self.use_service(
            ServiceNames.PLAYER,
            ServiceMethods.SET_POSITION,
            position
        )


    def handle_request(self, *arg, **kwarg):
        self.move_player(self.get_tile_position(self.result))
        self.exit()

    def get_input_options(self) -> Any:
        """No input options needed for moving player"""
        return []

    def get_prompt(self) -> str:
        """No prompt needed for moving player"""
        return "Moving player..."


    def exit(self):
        self.context.state_finished(
            trigger=self.trigger,
            result=None,
            next_tile=self.result)
        self.context = None
