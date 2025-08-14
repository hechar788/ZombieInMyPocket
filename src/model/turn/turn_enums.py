"""internal enums for turn"""
import enum
from enum import Enum

class Triggers(Enum):
    READY = "ready"
    MOVE_PLAYER = "move_player"
    NEW_TILE = 'new_room'
    OLD_TILE = 'old_room'
    CHOOSE_DOOR = "choose_door"
    DRAW_TILE = "draw_tile"
    EXIT_ROOM = "exit_room"


class StateNames(Enum):
    READY = "ready"
    EXIT_ROOM = "exit_room"
    DRAW_TILE = "draw_tile"
    MOVE_PLAYER = "move_player"
    #testing
    TEST_STATE = "test_state"


class ServiceNames(Enum):
    PLAYER = "player"
    GAME_PIECES = "gamePieces"
    UI = "ui"

class ServicesMethods(Enum):
    GET_POSITION = "get_position"
    GET_TILE_DOORS = "get_tile_doors"
    GET_INPUT = "get_input"
    IS_NEW_ROOM = "is_new_room"


