import os

__all__ = ["TurnFlow"]

from .turn_flow import TurnFlow

if os.getenv("RUNNING_TURN_TESTS") == "1":
    #running tests for the turn packages only
    #set environment variable to "RUNNING_TURN_TESTS=1"

    from .state import State
    from .turn_enums import Triggers, StateNames, ServiceNames, ServicesMethods

    __all__ = ["State",
               "TurnFlow",
               "Triggers",
               "StateNames",
               "ServiceNames",
               "ServicesMethods",

               ]