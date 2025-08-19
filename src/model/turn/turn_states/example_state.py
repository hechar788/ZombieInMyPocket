"""#No longer in use"""
from ..state import State
from ..turn_enums import ServiceNames, ServiceMethods, Triggers, StateNames

class ExitRoom(State):
    """a rudimentary example of a turn sate"""
    def __init__(self, name = StateNames.EXIT_ROOM):
        super().__init__(name)


    def enter(self, *args, **kwargs):
        """run when the state is entered"""
        player_position = self.use_service(ServiceNames.PLAYER, ServiceMethods.GET_POSITION)
        player_tile = self.use_service(ServiceNames.GAME_PIECES, ServiceMethods.GET_TILE, player_position)
        self.result = player_tile
        tile_exits = self.use_service(ServiceNames.GAME_PIECES, ServiceMethods.GET_TILE_EXITS, player_tile)
        self.use_service(ServiceNames.UI,
                         ServiceMethods.GET_INPUT,
                  dict['prompt':f"Pick a door to exit from {tile_exits}", 'options':tile_exits],
                         callback=self.get_request_handler())
        #return None


    def handle_request(self, selected_door):
        """resumes for where the state left off"""
        #check if new room
        if self.use_service(ServiceNames.GAME_PIECES, ServiceMethods.IS_NEW_TILE, selected_door):
            self.trigger = Triggers.NEW_TILE
        else:
            self.trigger = Triggers.OLD_TILE
        self.result = (self.result, selected_door)
        self.exit()
        #return None


    def exit(self):
        """run when the state is exited"""
        super().exit()