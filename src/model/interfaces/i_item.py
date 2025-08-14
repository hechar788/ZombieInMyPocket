from abc import ABC, abstractmethod
from ...enums_and_types.enums import ItemInfo, ItemType
from typing import List

class IItem(ABC):
    """Abstract interface defining the contract for item objects in the game."""
    
    @property
    @abstractmethod
    def name(self) -> ItemInfo:
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        pass
    
    @property
    @abstractmethod
    def type(self) -> ItemType:
        pass
    
    @property
    @abstractmethod
    def attack_bonus(self) -> int:
        pass
    
    @property
    @abstractmethod
    def heal_amount(self) -> int:
        pass
    
    @property
    @abstractmethod
    def is_single_use(self) -> bool:
        pass
    
    @abstractmethod
    def combinable_with(self) -> List[ItemInfo]:
        pass