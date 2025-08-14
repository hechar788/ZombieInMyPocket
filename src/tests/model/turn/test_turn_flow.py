import unittest
from unittest.mock import Mock, create_autospec

#testing...
from src.model.turn import TurnFlow, State

create_autospec(State, instance=True)

class MyTestCase(unittest.TestCase):
    def setUp(self):
        the_services = self.create_mock_services()
        the_transitions = self.create_mock_transitions()
        self.turn_flow = TurnFlow(the_services, the_transitions)

    def create_mock_services(self):
        #mock UI
        mock_ui = Mock()
        mock_ui.get_input.return_value = 'Option1'

        #mock game
        fake_tile = Mock()
        fake_rotation = 0

        self.mock_game_pieces = Mock()
        self.mock_game_pieces.get_tile.return_value = [fake_tile, fake_rotation]

        return {"ui":mock_ui, "game_pieces":self.mock_game_pieces}

    def create_mock_state(self, name="mock_state", result=None, trigger=None):
        # Create a mock that follows the State interface
        mock_state = create_autospec(State, instance=True)

        # Set attributes that would normally be initialized
        mock_state.name = name
        mock_state.result = result
        mock_state.trigger = trigger
        mock_state.context = Mock(spec=TurnFlow)  # mock context

        # Mock the abstract methods
        mock_state.enter.return_value = None
        mock_state.handle_request.return_value = None
        mock_state.exit.return_value = None

        def handle_enter_side_effect(*args, **kwargs):
            """mimics the state using a service"""
            mock_state.context.call_service_method('game_pieces', 'get_tile')

        def handle_request_side_effect(*args, **kwargs):
            """this mimics the real state being called then finishing"""
            mock_state.context.state_finished(mock_state.trigger, mock_state.result)

        mock_state.handle_request.side_effect = handle_request_side_effect
        mock_state.enter.side_effect = handle_enter_side_effect

        return mock_state

    def create_mock_transitions(self):
        mock_exit_room = self.create_mock_state("exit_room", "door_1", "choose_door")
        mock_draw_tile = self.create_mock_state("draw_tile", "fake_tile", "choose_door")
        mock_choose_door = self.create_mock_state("move_player", "door_chosen", "draw_tile")

        mock_transitions = {
            "exit_room": Mock(return_value=mock_exit_room),
            "draw_tile": Mock(return_value=mock_draw_tile),
            "choose_door": Mock(return_value=mock_choose_door),
        }
        return mock_transitions

    def create_ready_state(self):
        return self.create_mock_state(name="ready", result=None, trigger="exit_room")

    def test_starting_state_bad_day(self):
        with self.assertRaises(Exception):
            self.turn_flow.start()
        self.assertEqual(self.turn_flow.current_state, None)

    def test_starting_happy_day(self):
        self.turn_flow.register_transition("ready", Mock(return_value=self.create_ready_state()))
        self.assertEqual(self.turn_flow.start(), True)
        self.assertEqual(self.turn_flow.current_state.name, "ready")

    def test_calling_states(self):
        self.turn_flow.register_transition("ready", Mock(return_value=self.create_ready_state()))
        self.turn_flow.start()
        self.assertEqual(self.turn_flow.current_state.name, "ready")
        self.turn_flow.handle_request()
        self.assertEqual(self.turn_flow.current_state.name, "exit_room")
        self.mock_game_pieces.get_tile.assert_called()



if __name__ == '__main__':
    unittest.main()
