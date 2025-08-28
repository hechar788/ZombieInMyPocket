from ..model.turn import TurnSetUp
from ..model.game_status.game_status import GameStatus
from ..model.turn.turn_enums import ServiceNames
from ..enums_and_types.enums import MessageCode
from ..enums_and_types.game_over_reason import GameOverReason
from ..view.interfaces.i_ui import IUI
import time

class GameController:
    def __init__(self, ui: IUI):
        self.game_status = GameStatus()
        self.ui = ui
        self.the_set_up = TurnSetUp()
        self.the_turn = self.the_set_up.get_turn_flow()

    def begin_game(self):
        self.game_status.post_message(MessageCode.WELCOME)
        self.run_game()

    def run_game(self):
        while not self.game_status.is_game_over:
            self._process_and_display_messages()
            self._update_full_state()

            if self.the_turn.is_wait_for_input():
                self._handle_input()
            else:
                 self._process_turn()
                 time.sleep(0.5) 


    def _handle_input(self):
        """Handle user input for the current turn state"""

        current_state = self.the_turn.current_state
        if current_state is None:
            return

        # Get the current state's input requirements
        options = current_state.get_input_options()
        prompt = current_state.get_prompt()
        
        # Get input from UI
        user_input = self.ui.get_input(prompt, options)
        
        # Process the input in the current state
        self.the_turn.handle_input(user_input)

    def _process_turn(self):
        """Process the current turn state when no input is needed"""
        self.the_turn.process()


    def _process_and_display_messages(self):
        """Helper to get messages from GameStatus and display them."""
        messages = self.game_status.get_messages()
        if messages:
            for msg in messages:
                self.ui.display_message(msg)
            self.game_status.clear_messages()

    def _update_full_state(self):
        """Update the game display with current state"""
        player = self.the_turn.service[ServiceNames.PLAYER]
        self.ui.display_game_state(
            player_health=player.get_health(),
            player_attack=player.get_attack_power(),
            current_time="9:00 PM",  # TODO: Implement game time
            items=[item.name for item in player.get_inventory()]
        )