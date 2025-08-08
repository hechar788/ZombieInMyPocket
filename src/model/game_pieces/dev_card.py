from abc import ABC, abstractmethod
from model.item.item import Item
from model.encounter.encounter import Encounter

class DevCard(ABC):

    @abstractmethod
    def get_item(self) -> Item:
        pass

    @abstractmethod
    def get_encounter(self, time: int) -> Encounter:
        pass
