from src.enums_and_types import ItemName, ItemType
from ..interfaces import IItem
from .base_item import ConsumableItem, WeaponItem, CombinableItem, SpecialWeaponItem
from .item_config import ITEM_CONFIGS


class ItemFactory:
    @staticmethod
    def create_item(name: ItemName) -> IItem:
        if name not in ITEM_CONFIGS:
            raise ValueError(f"Unknown item: {name}")
        
        config = ITEM_CONFIGS[name]
        
        if config.item_type == ItemType.HEALING:
            return ConsumableItem(
                name=config.name,
                description=config.description,
                item_type=config.item_type,
                heal_amount=config.heal_amount,
                combinable_with=config.combinable_with
            )
        
        elif config.item_type == ItemType.WEAPON:
            if name == ItemName.CHAINSAW:
                return SpecialWeaponItem(
                    name=config.name,
                    description=config.description,
                    attack_bonus=config.attack_bonus,
                    uses=config.uses,
                    combinable_with=config.combinable_with
                )
            else:
                return WeaponItem(
                    name=config.name,
                    description=config.description,
                    attack_bonus=config.attack_bonus,
                    uses=config.uses,
                    combinable_with=config.combinable_with
                )
        
        elif config.item_type in [ItemType.COMBINE_ONLY, ItemType.ESCAPE]:
            return CombinableItem(
                name=config.name,
                description=config.description,
                item_type=config.item_type,
                combinable_with=config.combinable_with
            )
        
        else:
            raise ValueError(f"Unsupported item type: {config.item_type}")


def get_item(name: ItemName) -> IItem:
    return ItemFactory.create_item(name)

def get_all_items() -> list[IItem]:
    """Returns a list of all available items in the game."""
    return [get_item(item_name) for item_name in ItemName]
