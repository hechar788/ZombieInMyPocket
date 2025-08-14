from state import State
from typing import Callable

class TurnFlow:
    """
    Tracks the state of a turn,
    the context of the state machine, in the State Design Pattern
    """
    def __init__(self,
                 the_services: dict[
                    str,
                    object
                 ] | None = None,
                 the_transitions: dict[
                    tuple[str, str],
                    Callable[[], State]
                 ] | None = None) -> None:
        self.current_state = None
        self.next_state = None
        #map: (name, component)
        self.service: dict[str, object] = the_services if the_services is not None else {}
        #map: (event_name, result: str, state_factory(None) -> State
        self.transition: dict[
            tuple[str, str],
            Callable[[], State]
        ] = the_transitions if the_transitions is not None else {}

    def set_next_state(self, next_state: State) -> None:
        """sets the next state"""
        self.next_state = next_state

    def set_state(self, state_factory: Callable[[], State]) -> None:
        """sets the current state of the turn"""
        self.current_state = state_factory() #Make a new state object each time
        self.current_state.context = self
        self.current_state.enter()

    def change_state(self) -> None:
        """changes the current state of the turn to self.next_state"""
        if self.next_state is not None and self.current_state is not None:

            self.current_state = None
            self.set_state(self.next_state)

    def state_finished(self, result) -> None:
        """called when the state is finished"""
        self.next_state = self.transition[(self.current_state.name, result)]
        return None #The state that called state_finished mast end(return) immediately

    def handle_request(self, *args, **kwargs) -> None:
        """handles incoming requests"""
        self.current_state.handle_request(*args, **kwargs)
        self.change_state()
        return None #Returns to caller

    def register_transition(self,
           event_name: str,
           result: str,
           sate_factory: Callable[[], State]) -> None:
        """Register a transition, takes some event, some condition (fuc), and a state_factory (fun)"""
        self.transition[(event_name, result)] = sate_factory


    # def emit_state_transition_event(self, name: str, data: dict) -> None:
    #     """Called by a state to trigger a possible transition"""
    #     for (event_name, condition), state_factory in self.transition.items():
    #         if name == event_name and condition(data):
    #             self.set_state(state_factory)
    #             break

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
