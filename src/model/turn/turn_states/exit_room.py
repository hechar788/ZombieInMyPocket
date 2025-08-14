from ..state import State

class ExitRoom(State):
    """a rudimentary example of a turn sate"""
    def __init__(self, name):
        super().__init__(name)
        self.result = None
        self.trigger = None


    def enter(self, *args, **kwargs):
        """run when the state is entered"""
        player_position = self.call('player', 'get_position')
        tile_exits = self.call('gamePieces', 'get_tile_doors', player_position)
        self.call("ui", "get_input", dict['prompt':f"Pick a door to exit from {tile_exits}", 'options':tile_exits])
        return None


    def handle_request(self, selected_door):
        """resumes for where the state left off"""
        #check if new room
        if self.call('gamePieces', 'is_new_room', selected_door):
            self.trigger = 'new_room'
        else:
            self.trigger = 'old_room'
        self.result = selected_door
        self.exit()
        return None


    def exit(self):
        """run when the state is exited"""
        super().exit()