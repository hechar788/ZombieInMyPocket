from typing import List
from .i_player import IPlayer
from ..item.i_item import IItem
from ...enums_and_types.types import Position


class Player(IPlayer):
    """Concrete implementation of the IPlayer interface."""
    
    def __init__(self, initial_health: int = 100, initial_position: Position = (0, 0), base_attack_power: int = 10):
        self._health = initial_health
        self._base_attack_power = base_attack_power
        self._inventory = []
        self._position = initial_position
        self._has_totem = False
    
    @property
    def health(self) -> int:
        return self._health
    
    @property
    def attack_power(self) -> int:
        item_bonus = sum(item.attack_bonus for item in self._inventory)
        return self._base_attack_power + item_bonus
    
    @property
    def has_totem(self) -> bool:
        return self._has_totem
    
    @property
    def inventory(self) -> List[IItem]:
        return self._inventory.copy()
    
    @property
    def position(self) -> Position:
        return self._position
    
    @position.setter
    def position(self, position: Position) -> None:
        self._position = position
    
    def take_damage(self, amount: int) -> None:
        self._health = max(0, self._health - amount)
    
    def heal(self, amount: int) -> None:
        self._health += amount
    
    def use_item(self, item: IItem) -> None:
        if item in self._inventory:
            self._inventory.remove(item)
    
    def add_item_to_inventory(self, item: IItem) -> None:
        self._inventory.append(item)
    
    def remove_item_from_inventory(self, item: IItem) -> None:
        if item in self._inventory:
            self._inventory.remove(item)
    
    def combine_items_from_inventory(self) -> None:
        pass