from enum import Enum


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


class GameOverCondition(Enum):
    WIN_BURY_TOTEM = auto()                 #Win: Player managed to bury the zombie totem before midnight
    LOSE_COMBAT_DEATH = auto()              #Lose: Player loses its last health during COMBAT
    LOSE_RUN_AWAY_DEATH = auto()            #Lose: Player loses its last health after RUNNING AWAY
    LOSE_TIME_RAN_OUT_NO_TOTEM = auto()     #Lose: Player DOES NOT have the totem, but ran out of time before being able to bury the zombie totem
    LOSE_TIME_RAN_OUT_WITH_TOTEM = auto()   #Lose: Player DOES have the totem, but ran out of time before being able to bury the zombie totem