import unittest
from unittest.mock import create_autospec

from src.model import TurnFlow
from src.model.turn.turn_enums import Triggers, ServiceNames, ServiceMethods
from src.model.turn.turn_states import ExitRoom


class MyTestCase(unittest.TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.callback = None

    def setUp(self):
        self.state = ExitRoom()
        self.create_mock_turn_flow()
        self.state.context = self.mock_turn_flow
        self.state.enter()


    def create_mock_turn_flow(self):
        self.mock_turn_flow = create_autospec(TurnFlow, instance=True)
        self.mock_turn_flow.state_finished.return_value = None
        self.mock_turn_flow.call_service_method.return_value = 'up'
        self.mock_turn_flow.handle_request.return_value = None

        def mock_handle_request():
            self.state.handle_request(3)

        def mock_service_side_effect(name, method, *args, **kwargs):
            if name == ServiceNames.PLAYER and method == ServiceMethods.GET_POSITION:
                return 5, 10
            elif name == ServiceNames.GAME_PIECES and method == ServiceMethods.GET_TILE_DOORS:
                return [0, 1, 3]
            elif name == ServiceNames.GAME_PIECES and method == ServiceMethods.IS_NEW_ROOM:
                return True
            elif name == ServiceNames.UI and method == ServiceMethods.GET_INPUT:
                self.callback = kwargs.get('callback')
                return None
            else:
                raise Exception(f"Unexpected call: {name}.{method}")

        self.mock_turn_flow.call_service_method.side_effect = mock_service_side_effect
        self.mock_turn_flow.handle_request = mock_handle_request




    def test_player_position_called(self):
        self.mock_turn_flow.call_service_method.assert_any_call(ServiceNames.PLAYER, ServiceMethods.GET_POSITION)

    def test_game_pieces_called(self):
        self.mock_turn_flow.call_service_method.assert_any_call(ServiceNames.GAME_PIECES, ServiceMethods.GET_TILE_DOORS, (5, 10))

    def test_state_finished_called(self):
        self.mock_turn_flow.handle_request()
        self.mock_turn_flow.state_finished.assert_called_once_with(Triggers.NEW_TILE, 3)


if __name__ == '__main__':
    unittest.main()
