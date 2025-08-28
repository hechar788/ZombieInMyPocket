from typing import Optional
from src.enums_and_types import ItemName, ItemType
from ..interfaces import IItem


class BaseItem(IItem):
    def __init__(self, name: ItemName, description: str, item_type: ItemType,
                 attack_bonus: int = 0, heal_amount: int = 0, 
                 uses: int = 1, combinable_with: Optional[list[ItemName]] = None) -> None:
        self._name = name
        self._description = description
        self._type = item_type
        self._attack_bonus = attack_bonus
        self._heal_amount = heal_amount
        self._max_uses = uses
        self._uses_remaining = uses
        self._combinable_with = combinable_with or []

    @property
    def name(self) -> ItemName:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def type(self) -> ItemType:
        return self._type

    @property
    def attack_bonus(self) -> int:
        return self._attack_bonus

    @property
    def heal_amount(self) -> int:
        return self._heal_amount

    @property
    def uses_remaining(self) -> int:
        return self._uses_remaining

    @property
    def combinable_with(self) -> list[ItemName]:
        return self._combinable_with.copy()

    def use(self) -> bool:
        if self._uses_remaining <= 0:
            return True
        
        self._uses_remaining -= 1
        return self._uses_remaining <= 0


class ConsumableItem(BaseItem):
    def __init__(self, name: ItemName, description: str, item_type: ItemType,
                 heal_amount: int = 0, combinable_with: Optional[list[ItemName]] = None) -> None:
        super().__init__(name, description, item_type, 
                        heal_amount=heal_amount, uses=1, 
                        combinable_with=combinable_with)


class WeaponItem(BaseItem):
    def __init__(self, name: ItemName, description: str, attack_bonus: int,
                 uses: int = 99, combinable_with: Optional[list[ItemName]] = None) -> None:
        super().__init__(name, description, ItemType.WEAPON, 
                        attack_bonus=attack_bonus, uses=uses,
                        combinable_with=combinable_with)


class CombinableItem(BaseItem):
    def __init__(self, name: ItemName, description: str, item_type: ItemType,
                 combinable_with: list[ItemName]) -> None:
        super().__init__(name, description, item_type, uses=1,
                        combinable_with=combinable_with)


class SpecialWeaponItem(WeaponItem):
    def add_uses(self, amount: int) -> None:
        self._uses_remaining += amount