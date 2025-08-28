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


    def get_tile_exits (self, a_tile):
        self.tile_exits = a_tile.get_exits()
        # self.tile_exits = self.use_service(
        #     ServiceNames.GAME_PIECES,
        #     ServiceMethods.GET_TILE_EXITS,
        #     self.result)


    


    def handle_request(self, selected_exit):
        if self.args:
            current_tile, current_exit = self.args[0]
            self.result = (self.result, selected_exit, current_tile, current_exit)
        else:
            self.result = (self.result, selected_exit)
        self.exit()

    def get_input_options(self) -> Any:
        """Return the available exits for the current tile"""
        return self.tile_exits

    def get_prompt(self) -> str:
        """Return the prompt for exit selection"""
        return f"Pick an exit on the {self.result.get_name() if self.result else ''} tile"

    def exit(self):
        super().exit()
        # Expected next state check_new_tile or place_tile