from ..state import State
from ..turn_enums import ServiceNames, ServiceMethods, Triggers, StateNames

class SelectExit(State):
    """Ask the user to select an exit from a give tile"""
    def __init__(self, name = StateNames.DRAW_TILE):
        super().__init__(name)

    def enter(self, a_tile: object):
        self.result = a_tile
        tile_exits = self.use_service(ServiceNames.GAME_PIECES, ServiceMethods.GET_TILE_DOORS, a_tile)
        self.use_service(ServiceNames.UI,
                         ServiceMethods.GET_INPUT,
                  dict['prompt':f"Pick a door to exit from {tile_exits}", 'options':tile_exits],
                         callback=self.get_request_handler())
        #return None

    def handle_request(self, selected_door):
        self.result = (self.result, selected_door)
        self.exit()

    def exit(self):
        super().exit()