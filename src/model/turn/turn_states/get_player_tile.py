"""Get the players tile"""
from src.model import State
from ..turn_enums import StateNames, ServiceNames, ServiceMethods, Triggers


class GetPlayerTile(State):
    def __init__(self, name: StateNames = StateNames.GET_PLAYER_TILE):
        super().__init__(name)
        self.player_location = None

    def enter(self) -> None:
        """Get the players location and the tile at that location"""
        self.get_player_location()
        self.get_player_tile()
        self.exit()


    def get_player_location(self) -> None:
        """Gets the players location"""
        self.player_location = self.use_service(
            ServiceNames.PLAYER,
            ServiceMethods.GET_POSITION)


    def get_player_tile(self):
        """Gets the players tile"""
        self.trigger = Triggers.SELECT_EXIT
        self.result = self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.GET_TILE,
            self.player_location)


    def handle_request(self, *args, **kwargs):
        """This state doesn't take requests"""
        super().handle_request()


    def exit(self) -> None:
        a_tile = self.result
        self.result = (a_tile, Triggers.PLAYER_TILE_EXIT)
        self.context.state_finished(
            trigger=self.trigger,
            result=self.result,
            next_tile=a_tile)
        #Expected next state select_exit