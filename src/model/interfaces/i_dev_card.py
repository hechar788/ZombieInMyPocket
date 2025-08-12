from abc import ABC, abstractmethod
from .i_encounter import IEncounter
from .i_item import IItem


class IDevCard(ABC):

    @abstractmethod
    def get_item(self) -> IItem:
        pass

    @abstractmethod
    def get_encounter(self, time: int) -> IEncounter:
        pass
