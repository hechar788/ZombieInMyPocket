from src.model import State
from src.model.turn import StateNames, Triggers, ServiceNames, ServiceMethods
from src.model.encounters import encounters

class RunEncounter(State):
    def __init__(self, name: StateNames = StateNames.RUN_ENCOUNTER):
        super().__init__(name)

    def enter(self, encounter, exit_mode):
        self.trigger = type
        encounter.handle_encounter(player=ServiceNames.PLAYER)
        self.result = None

    def handle_request(self):
        super().handle_request()

    def exit(self):
        super().exit()