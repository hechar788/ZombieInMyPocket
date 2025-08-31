import unittest
from unittest.mock import Mock, create_autospec

from src.model.turn import Turn

class TestTurn(unittest.TestCase):
    """tests for Turn"""
    def setUp(self):
        """set up a turn to test"""
        self.the_turn = Turn.create(*self.create_mock_services())

    @staticmethod
    def create_mock_services():
        """create mock services"""
        from src.model.interfaces import IPlayer, IGamePieces
        from src.view.mock_ui import UserInterface

        mock_player = create_autospec(IPlayer)
        mock_game_pieces = create_autospec(IGamePieces)
        mock_user_interface = create_autospec(UserInterface)

        return mock_game_pieces, mock_player, mock_user_interface


    def assert_pre_start(self):
        """Turn should start with no state"""
        self.assertTrue(self.the_turn.is_waiting_for_callback())
        with self.assertRaisesRegex(RuntimeError, "Cannot continue turn while waiting for input."):
            self.the_turn.continue_turn()

    def test_turn_before_start(self):
        """turn should start with no state"""
        self.assert_pre_start()

    def test_turn_after_start(self):
        """turn should be in the ready state"""
        pass



if __name__ == '__main__':
    unittest.main()
