"""Places a tile"""
from urllib.request import Request

from src.model import State
from src.model.turn import StateNames, ServiceNames, ServiceMethods, Triggers


class PlaceTile(State):
    def __init__(self, name: StateNames = StateNames.PLACE_TILE):
        super().__init__(name)


    def enter(self, new_tile, new_exit, current_tile, current_exit):
        self.trigger = Triggers.MOVE_PLAYER
        self.result = self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.PLACE_TILE,
            new_tile,
            new_exit,
            current_tile,
            current_exit
        )


    def handle_request(self, request: Request):
        super().handle_request()


    def exit(self):
        super().exit()