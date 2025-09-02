# Arsenie: [1] Component for User Story 12 - Game set-up start thing
# Used by game_session_manager

from abc import ABC, abstractmethod
from ..event import Event
from src.enums_and_types import GameOverReason


class IGameOver(ABC):

    @property
    @abstractmethod
    def game_over_event(self) -> Event[GameOverReason]:
        pass

    @game_over_event.setter
    @abstractmethod
    def game_over_event(self, value: Event[GameOverReason]) -> None:
        pass

    @abstractmethod
    def health_is_zero(self) -> None:
        pass

    @abstractmethod
    def time_is_up(self) -> None:
        pass

    @abstractmethod
    def totem_is_buried(self) -> None:
        pass
