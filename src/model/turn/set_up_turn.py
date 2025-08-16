#imports from external
from typing import TYPE_CHECKING, Callable, Any

#imports from components
from src.model.game_pieces import GamePieces
from src.model.player import Player
from src.view.mock_ui import UserInterface

#imports from Turn
from . import TurnFlow, State
from .turn_enums import Triggers, ServiceNames
from .turn_states import SelectExit, ExitRoom


class TurnSetUp:
    """Sets up the turn flow, states and services"""
    def __init__(self):
        self.the_turn:TurnFlow = (
            TurnFlow(self.get_services(), self.get_transitions()))
        self.the_turn.start() #Move the turn into the ready state

    @staticmethod
    def get_services() -> dict[ServiceNames, object]:
        """Get the services used by the turn"""
        the_services = {
            ServiceNames.GAME_PIECES: GamePieces(),
            ServiceNames.PLAYER: Player(),
            ServiceNames.UI: UserInterface()
        }
        return the_services

    @staticmethod
    def get_transitions() -> dict[Triggers, Callable[[], State]]:
        """Get the transitions used by the turn"""
        the_transitions = {
            #Trigger,                   #Next State
            Triggers.READY: lambda : SelectExit(),

        }
        return the_transitions

