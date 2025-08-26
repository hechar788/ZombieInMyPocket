from typing import Any
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods

class SelectExit(State):
    """Ask the user to select an exit from a give tile"""
    def __init__(self, name = StateNames.SELECT_EXIT):
        super().__init__(name)
        self.tile_exits = []
        self.args = None


    def enter(self,
              a_tile: Any,
              exit_mode: Triggers,
              *arg
              ):
        self.result = a_tile
        #to do refactor to make the exit mode trigger set in handle_request based on args
        self.trigger = exit_mode
        print(exit_mode)
        self.args = arg or None
        self.needs_input = True

        self.get_tile_exits(a_tile)
        self.get_user_selection(a_tile.get_name())


    def get_tile_exits (self, a_tile):
        self.tile_exits = a_tile.get_exits()
        # self.tile_exits = self.use_service(
        #     ServiceNames.GAME_PIECES,
        #     ServiceMethods.GET_TILE_EXITS,
        #     self.result)


    def get_user_selection(self, tile_name):
        self.use_service(
            ServiceNames.UI,
            ServiceMethods.GET_INPUT,
            prompt = f"Pick an exit on the {tile_name} tile",
            options = self.tile_exits,
            callback = self.get_request_handler())


    def handle_request(self, selected_exit):
        if self.args:
            current_tile, current_exit = self.args[0]
            #print(current_tile, current_exit)
            self.result = (self.result, selected_exit, current_tile, current_exit)
        else:
            self.result = (self.result, selected_exit)
        self.exit()


    def exit(self):
        super().exit()
        # Expected next state check_new_tile or place_tile