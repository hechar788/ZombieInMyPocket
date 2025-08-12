import typing

class TurnFlow(object):
    """Tracks the state of a turn"""
    def __init__(self, initial_state):
        self.current_state = initial_state

    def change_state(self, next_state):
        self.current_state = next_state

    def request(self, *data):
        self.current_state.handle_request(data)