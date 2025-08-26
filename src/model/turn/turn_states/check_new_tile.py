"""Check if the given tile and exit leads to a new tile or an existing tile."""
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class CheckNewTile(State):
    def __init__(self, name = StateNames.CHECK_NEW_TILE):
        super().__init__(name)
        self.tile = None
        self.selected_door = None


    def enter(self, a_tile, selected_door):
        self.tile = a_tile
        self.selected_door = selected_door
        self.result = (a_tile, selected_door)


    def is_new_tile(self, a_tile, selected_door) -> bool:
        """Check if the tile attached to the give door on the give tile is new or not."""
        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.CAN_MOVE_TO_NEW_TILE,
            a_tile,
            selected_door)


    def handle_request(self, *args, **kwargs):
        if self.is_new_tile(self.tile, self.selected_door):
            self.trigger = Triggers.MOVE_PLAYER
        else:
            self.trigger = Triggers.DRAW_TILE
        super().handle_request()

    def exit(self):
        super().exit()