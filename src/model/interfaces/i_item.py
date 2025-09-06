from abc import ABC, abstractmethod
from src.enums_and_types import *


class IItem(ABC):
    """Abstract interface defining the contract for item objects in the game.
    """

    @property
    @abstractmethod
    def name(self) -> ItemName:
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

    # @property
    # @abstractmethod
    # def is_single_use(self) -> bool:
    #     pass

    # Changed is_single_use to uses_remaning because the chainsaw
    # has multiple uses
    @property
    @abstractmethod
    def uses_remaining(self) -> int:
        """Number of uses remaining."""
        pass

    @property
    @abstractmethod
    def combinable_with(self) -> list[ItemName]:
        pass

    @abstractmethod
    def use(self) -> bool:
        """This method is just for decrementing the uses remaning
        if the item has limited used.

        Return True if the item has depleated all it's uses
        """
        pass
