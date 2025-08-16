from typing import Callable, Optional, Any
from abc import ABC, abstractmethod

from src.enums_and_types.types import Position

from .turn_enums import ServiceNames, ServiceMethods, Triggers, StateNames
from .turn_helpers import AsyncServiceRunner

from ..interfaces import IGamePieces

class AService(ABC):
    def __init__(self, service_name: ServiceNames, the_service: object):
        self.service_name = service_name
        self.service = the_service
#
#     def service_method(self, method_name: str) -> Callable:
#         return getattr(self.service, method_name)

class ServiceGateway:
    """The gateway between game and components turn needs to call
    """
    #Runner
    def __init__(self):
        self.services = []

    def get_services(self) -> dict[ServiceNames, object]:
        the_services = {}
        for service in self.services:
            the_services[service.name] = service
        return the_services


    @staticmethod
    def run_service(
            service_method: Callable[[], Any],
            callback: Optional[Callable[[Any], None]] = None
    ) -> Optional[Any]:
        """runs a service Synchronously or asynchronously with a callback"""
        if callback is not None:
            # Call asynchronously with callback
            AsyncServiceRunner.use_callback(service_method, callback)
            output = None
        else:
            # Call synchronously and return result
            output = service_method()

        return output
