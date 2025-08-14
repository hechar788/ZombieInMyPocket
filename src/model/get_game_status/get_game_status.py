from ..interfaces.i_get_game_status import IGameStatus
from ...enums_and_types.enums import GameStateMessage, GameInstruction, AlertMessage, UnknownErrorMessage

class GameStatus(IGameStatus):
    def __init__(self) -> None:
        # self._is_game_over: bool = False
        self._game_over_message: str | None = None
        self._system_message: str | None = None

    # @property
    # def is_game_over(self) -> bool:
    #     return self._is_game_over


    @property
    def handle_game_over(self) -> str | None:
        return self._game_over_message

    @property
    def system_message(self) -> str | None:
        return self._system_message

    #TODO: Change condition type to enum of game over conditions
    def trigger_game_over(self, condition: str) -> None:
        # self._is_game_over = True
        self._game_over_message = condition

    def reset(self) -> None:
        """Resets for new game."""
        # self._is_game_over = False
        self._game_over_message = None
        self._system_message = None

    def post_message(self, code: GameStateMessage, *args) -> None:
        # TODO: Add validation here for if args are missing but required
        pass
        # message_template = self._MESSAGE_MAP.get(code, "Unknown system event.")
        # self._system_message = message_template.format(*args) # Error Possible Here