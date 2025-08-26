from ..state import State
from ..turn_enums import StateNames, ServiceNames

class RunEncounter(State):
    """Runs the encounter from the previous state"""
    def __init__(self, name: StateNames = StateNames.RUN_ENCOUNTER):
        super().__init__(name)
        self.encounter = None

    def enter(self, encounter, exit_mode):
        self.trigger = exit_mode
        self.encounter = encounter


    def handle_request(self):
        self.encounter.handle_encounter(
            self.context.get_service(ServiceNames.PLAYER)
        )
        self.result = None
        super().handle_request()

    def exit(self):
        super().exit()