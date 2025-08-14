from model.interfaces.i_item import IItem
from enums_and_types.enums import ItemInfo, ItemType


class Item(IItem):
    def __init__(self, item_info: ItemInfo):
        self._item_info = item_info

    @property
    def name(self) -> ItemInfo:
        return self._item_info

    @property
    def description(self) -> str:
        return self._item_info.description

    @property
    def type(self) -> ItemType:
        return self._item_info.item_type

    @property
    def attack_bonus(self) -> int:
        return self._item_info.attack_bonus

    @property
    def heal_amount(self) -> int:
        return self._item_info.heal_amount

    @property
    def is_single_use(self) -> bool:
        return self._item_info.is_single_use

    def combinable_with(self) -> list[ItemInfo]:
        return self._item_info.combinable_with
