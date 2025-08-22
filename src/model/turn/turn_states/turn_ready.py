"""Ready to start a turn"""
from typing import TYPE_CHECKING
from ..state import State
from ..turn_enums import StateNames, Triggers

#if TYPE_CHECKING:



class Ready(State):
    """Ready to start a turn"""
    def __init__(self, name = StateNames.READY):
        super().__init__(name)

    def enter(self):
        """Ready to start a turn"""
        self.trigger = Triggers.START_TURN
        super().enter()


    def handle_request(self):
        """Wait before starting a new turn"""
        self.exit()

    def exit(self):
        super().exit()
        #Expected next state Get player tile