import unittest
from unittest.mock import create_autospec

from src.model.turn.turn_enums import ServiceNames, Triggers
from src.model.game_pieces import *
from src.model.game_time.game_time import GameTime
from src.model.turn import *
from src.view.mock_ui import UserInterface
from src.model.interfaces import IPlayer


class TestTurnAdvancement(unittest.TestCase):
    """tests for Turn (context and states"""
    def setUp(self):
        """set up a turn to test"""
        self.user_interface = create_autospec(UserInterface)
        self.player = create_autospec(IPlayer)
        self.game_pieces = GamePieces()
        self.game_time = GameTime()
        self.the_turn = Turn.create(
            self.game_pieces,
            self.player,
            self.user_interface,
            self.game_time
        )

    def jump_to_dev_encounter(self):
        """advance the turn 10 steps"""
        self.the_turn._flow.state_finished(
            trigger = Triggers.START_ENCOUNTERS,
            result = None
        )
        self.the_turn._flow._change_state()


    def test_turn_advancement(self):
        """
        Given:  the game is running
        When:   a Dev card is dawn
        Then:   time must update according to the rule of Time Passes
        """
        self.the_turn.start_turn()
        time_before = self.game_time.get_current_time()

        self.jump_to_dev_encounter()
        self.assertEqual('get_dev_encounter', self.the_turn._flow._current_state.name.value)

        self.the_turn.continue_turn()

        self.assertEqual('run_encounter', self.the_turn._flow._current_state.name.value)
        self.assertEqual(time_before, self.game_time.get_current_time())

        i  = 0
        while i < 9:
            #run out the dev cards
            self.jump_to_dev_encounter()
            self.the_turn.continue_turn()
            i += 1
        self.assertNotEqual(time_before, self.game_time.get_current_time())

if __name__ == '__main__':
    unittest.main()
