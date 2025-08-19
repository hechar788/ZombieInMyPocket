from ..state import State
from ..turn_enums import ServiceNames, StateNames

class RunEncounter(State):
    """Runs the encounter from the previous state"""
    def __init__(self, name: StateNames = StateNames.RUN_ENCOUNTER):
        super().__init__(name)

    def enter(self, encounter, exit_mode):
        self.trigger = exit_mode
        encounter.handle_encounter(player=ServiceNames.PLAYER)
        self.result = None

    def handle_request(self):
        super().handle_request()

    def exit(self):
        super().exit()