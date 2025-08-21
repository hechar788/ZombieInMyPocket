from src.model import State
from src.model.turn import StateNames, Triggers, ServiceNames, ServiceMethods
from src.model.encounters import encounters

class GetCowerEncounter(State):
    def __init__(self, name=StateNames.GET_COWER_ENCOUNTER):
        super().__init__(name)

    def enter(self):
        self.trigger = Triggers.RUN_ENCOUNTER
        self.use_service(
            ServiceNames.UI,
            ServiceMethods.GET_INPUT,
            dict['prompt':'Would you like to cower', 'options':['yes', 'no']]
            ) #add callback

    def handle_request(self, selected_option):
        if selected_option == 'yes':
            self.result = (
                encounters.CowerEncounter,
                Triggers.COWER_ENCOUNTER_END
            )
            self.trigger = Triggers.RUN_ENCOUNTER
        else:
            self.result = None
            self.trigger = Triggers.COWER_ENCOUNTER_END

    def exit(self):
        super().exit()
