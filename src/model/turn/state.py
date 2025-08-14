from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    #only imported for type checking
    from .turn_flow import TurnFlow

class State(ABC):
    """The parent state class"""
    @abstractmethod
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.result: str | None = None
        self.trigger: str | None = None
        self.context: TurnFlow | None = None #none should be assigned before exiting to help with clean up

    def call(self, service: str, method: str, *args, **kwargs):
        return self.context.call_service_method(service, method, *args, **kwargs)

    @abstractmethod
    def enter(self, *args, **kwargs):
        """run when the state is entered"""
        pass

    @abstractmethod
    def handle_request(self, *args, **kwargs):
        """handles incoming requests in a way that is unique to this state"""
        pass

    @abstractmethod
    def exit(self):
        """run when the state is exited"""
        self.context.state_finished(self.trigger, self.result)
        self.context = None #set none to help with clean up
        return None #return quickly to give control back to context

