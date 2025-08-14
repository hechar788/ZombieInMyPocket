from abc import ABC, abstractmethod
from ...enums_and_types.enums import MessageCode


class IGameStatus(ABC):
    """
    An interface to handle game state changes and construct status messages.
    """

    @property
    @abstractmethod
    def is_game_over(self) -> bool:
        pass

    @property
    @abstractmethod
    # TODO: Change condition type to enum of game over conditions
    def game_over_condition(self) -> str | None:
        pass

    @property
    @abstractmethod
    def system_message(self) -> str | None:
        pass

    @abstractmethod
    def post_message(self, code: MessageCode, *args) -> None:
        pass

    @abstractmethod
    def trigger_game_over(self, condition: str) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass