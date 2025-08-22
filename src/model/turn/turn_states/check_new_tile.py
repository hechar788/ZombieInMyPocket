"""Check if the given tile and exit leads to a new tile or an existing tile."""
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class CheckNewTile(State):
    def __init__(self, name = StateNames.CHECK_NEW_TILE):
        super().__init__(name)


    def enter(self, a_tile, selected_door):
        self.result = (a_tile, selected_door)
        if self.is_new_tile(a_tile, selected_door):
            self.trigger = Triggers.DRAW_TILE
        else:
            self.trigger = Triggers.MOVE_PLAYER
        self.exit()


    def is_new_tile(self, a_tile, selected_door) -> bool:
        """Check if the tile attached to the give door on the give tile is new or not."""
        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.IS_NEW_TILE,
            a_tile,
            selected_door)

    def handle_request(self, *args, **kwargs):
        super().handle_request()

    def exit(self):
        super().exit()