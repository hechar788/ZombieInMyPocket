"""internal enums for turn"""
from enum import Enum
from typing import TypedDict, Callable, Any


#States and Triggers
class Triggers(Enum):

    START_TURN = "start_turn"

    PLAYER_TILE_EXIT = "player_tile_exit"
    NEW_TILE_EXIT = "new_tile_exit"

    DRAW_TILE = "draw_tile"
    MOVE_PLAYER = "move_player"

    SELECT_EXIT = "select_exit"

    START_ENCOUNTERS = "start_encounters"
    RUN_ENCOUNTER = "run_encounter"
    DEV_ENCOUNTER_END = "dev_encounter_end"
    TILE_ENCOUNTER_END = "tile_encounter_end"
    COWER_ENCOUNTER_END = "cow_encounter_end"

    NEXT_TURN = "next_turn"
    READY = "ready"


class StateNames(Enum):
    READY = "ready"
    GET_PLAYER_TILE = "get_player_tile"
    SELECT_EXIT = "select_exit"
    CHECK_NEW_TILE = "check_new_tile"
    DRAW_TILE = "draw_tile"
    PLACE_TILE = "place_tile"
    MOVE_PLAYER = "move_player"
    GET_DEV_ENCOUNTER = "get_dev_encounter"
    GET_TILE_ENCOUNTER = "get_tile_encounter"
    GET_COWER_ENCOUNTER = "get_cower_encounter"
    RUN_ENCOUNTER = "run_encounter"
    #testing
    TEST_STATE = "test_state"

#Services
class ServiceNames(Enum):
    PLAYER = "player"
    GAME_PIECES = "gamePieces"
    UI = "ui"

#Change the name of service methods here
class ServiceMethods(Enum):
    #for player
    GET_POSITION = "get_position"
    MOVE_PLAYER = "move_player"
    # for UI
    GET_INPUT = "get_input_with_callback"
    #for GamePieces
    GET_TILE_EXITS = "get_tile_exits"
    GET_TILE = "get_tile"
    DRAW_TILE = "draw_tile"
    IS_NEW_TILE = "is_new_tile"
    PLACE_TILE = "place_tile"
    GET_TILE_LOCATION = "get_tile_location"
    DRAW_DEV_CARD = "draw_dev_card"
    GET_ENCOUNTER = "get_encounter"


class PendingTransition(TypedDict):
    """stores the state factory for a new state
    and any results from previous states to pass to it"""
    next_state: Callable[[], Any]
    previous_result: tuple[Any, ...] | None
    next_tile: Any
