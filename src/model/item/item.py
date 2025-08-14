# from model.interfaces.i_item import IItem
# from enums_and_types.enums import ItemInfo, ItemType


# class Item(IItem):
#     def __init__(self, item_info: ItemInfo):
#         self._item_info = item_info

#     @property
#     def name(self) -> ItemInfo:
#         return self._item_info

#     @property
#     def description(self) -> str:
#         return self._item_info.description

#     @property
#     def type(self) -> ItemType:
#         return self._item_info.item_type

#     @property
#     def attack_bonus(self) -> int:
#         return self._item_info.attack_bonus

#     @property
#     def heal_amount(self) -> int:
#         return self._item_info.heal_amount

#     @property
#     def is_single_use(self) -> bool:
#         return self._item_info.is_single_use

#     def combinable_with(self) -> list[ItemInfo]:
#         return self._item_info.combinable_with

from enums_and_types import ItemName, ItemType
from ..interfaces import IItem
from .oil import Oil
from .combine_to_kill import CombineToKill
from .weapon import Weapon
from .can_of_soda import CanOfSoda
from .chainsaw import Chainsaw


class Item(IItem):
    def __init__(self, name: ItemName,
                 description: str,
                 type: ItemType,
                 attack_bonus: int = 0,
                 heal_amount: int = 0) -> None:
        self.__name = name
        self.__description = description
        self.__type = type
        self.__attack_bonus = attack_bonus
        self.__heal_amount = heal_amount

    @property
    def name(self) -> ItemName:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def type(self) -> ItemType:
        return self.__type

    @property
    def attack_bonus(self) -> int:
        return self.__attack_bonus

    @property
    def heal_amount(self) -> int:
        return self.__heal_amount

    @property
    def combinable_with(self) -> list[ItemName]:
        return []


GASOLINE_DESCRIPTION = ("Combine with Candle to kill all zombies without "
                        "taking damage. Combine with Chainsaw to give "
                        "two more chainsaw uses. One time use.")
BOARD_WITH_NAILS_DESCRIPTION = "Add 1 to Attack score."
GRISLY_FEMUR_DESCRIPTION = "Add 1 to Attack score."
GOLF_CLUB_DESCRIPTION = "Add 1 to Attack score."
CANDLE_DESCRIPTION = ("Combine with Oil or Gasoline to kill all zombies "
                      "on one tile without taking damage.")
MACHETE_DESCRIPTION = "Add 2 to Attack score."
GASOLINE_CHAINSAW_USES = 2


def get_item(name: ItemName) -> IItem:
    match name:
        case ItemName.OIL:
            return Oil()
        case ItemName.GASOLINE:
            return CombineToKill(
                ItemName.GASOLINE,
                GASOLINE_DESCRIPTION,
                [ItemName.CANDLE]
            )
        case ItemName.BOARD_WITH_NAILS:
            return Weapon(
                ItemName.BOARD_WITH_NAILS,
                BOARD_WITH_NAILS_DESCRIPTION,
                1
            )
        case ItemName.CAN_OF_SODA:
            return CanOfSoda()
        case ItemName.GRISLY_FEMUR:
            return Weapon(
                ItemName.GRISLY_FEMUR,
                GRISLY_FEMUR_DESCRIPTION,
                1
            )
        case ItemName.GOLF_CLUB:
            return Weapon(
                ItemName.GOLF_CLUB,
                GOLF_CLUB_DESCRIPTION,
                1
            )
        case ItemName.CANDLE:
            return CombineToKill(
                ItemName.CANDLE,
                CANDLE_DESCRIPTION,
                [ItemName.OIL, ItemName.GASOLINE]
            )
        case ItemName.CHAINSAW:
            return Chainsaw()
        case ItemName.MACHETE:
            return Weapon(
                ItemName.MACHETE,
                MACHETE_DESCRIPTION,
                2
            )


def combine_items(a: IItem, b: IItem) -> bool:
    """Combine two items. Returns True if all zombies should be killed.

    Items that have 0 uses_remaining need to be discarded after this.
    """

    assert a.name in b.combinable_with
    assert b.name in a.combinable_with

    # Combining candle with either Oil or Gasoline.
    if (a.name == ItemName.CANDLE and b.name == ItemName.GASOLINE) \
            or (a.name == ItemName.GASOLINE and b.name == ItemName.CANDLE) \
            or (a.name == ItemName.CANDLE and b.name == ItemName.OIL) \
            or (a.name == ItemName.OIL and b.name == ItemName.CANDLE):
        a.use()
        b.use()
        return True

    # Combining Chainsaw with Gasoline
    if a.name == ItemName.CHAINSAW and b.name == ItemName.GASOLINE \
            or (a.name == ItemName.GASOLINE and b.name == ItemName.CHAINSAW):
        if isinstance(a, Chainsaw):
            a.add_uses(GASOLINE_CHAINSAW_USES)
            b.use()
        elif isinstance(b, Chainsaw):
            b.add_uses(GASOLINE_CHAINSAW_USES)
            a.use()
    return False
