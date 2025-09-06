import unittest
from unittest.mock import create_autospec

from src.model.turn import *
from src.model.game_pieces import *
from src.model.player import Player
from src.model.game_time.game_time import GameTime
from src.view.mock_ui import UserInterface

class TestTurn(unittest.TestCase):
    """tests for Turn (context and states"""
    def setUp(self):
        """set up a turn to test"""
        self.user_interface = create_autospec(UserInterface)
        self.player = Player()
        self.game_pieces = GamePieces()
        self.game_time = GameTime()
        self.the_turn = Turn.create(
            self.game_pieces,
            self.player,
            self.user_interface,
            self.game_time
        )


    def assert_pre_start(self):
        """Turn should start with no state"""
        self.assertTrue(self.the_turn.is_waiting_for_callback())
        with self.assertRaisesRegex(RuntimeError, "Cannot continue turn while waiting for input."):
            self.the_turn.continue_turn()


    def test_turn_before_start(self):
        """turn should start with no state"""
        self.assert_pre_start()


    def test_turn_start(self):
        """
        given:  the turn is ready to start
        when:   the game_manger starts the turn
        Then:   the turn should be in the ready state
        """
        self.the_turn.start_turn()
        self.assertEqual(self.the_turn._flow._current_state.name.value, 'ready')
        self.assertFalse(self.the_turn.is_waiting_for_callback())


    def test_continue_turn(self):
        """turn should move to the ready state then the get player tile state"""
        self.the_turn.start_turn()
        self.the_turn.continue_turn()
        self.assertEqual(self.the_turn._flow._current_state.name.value, 'get_player_tile')


    def test_turn_after_stop(self):
        """turn should move to pre_start with no state"""
        self.the_turn.start_turn()
        self.the_turn.continue_turn()
        self.the_turn.continue_turn()
        self.the_turn.end_turn()
        self.assert_pre_start()


    def jump_to_dev_encounter(self):
        """advance the turn 10 steps"""
        from src.model.turn.turn_enums import Triggers
        self.the_turn.start_turn()

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
        self.jump_to_dev_encounter()
        self.assertEqual('get_dev_encounter', self.the_turn._flow._current_state.name.value)
        self.the_turn.continue_turn()
        self.assertEqual('run_encounter', self.the_turn._flow._current_state.name.value)


if __name__ == '__main__':
    unittest.main()
