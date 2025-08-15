from ..state import State
from ..turn_enums import ServiceNames, ServiceMethods, Triggers, StateNames

from src.enums_and_types.types import Position

class GetTile(State):
    """gets a tile, if with position returns the tile at that position,
     if no position draws a new tile indoors or outdoors"""
    def __init__(self, name = StateNames.DRAW_TILE):
        super().__init__(name)

    def enter(self, a_position:Position|None = None ):
        if a_position is not None:
            #Get the tile at the position
            self.use_service(
                ServiceNames.GAME_PIECES,
                ServiceMethods.GET_TILE,
                a_position,
                self.get_request_handler()
            )
        else:
            #draw a new tile
            self.use_service(
                # check indoor/outdoor in service
                ServiceNames.GAME_PIECES,
                ServiceMethods.DRAW_TILE,
                self.get_request_handler()
            )

    def handle_request(self, the_tile):
        self.result = the_tile

    def exit(self):
        super().exit()

