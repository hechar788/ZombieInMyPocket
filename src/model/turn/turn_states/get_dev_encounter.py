"""Draw a dev card then get the encounter from it based on time"""
from ..state import State
from ..turn_enums import StateNames, Triggers, ServiceNames, ServiceMethods


class GetDevEncounter(State):
    def __init__(self, name=StateNames.GET_DEV_ENCOUNTER):
        super().__init__(name)
    
    def enter(self):
        self.trigger = Triggers.RUN_ENCOUNTER


    def handle_request(self):
        the_dev_card = self._get_dev_card()
        self.result = (
            self._get_dev_encounter(the_dev_card),
            Triggers.DEV_ENCOUNTER_END
        )
        super().handle_request()


    def exit(self):
        super().exit()

    def _is_dev_cards_remaining(self) -> bool:
        """returns true if there are dev cards remaining to pull"""
        is_dev_cards_remaining = True
        if self.use_service(
                ServiceNames.GAME_PIECES,
                ServiceMethods.DEV_CARDS_REMAINING
        ) <= 0:
            is_dev_cards_remaining = False
        return is_dev_cards_remaining


    def _increase_time(self):
        """Increase time"""
        self.use_service(ServiceNames.GAME_TIME, ServiceMethods.INCREASE_TIME)


    def _shuffle_cards(self):
        """Shuffle the dev cards"""
        #suffle not implemented in game pieces (or anywhere)
        self.use_service(ServiceNames.GAME_PIECES, ServiceMethods.SHUFFLE_DEV_CARDS)

    
    def _get_dev_card(self):
        """Draws a dev card if any remaining"""
        if not self._is_dev_cards_remaining():
            #no cards remaining increase time and shuffle cards
            self._increase_time()
            self._shuffle_cards()

        return self.use_service(
            ServiceNames.GAME_PIECES,
            ServiceMethods.DRAW_DEV_CARD
        )


    def _get_dev_encounter(self, the_dev_card):
        the_time = self.use_service(
            ServiceNames.GAME_TIME,
            ServiceMethods.GET_CURRENT_TIME
        )
        return the_dev_card.get_encounter(9) #todo use game time

    