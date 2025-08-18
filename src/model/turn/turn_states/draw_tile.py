from ..state import State
from ..turn_enums import ServiceNames, ServiceMethods, Triggers, StateNames

from src.enums_and_types.types import Position

class DrawTile(State):
    """gets a tile, if with position returns the tile at that position,
     if no position draws a new tile indoors or outdoors"""
    def __init__(self, name = StateNames.DRAW_TILE):
        super().__init__(name)

    def enter(self, *args):
        self.args = args
        self.result = self.use_service(
            # check indoor/outdoor in service
            ServiceNames.GAME_PIECES,
            ServiceMethods.DRAW_TILE,
        )

    def handle_request(self, the_tile):
        super().handle_request()

    def exit(self):
        self.result = (self.result, Triggers.NEW_TILE_EXIT, self.args)
        super().exit()

