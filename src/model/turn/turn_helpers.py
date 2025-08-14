from abc import ABC, abstractmethod
from typing import TypedDict, Callable
from typing import TYPE_CHECKING

from .state import State
from .turn_enums import Triggers, StateNames

class PendingTransition(TypedDict):
    """stores the state factory for a new state
    and any results from previous states to pass to it"""
    next_state: Callable[[], State]
    previous_result: Triggers

class StateFactory(ABC):
    """makes a new states instant when needed"""
    pass