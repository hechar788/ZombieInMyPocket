#imports from external
from typing import TYPE_CHECKING, Callable, Any

#imports from components
from src.model.game_pieces import GamePieces
from src.model.player import Player
from src.view.mock_ui import UserInterface

#imports from Turn
from .turn_flow import TurnFlow #, state
from .turn_enums import Triggers, ServiceNames, StateNames
from .turn_states import *


class TurnSetUp:
    """Sets up the turn flow, states and services"""
    def __init__(self):
        self.the_turn:TurnFlow = (
            TurnFlow(self.get_services(), self.get_transitions(), self.get_turn_states()))
        self.the_turn.start() #Move the turn into the ready state

    def get_turn_flow(self):
        return self.the_turn

    @staticmethod
    def get_services() -> dict[ServiceNames, object]:
        """Get the services used by the turn"""
        the_services = {
            ServiceNames.GAME_PIECES:   GamePieces(),
            ServiceNames.PLAYER:        Player(),
            ServiceNames.UI:            UserInterface()
        }
        return the_services

    @staticmethod
    def get_transitions() -> dict[Triggers, StateNames]:
        """Get the transitions used by the turn"""
        the_transitions = {
            #Trigger,                       #Next State
            Triggers.READY:                 StateNames.READY,

            Triggers.START_TURN:            StateNames.GET_PLAYER_TILE,
            Triggers.SELECT_EXIT:           StateNames.SELECT_EXIT,

            Triggers.DRAW_TILE:             StateNames.DRAW_TILE,
            Triggers.MOVE_PLAYER:           StateNames.MOVE_PLAYER,

            Triggers.NEW_TILE_EXIT:         StateNames.PLACE_TILE,
            Triggers.PLAYER_TILE_EXIT:      StateNames.CHECK_NEW_TILE,

            Triggers.START_ENCOUNTERS:      StateNames.GET_DEV_ENCOUNTER,
            Triggers.RUN_ENCOUNTER:         StateNames.RUN_ENCOUNTER,
            Triggers.DEV_ENCOUNTER_END:     StateNames.GET_TILE_ENCOUNTER,
            Triggers.TILE_ENCOUNTER_END:    StateNames.GET_COWER_ENCOUNTER,
            Triggers.COWER_ENCOUNTER_END:   StateNames.READY,

        }
        return the_transitions

    @staticmethod
    def get_turn_states() -> dict[StateNames, Callable[[], Any]]:
        """Get the states used by the turn"""
        the_turn_states = {
            StateNames.READY:           lambda : Ready(),
            StateNames.SELECT_EXIT:     lambda : SelectExit(),
            StateNames.GET_PLAYER_TILE: lambda : GetPlayerTile(),
            StateNames.DRAW_TILE:       lambda : DrawTile(),
            StateNames.CHECK_NEW_TILE:  lambda : CheckNewTile(),
            StateNames.PLACE_TILE:      lambda : PlaceTile(),


        }
        return the_turn_states

if __name__ == '__main__':
    TurnSetUp()

