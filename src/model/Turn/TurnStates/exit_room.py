from ..state import State
from ..interfaces.i_player import IPlayer
from enums_and_types.types import Position

class Exit_Room(State):
    """a rudimentary example of a turn sate"""

    def enter(self):
        """run when the state is entered"""
        self.tile = IGamePieces.get_tile(IPlayer.position());
        # get player input (How?)
        ui.get_input(f"Pick a door to exit from {self.tile.get_exits()}") #place holder
        # return

    def handle_request(self, selected_door):
        """resumes for where the state left off"""
        #check if new room
        if IGamePieces.is_new_room(): #Place holder check
            self.exit('New room')
        else:
            self.exit('Revisit_Room')
        #return

    def exit(self, next_state):
        """run when the state is exited"""
        TurnFlow.set_state(next_state)
        pass