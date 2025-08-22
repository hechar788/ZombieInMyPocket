import os

#from .turn_flow import TurnFlow
from .set_up_turn import TurnSetUp

__all__ = [
    #"TurnFlow",
    "TurnSetUp"
]

if os.getenv("RUNNING_TURN_TESTS") == "1":
    #running tests for the turn packages only
    #set environment variable to "RUNNING_TURN_TESTS=1"

    from .state import State
    from .turn_enums import Triggers, StateNames, ServiceNames, ServiceMethods

    __all__ = ["State",
               #"TurnFlow",
               #"TurnSetUp"
               "Triggers",
               "StateNames",
               "ServiceNames",
               "ServiceMethods",

               ]