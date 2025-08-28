"""Controls the flow of the turn by changing state"""
from typing import Callable, Any, TYPE_CHECKING

from .turn_enums import Triggers, ServiceNames, ServiceMethods, StateNames, PendingTransition

if TYPE_CHECKING:
    from .state import State


class TurnFlow:
    """
    Tracks the state of a turn,
    the context of the state machine, in the State Design Pattern
    """
    def __init__(self,
                 the_services: dict[
                    ServiceNames, object
                 ] | None = None,
                 the_states: dict[
                     StateNames,
                     Callable[[], Any]
                 ] | None = None,
                 the_transitions: dict[
                    Triggers,
                    StateNames
                 ] | None = None) -> None:


        #map: (name ServiceNames, component)
        self.service: dict[ServiceNames, object] = the_services if the_services is not None else {}

        # Map of transitions: trigger -> state factory (callable that returns a State)
        self.transitions: dict[Triggers, StateNames] = the_transitions if the_transitions is not None else {}
        # Note: if multiple states can finish with the same trigger but transition to different next states,
        # you could refactor the dict key to include the current state's name along with the trigger.
        # But consider changing one of the trigger instead
        self.states: dict[StateNames, Callable[[], State]] = the_states if the_states is not None else {}

        self.pending_transition: PendingTransition | None = None

        self.current_state: State | None = None
        # hold the active tile to make it easier to get the tile encounter
        self.active_tile: Any | None = None

        #todo update states and context to use transition and maybe active tile
        #self.transition_type = None
        #instead of having DEV_ENCOUNTER_END, ROOM_ENCOUNTER_END, etc
        #the context would use the transition_type to determine the next state


    def start(self) -> None:
        start_state = self.get_state_factory(Triggers.READY)
        if start_state is None:
            raise Exception(f"No start_state: use {Triggers.READY} trigger")
        self.current_state = self.setup_new_state(start_state)


    def end(self) -> None:
        """Resets the state to its initial state"""
        self.pending_transition = None
        self.current_state = None
        self.active_tile = None


    def setup_new_state(
            self,
            state_factory: Callable[[], Any],
            next_tile: Any | None = None,
            previous_result: tuple[Any, ...] | None = None
    ) -> Any:
        """sets the current state of the turn"""
        new_state = state_factory() #Make a new state object each time
        new_state.context = self
        print(f"the next state is {new_state.name}\n the previous result is {previous_result}")
        if next_tile is not None:
            self.active_tile = next_tile
        if previous_result is not None:
            new_state.enter(*previous_result)
        else:
            new_state.enter()

        return new_state
        #return None #Passback


    def change_state(self) -> None:
        """changes the current state of the turn if there is a pending transition"""
        if self.pending_transition is not None and self.current_state is not None:
            self.current_state = None
            new_state = self.setup_new_state(
                self.pending_transition["next_state"],
                self.pending_transition["next_tile"],
                self.pending_transition["previous_result"]
            )
            self.pending_transition = None
            self.current_state = new_state
        #return None #Passback


    def get_state_factory(self, trigger: Triggers) -> Callable[[], Any] | None:
        """returns the factory for a state given trigger,
        or None if there is no trigger:state pair"""
        a_state_name = self.transitions.get(trigger)
        return self.states.get(a_state_name, None)
        #return self.transitions.get(trigger, None)


    def state_finished(
            self,
            trigger: Triggers,
            result: tuple[Any, ...] | None,
            next_tile: Any | None = None
    ) -> None:
        """called when the state is finished"""
        next_transition = self.get_state_factory(trigger)
        if next_transition is None:
            raise Exception(f"No such transition: {trigger}, exiting {self.current_state.name}")
        self.pending_transition: PendingTransition = {
            "next_state": next_transition,
            "previous_result": result,
            "next_tile": next_tile
        }
        #return None
        #The state that called state_finished mast end(return) quickly
        #state returns to handle request, handle request changes the state
        #then returns to where it was called


    def is_wait_for_input(self) -> bool:
        """returns True if the state is waiting for input"""
        output = True #Stops calls to handle request when no state is active
        if self.current_state is not None:
            output = self.current_state.needs_input
        return output


    def handle_request(self, *args, **kwargs) -> None:
        """handles incoming requests"""
        if self.current_state is None:
            raise Exception(f"No current state")

        self.current_state.handle_request(*args, **kwargs)
        self.change_state()


    def get_service(self, name: ServiceNames) -> object | None:
        """returns the interface registered for the given name
        returns none if the interface is not registered"""
        return self.service.get(name, None)


    def call_service_method(self, name: ServiceNames, method: ServiceMethods, *args, **kwargs) -> object:
        """calls a method on the given service"""
        service = self.get_service(name)
        if service is None:
            raise Exception(f"No such service: {name}")
        try:
            method = getattr(service, method.value)
        except AttributeError:
            raise Exception(f"No such method: {service}.{method}")
        else:
            return method(*args, **kwargs)

    #could add register_state, register_transition, register_service and
    #unregister_state etc. if the need to change any dynamically comes up