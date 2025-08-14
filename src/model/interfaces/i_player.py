from abc import ABC, abstractmethod
from enums_and_types import Position
from .i_item import IItem


class IPlayer(ABC):
    """Abstract interface defining the contract for player objects in the game.
    """

    @abstractmethod
    def get_health(self) -> int:
        pass

    @abstractmethod
    def take_damage(self, amount: int) -> None:
        pass

    @abstractmethod
    def heal(self, amount: int) -> None:
        pass

    @abstractmethod
    def get_attack_power(self) -> int:
        pass

    @abstractmethod
    def has_totem(self) -> bool:
        pass

    @abstractmethod
    def get_position(self) -> Position:
        pass

    @abstractmethod
    def set_position(self, position: Position) -> None:
        pass

    @abstractmethod
    def use_item(self, item: IItem) -> None:
        pass

    @abstractmethod
    def get_inventory(self) -> list[IItem]:
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
