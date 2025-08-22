from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class MovePlayer(State):
    """Moves the player"""
    def __init__(self, name=StateNames.MOVE_PLAYER):
        super().__init__(name)


    def enter(self, a_tile):
        self.trigger = Triggers.START_ENCOUNTERS
        self.result = a_tile
        self.move_player(self.get_tile_position(a_tile))


    def get_tile_position(self, a_tile):
        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.GET_TILE_LOCATION,
            a_tile
        )


    def move_player(self, position):
        self.use_service(
            ServiceNames.PLAYER,
            ServiceMethods.MOVE_PLAYER,
            position
        )


    def handle_request(self, *arg, **kwarg):
        super().handle_request()


    def exit(self):
        self.context.state_finished(
            trigger=self.trigger,
            result=self.result,
            next_tile=self.result)
