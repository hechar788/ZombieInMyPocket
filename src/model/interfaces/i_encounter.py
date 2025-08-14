from abc import ABC, abstractmethod

class IEncounter(ABC):
    """Abstract Class for building other Encounter Classes"""
    @abstractmethod
    def set_values(self, value):
        ...

    @abstractmethod
    def handle_encounter(self, player):
        ...

    def handle_status_message(self, message):
        ...
