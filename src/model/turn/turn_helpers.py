from abc import ABC, abstractmethod
from typing import TypedDict, Callable
from .state import State


class PendingTransition(TypedDict):
    """stores the state factory for a new state
    and any results from previous states to pass to it"""
    next_state: Callable[[], State]
    previous_result: str

class StateFactory(ABC):
    """makes a new states instant when needed"""
    pass