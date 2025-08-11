from abc import ABC, abstractmethod
from typing import List
from ...enums_and_types.types import Position
from .i_item import IItem


class IPlayer(ABC):
    """Abstract interface defining the contract for player objects in the game."""
    
    @property
    @abstractmethod
    def health(self) -> int:
        pass
    
    @property
    @abstractmethod
    def attack_power(self) -> int:
        pass

    @property
    @abstractmethod
    def has_totem(self) -> bool:
        pass

    @property
    @abstractmethod
    def inventory(self) -> List[IItem]:
        pass
    
    @property
    @abstractmethod
    def position(self) -> Position:
        pass
    
    @position.setter
    @abstractmethod
    def position(self, position: Position) -> None:
        pass

    
    @abstractmethod
    def take_damage(self, amount: int) -> None:
        pass
    
    @abstractmethod
    def heal(self, amount: int) -> None:
        pass

    @abstractmethod
    def use_item(self, item: IItem) -> None:
        pass
    
    @abstractmethod
    def add_item_to_inventory(self, item: IItem) -> None:
        pass
    
    @abstractmethod
    def remove_item_from_inventory(self, item: IItem) -> None:
        pass
    
    @abstractmethod
    def combine_items_from_inventory(self) -> None:
        pass