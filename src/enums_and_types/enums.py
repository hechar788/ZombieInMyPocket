from enum import Enum, auto
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    pass


class Rotation(Enum):
    """Rotation of a tile."""

    NONE = 0
    """No rotation."""

    CLOCKWISE = 1
    """Rotated 90 degrees clockwise."""

    UPSIDE_DOWN = 2
    """Rotated 180 degrees"""

    ANTICLOCKWISE = 3
    """Rotated 90 degrees anticlockwise."""


class Direction(Enum):
    """Direction of where doors are and where the player can move to."""

    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class ItemType(Enum):
    WEAPON = 0,
    HEALING = 1


class ItemInfo(Enum):
    SPADE = ("Spade", "A sturdy digging tool that can be used as a weapon", ItemType.WEAPON, 2, 0, False,
             cast(list['ItemInfo'], []))
    AXE = ("Axe", "A sharp wood-cutting axe effective in combat", ItemType.WEAPON, 3, 0, False,
           cast(list['ItemInfo'], []))
    BANDAGE = ("Bandage", "Basic medical supplies for treating wounds", ItemType.HEALING, 0, 3, True,
               cast(list['ItemInfo'], []))
    HEALTH_KIT = ("Health Kit", "Advanced medical kit for serious injuries", ItemType.HEALING, 0, 8, True,
                  cast(list['ItemInfo'], []))

    def __init__(self, display_name: str, description: str, item_type: ItemType,
                 attack_bonus: int, heal_amount: int, is_single_use: bool,
                 combinable_with: list['ItemInfo']):
        self.display_name = display_name
        self.description = description
        self.item_type = item_type
        self.attack_bonus = attack_bonus
        self.heal_amount = heal_amount
        self.is_single_use = is_single_use
        self.combinable_with = combinable_with

# Arsenie: State
class GameState(Enum):
    INIT = auto()       # Basic flow
    READY = auto()      # Basic flow
    RUNNING = auto()    # Basic flow
    PAUSED = auto()     # Alternate flow
    OVER = auto()       # Basic flow

# Arsenie: [Event-driven] Game setup messages, used in get-game-status and game-state-manager.
class GameSetupMessage(Enum):
    """Messages related to game initialisation."""
    GAME_START = "Welcome Player!"
    INITIALISE = "Initialising game..."
    SHUFFLING_CARDS = "Shuffling DevCard deck..."

# Arsenie: [Event-driven] List of the game states, used in get-game-status and game-state-manager.
class GameStateMessage(Enum):
    """Codes for game state messages in the game."""
    ROOM_CHANGED = "You are now in room {}"
    TIME_CHANGE= "It is now {} PM"
    HEALTH_CHANGE = "+{} Health gained"
    ATTACK_SCORE_UPDATE = "+{} Attack score gained"
    ITEM_ACQUIRED = "You acquired a new item: {}"
    ATTACK_ITEM_SELECTED = "You picked {} item as a weapon."
    ZOMBIE_DOOR_CREATED = "Zombie Door Created!"

class GameOverMessage(Enum):
    """Messages for different game-over outcomes."""
    GAME_OVER_WIN = "Congratulations! You have won!"
    GAME_OVER_LOSE_TIME = "Oh no. You ran out of time! You have been eaten by the zombies!"
    GAME_OVER_LOSE_HEALTH = "Oh no. You are exhausted! You have been eaten by the zombies!"

class GameInstruction(Enum):
    """Codes for game tips in the game."""
    STORAGE_ROOM = "You may draw another card for a chance to get an item."
    GRAVEYARD = "Resolve a new card to bury the totem.",
    EVIL_TEMPLE = "Resolve a new card to find the totem."
    PICK_ATTACK_ITEM = "Choose item"

class AlertMessage(Enum):
    """Codes for game warnings & alerts in the game."""
    TIME_WARNING = "Hurry! Your time is running out! Burry the totem!"
    LOW_HEALTH_WARNING = "Warning! Your health is running low!"

    INVALID_COWER_MOVE = "You cannot cower during a zombie door attack"
    INVALID_DOOR_EXIT_SELECTED = "You can't enter from this side. There's no door here."
    INVALID_GRASS_PATH_SELECTED = "You can't enter from this side. Hedges block your path."


class UnknownErrorMessage(Enum):
    """Codes for system errors in the game."""
    UnknownStatusError = "Unknown system error!"