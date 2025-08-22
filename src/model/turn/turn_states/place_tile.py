"""Places a tile"""

from ..state import State
from ..turn_enums import StateNames, ServiceNames, ServiceMethods, Triggers


class PlaceTile(State):
    def __init__(self, name: StateNames = StateNames.PLACE_TILE):
        super().__init__(name)


    def enter(self, new_tile, new_exit, current_tile, current_exit):
        self.trigger = Triggers.MOVE_PLAYER
        self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.PLACE_TILE,
            new_tile,
            new_exit,
            current_tile,
            current_exit
        )
        self.result = new_tile


    def handle_request(self, *arg, **kwarg):
        super().handle_request()


    def exit(self):
        super().exit()