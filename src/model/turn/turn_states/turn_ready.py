"""Ready to start a turn"""
from src.model import State
from src.model.turn import StateNames, Triggers


class Ready(State):
    """Ready to start a turn"""
    def __init__(self, name = StateNames.READY):
        super().__init__(name)

    def enter(self):
        """Ready to start a turn"""
        self.trigger = Triggers.START_TURN

    def handle_request(self):
        """Wait before starting a new turn"""
        self.exit()

    def exit(self):
        super().exit()
        #Expected next state Get player tile