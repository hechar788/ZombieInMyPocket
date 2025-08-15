from typing import Callable, Optional
from threading import Timer
from .turn_enums import ServiceNames, ServiceMethods, Triggers, StateNames

from src.enums_and_types.types import Position
from ..interfaces import IGamePieces




class ServiceGateway:
    """The gateway between game and components turn needs to call
    """
    #Real Services
    class GamePieces:
        """the gateway for game pieces"""
        def __init__(self, game_pieces: IGamePieces):
            self.implementation = game_pieces

        def get_tile(
                self,
                position: Position,
                callback: Optional[Callable[[any], None]] = None
        ) -> Optional[any]:

            service_method = lambda: self.implementation.get_tile(position)

            if callback is not None:
                # Call asynchronously with callback
                ServiceGateway.use_callback(service_method, callback)
                output = None
            else:
                # Call synchronously and return result
                output = service_method

            return output

    #Mocks
    @staticmethod
    def use_callback(self, service_method: Callable[[], any], callback: Callable[[any], None]) -> None:
        """adds a callback to a given service method"""
        def delated_call():
            result = service_method()
            callback(result)
        Timer(1, delated_call).start()

