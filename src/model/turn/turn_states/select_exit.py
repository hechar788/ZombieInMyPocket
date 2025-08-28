from typing import Any
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods
from src.enums_and_types import Direction # New import

class SelectExit(State):
    """Ask the user to select an exit from a give tile"""
    def __init__(self, name = StateNames.SELECT_EXIT):
        super().__init__(name)
        self.tile = None 
        self.other_tile = None 
        self.other_exit = None 


    def enter(self,
              the_tile: Any, 
              exit_mode: Triggers,
              other_tile: Any = None, 
              other_exit: Any = None 
              ):
        self.tile = the_tile 
        self.trigger = exit_mode
        self.other_tile = other_tile 
        self.other_exit = other_exit 
        self.needs_input = True


    def get_tile_exits (self): 
        return self.tile.get_exits()


    def handle_request(self, selected_exit):
        selected_exit = Direction(int(selected_exit)) 

        if self.trigger == Triggers.NEW_TILE_EXIT:
            self.result = (
                self.tile,
                selected_exit,
                self.other_tile,
                self.other_exit
            )
        else:
            self.result = (
                self.tile,
                selected_exit
            )
        self.exit()

    def get_input_options(self) -> Any:
        """Return the available exits for the current tile"""
        return self.get_tile_exits() # Use the new get_tile_exits

    def get_prompt(self) -> str:
        """Return the prompt for exit selection"""
        return f"Pick an exit on the {self.tile.get_name() if self.tile else ''} tile" # Use self.tile

    def exit(self):
        super().exit()