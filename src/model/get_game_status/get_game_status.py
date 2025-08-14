from abc import ABC
from typing import Optional

from ..interfaces.i_get_game_status import IGameStatus
from ..interfaces.i_time import ITime
from ...enums_and_types.enums import GameStateMessage, GameInstruction, AlertMessage, UnknownErrorMessage, GameState, \
    GameOverMessage


class GameStatus(IGameStatus, ABC):
    def __init__(self, current_time: ITime) -> None:
        self._game_over_message = None
        self.current_time = current_time
        self._state = GameState.INIT
        self._low_health = False

    # @property
    # def check_game_state(self) -> GameState:
    #     """"""
    #     return self._state

    @property
    def handle_game_over(self) -> Optional[GameOverMessage]:
        """ Retrieves message code for the end game details, based on GameOverMessage enum"""
        return self._game_over_message

    @property
    def get_state_message(self) -> Optional[GameStateMessage]:
        """Retrieves message code that constantly updates based on the players choices (i.e. room change, item selection/acquired, heal, and attack score gains  """
        pass

    @property
    def handle_help_key(self) -> Optional[GameInstruction]:
        """ Retrieves message code that corresponds to the current room and game state when H key is pressed"""
        pass

    @property
    def handle_game_warning_event(self) -> Optional[AlertMessage]:
        """ Retrieves message code when triggered by game time warnings"""
        pass
