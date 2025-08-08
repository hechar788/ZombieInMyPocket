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

