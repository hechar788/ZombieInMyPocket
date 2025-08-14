from state import State
from typing import Callable
from turn_helpers import PendingTransition

class TurnFlow:
    """
    Tracks the state of a turn,
    the context of the state machine, in the State Design Pattern
    """
    def __init__(self,
                 the_services: dict[
                    str, object
                 ] | None = None,
                 the_transitions: dict[
                    tuple[str],
                    Callable[[], State]
                 ] | None = None) -> None:

        self.pending_transition: PendingTransition | None = None
        self.current_state = None

        #map: (name, component)
        self.service: dict[str, object] = the_services if the_services is not None else {}

        # Map of transitions: trigger -> state factory (callable that returns a State)
        self.transitions: dict[str, Callable[[], State]] = the_transitions if the_transitions is not None else {}

        # Note: if multiple states can finish with the same trigger but transition to different next states,
        # you could refactor the dict key to include the current state's name along with the trigger.
        # But consider changing one of the trigger first


    def set_state(self, state_factory: Callable[[], State], *args, **kwargs) -> None:
        """sets the current state of the turn"""
        self.current_state = state_factory() #Make a new state object each time
        self.current_state.context = self
        self.current_state.enter(*args, **kwargs)
        return None #Passback


    def change_state(self) -> None:
        """changes the current state of the turn if there is a pending transition"""
        if self.pending_transition is not None and self.current_state is not None:
            self.current_state = None
            self.set_state(self.pending_transition["next_state"], self.pending_transition["previous_result"])
            self.pending_transition = None
        return None #Passback


    def get_state_factory(self, trigger) -> Callable[[], State] | None:
        """returns the factory for a state with a given trigger,
        or None if there is no trigger:state pair"""
        return self.transitions.get(trigger, None)


    def state_finished(self, trigger, result) -> None:
        """called when the state is finished"""
        next_transition = self.get_state_factory(trigger)
        if next_transition is None:
            raise Exception(f"No such transition: {next_transition}")
        self.pending_transition: PendingTransition = {
            "next_state": next_transition,
            "previous_result": result
        }
        return None #The state that called state_finished mast end(return) quickly


    def handle_request(self, *args, **kwargs) -> None:
        """handles incoming requests"""
        self.current_state.handle_request(*args, **kwargs)
        self.change_state()
        return None #Returns to caller


    def register_transition(self,
           trigger: str,
           sate_factory: Callable[[], State]) -> None:
        """Register a transition, takes some trigger, and a state_factory"""
        self.transitions[trigger] = sate_factory


    # services (could be moved to a new class)
    def register_service(self, name: str, interface: object) -> None:
        """registers a new interface
        E.G. register_interface('combat', combat_interface)
        """
        self.service[name] = interface

    def unregister_service(self, name: str) -> object:
        """unregisters a service, returns the service"""
        return self.service.pop(name)

    def get_service(self, name: str) -> object | None:
        """returns the interface registered for the given name
        returns none if the interface is not registered"""
        return self.service.get(name, None)

    def call_service_method(self, name: str, method: str, *args, **kwargs) -> object:
        """calls a method on the given service"""
        service = self.get_service(name)
        if service is None:
            raise Exception(f"No such service: {name}")
        try:
            method = getattr(service, method)
        except AttributeError:
            raise Exception(f"No such method: {method}")
        else:
            return method(*args, **kwargs)
