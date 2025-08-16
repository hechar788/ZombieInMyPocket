from abc import ABC, abstractmethod
from typing import TypedDict, Callable, Any
from threading import Timer

from .state import State
from .turn_enums import Triggers, StateNames
from .turn_states import SelectExit, ExitRoom


class AsyncServiceRunner:
    """Mock implementation of AsyncServiceRunner to replicate simple callback behavior"""
    @staticmethod
    def use_callback(service_method: Callable[[], Any], callback: Callable[[Any], None]) -> None:
        """adds a callback to a given service method"""
        def delay_call():
            result = service_method()
            callback(result)
        Timer(1, delay_call).start()

class PendingTransition(TypedDict):
    """stores the state factory for a new state
    and any results from previous states to pass to it"""
    next_state: Callable[[], State]
    previous_result: Triggers