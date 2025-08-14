from ..interfaces.i_game_status import IGameStatus
from ...enums_and_types.enums import MessageCode, GameOverConditions

class GameStatus(IGameStatus):

    _MESSAGE_MAP = {
        MessageCode.WELCOME: "Welcome",
        MessageCode.ROOM_CHANGED: "Current Room {}",
        MessageCode.HEALTH_GAINED: "+{} Health gained",
        MessageCode.ENTERED_GRAVEYARD: "Resolve a new card to bury the totem.",
        MessageCode.ENTERED_EVIL_TEMPLE: "Resolve a new card to find the totem.",
        MessageCode.STORAGE_ROOM_PROMPT: "You may draw another card for a chance to get an item.",
        MessageCode.LOW_HEALTH_WARNING: "Low Health!",
        MessageCode.TIME_WARNING: "Time running low!",
        MessageCode.ITEM_ACQUIRED: "New item: {}",
        MessageCode.ZOMBIE_DOOR_CREATED: "A zombie door has been created on the {} wall",
        MessageCode.INVALID_COWER_MOVE: "You cannot cower during a zombie door attack"
    }

    def __init__(self) -> None:
        self._is_game_over: bool = False
        self._game_over_condition: str | None = None
        self._system_message: str | None = None

    @property
    def is_game_over(self) -> bool:
        return self._is_game_over

    @property
    def game_over_condition(self) -> GameOverConditions | None:
        return self._game_over_condition

    @property
    def system_message(self) -> str | None:
        return self._system_message

    def trigger_game_over(self, condition: GameOverConditions) -> None:
        self._is_game_over = True
        self._game_over_condition = condition

    def reset(self) -> None:
        """Resets for new game."""
        self._is_game_over = False
        self._game_over_condition = None
        self._system_message = None

    def post_message(self, code: MessageCode, *args) -> None:
        #TODO: Add validation here for if args are missing but required
        message_template = self._MESSAGE_MAP.get(code, "Unknown system event.")
        self._system_message = message_template.format(*args) # Error Possible Here