"""Places a tile"""

from typing import Any
from ..state import State
from ..turn_enums import StateNames, ServiceNames, ServiceMethods, Triggers
from ....enums_and_types.enums import Rotation


class PlaceTile(State):
    def __init__(self, name: StateNames = StateNames.PLACE_TILE):
        super().__init__(name)
        self.new_tile = None
        self.new_exit = None
        self.current_tile = None
        self.current_exit = None


    def enter(self, new_tile, new_exit, current_tile, current_exit):
        self.trigger = Triggers.MOVE_PLAYER
        self.new_tile = new_tile
        self.new_exit = new_exit
        self.current_tile = current_tile
        self.current_exit = current_exit


    def place_tile(self):
        self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.PLACE_TILE,
            self.new_tile,
            self.new_exit,
            self.current_tile,
            self.current_exit
        )


    def can_place_tile(self):
        #temp
        return True #override whilst CAN_PLACE_TILE isn't working
        # return self.use_service(
        #     ServiceNames.GAME_PIECES,
        #     ServiceMethods.CAN_PLACE_TILE,
        #     self.new_tile,
        #     self.new_exit,
        #     self.current_tile,
        #     self.current_exit
        # )

    def handle_request(self, *arg, **kwarg):
        if self.can_place_tile():
            self.place_tile()
            self.result = (self.new_tile, )
            self.exit()
        else:
            raise Exception("Cannot place tile in this position")

    def get_input_options(self) -> Any:
        """Return the available rotations for placing the tile"""
        return list(Rotation)

    def get_prompt(self) -> str:
        """Return the prompt for tile placement"""
        return f"Choose rotation for placing {self.new_tile.get_name() if self.new_tile else ''}"


    def exit(self):
        super().exit()