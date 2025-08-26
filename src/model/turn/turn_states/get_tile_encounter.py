from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class GetTileEncounter(State):
    def __init__(self, name=StateNames.GET_TILE_ENCOUNTER):
        super().__init__(name)

    def enter(self):
        self.trigger = Triggers.RUN_ENCOUNTER


    def get_tile_encounter(self, tile):
        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.GET_ENCOUNTER,
            tile = tile
        )

    def handle_request(self, *arg, **kwarg):
        self.result = (
            self.get_tile_encounter(self.context.active_tile),
            Triggers.TILE_ENCOUNTER_END
        )
        super().handle_request()

    def exit(self):
        super().exit()