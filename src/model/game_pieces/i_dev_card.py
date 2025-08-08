from abc import ABC, abstractmethod
from model.item.i_item import IItem
from model.encounter.i_encounter import IEncounter

class IDevCard(ABC):

    @abstractmethod
    def get_item(self) -> IItem:
        pass

    @abstractmethod
    def get_encounter(self, time: int) -> IEncounter:
        pass
