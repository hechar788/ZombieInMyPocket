from abc import ABC, abstractmethod
from typing import Optional

from ...enums_and_types.enums import GameStateMessage, GameInstruction, AlertMessage, UnknownErrorMessage, GameState, \
    GameOverMessage


class IGameStatus(ABC):
    """ Handles game status messages."""

    @property
    @abstractmethod
    def check_game_state(self) -> GameState:
        pass

    @property
    @abstractmethod
    # TODO: Change condition type to enum of game over conditions
    def handle_game_over(self) -> Optional[GameOverMessage]:
        """ Game over event-driven that calls appropriate game over message and options, based on GameOverMessage enum"""
        pass

    @abstractmethod
    def get_state_message(self) -> Optional[GameStateMessage]:
        """Returns a state update message (e.g., room changed, health update)."""
        pass

    @abstractmethod
    def handle_help_key(self) -> Optional[GameInstruction]:
        """ Toggles show/hide instruction when H key is pressed, based on GameInstruction enum"""
        pass

    @property
    @abstractmethod
    def handle_game_warning_event(self) -> Optional[AlertMessage]:
        """ Handles event-driven alerts (e.g. almost time, low health, invalid moves) and informs users based on AlertMessage enum"""
        pass
