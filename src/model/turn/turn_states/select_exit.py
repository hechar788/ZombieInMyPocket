from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods

class SelectExit(State):
    """Ask the user to select an exit from a give tile"""
    def __init__(self, name = StateNames.DRAW_TILE):
        super().__init__(name)
        self.tile_exits = []
        self.args = None


    def enter(self,
              #a_tile: object,
              #exit_mode: Triggers,
              *args) -> bool:
        a_thing = args[0]
        a_tile, exit_mode = a_thing
        self.result = a_tile
        self.trigger = exit_mode

        self.get_tile_exits(a_tile)
        self.get_user_selection()
        return True #wait for callback


    def get_tile_exits (self, a_tile):
        self.tile_exits = a_tile.get_exits()
        # self.tile_exits = self.use_service(
        #     ServiceNames.GAME_PIECES,
        #     ServiceMethods.GET_TILE_EXITS,
        #     self.result)


    def get_user_selection(self):
        self.use_service(
            ServiceNames.UI,
            ServiceMethods.GET_INPUT,
            prompt=f"Pick an exit {self.tile_exits}",
            options=self.tile_exits,
            callback=self.get_request_handler())


    def handle_request(self, selected_exit):
        if self.args:
            self.result = (self.result, selected_exit, self.args)
        else:
            self.result = (self.result, selected_exit)
        self.exit()


    def exit(self):
        super().exit()
        # Expected next state check_new_tile or place_tile