from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from .turn_enums import Triggers, ServiceNames, ServicesMethods, StateNames

if TYPE_CHECKING:
    #only imported for type checking
    from .turn_flow import TurnFlow

class State(ABC):
    """The parent state class"""
    @abstractmethod
    def __init__(self, name: StateNames) -> None:
        self.name: StateNames = name
        self.result: str | None = None
        self.trigger: Triggers | None = None
        self.context: TurnFlow | None = None #none should be assigned before exiting to help with clean up

    def use_service(self, service: ServiceNames, method: ServicesMethods, *args, **kwargs):
        return self.context.call_service_method(service, method, *args, **kwargs)

    def get_request_handler(self):
        return self.context.handle_request

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

