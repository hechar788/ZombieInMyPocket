from abc import ABC, abstractmethod
from dataclasses import dataclass
from src.enums_and_types import ItemName
from ..interfaces import IItem
from .base_item import SpecialWeaponItem
from .item_config import GASOLINE_CHAINSAW_USES


@dataclass
class CombinationResult:
    kills_all_zombies: bool = False
    items_consumed: list[IItem] = None
    
    def __post_init__(self):
        if self.items_consumed is None:
            self.items_consumed = []


class CombinationRule(ABC):
    @abstractmethod
    def can_combine(self, item_a: IItem, item_b: IItem) -> bool:
        pass
    
    @abstractmethod
    def combine(self, item_a: IItem, item_b: IItem) -> CombinationResult:
        pass


class CandleWithFlammableRule(CombinationRule):
    def can_combine(self, item_a: IItem, item_b: IItem) -> bool:
        return ((item_a.name == ItemName.CANDLE and 
                 item_b.name in [ItemName.OIL, ItemName.GASOLINE]) or
                (item_b.name == ItemName.CANDLE and 
                 item_a.name in [ItemName.OIL, ItemName.GASOLINE]))
    
    def combine(self, item_a: IItem, item_b: IItem) -> CombinationResult:
        item_a.use()
        item_b.use()
        
        consumed = []
        if item_a.uses_remaining <= 0:
            consumed.append(item_a)
        if item_b.uses_remaining <= 0:
            consumed.append(item_b)
        
        return CombinationResult(
            kills_all_zombies=True,
            items_consumed=consumed
        )


class ChainsawWithGasolineRule(CombinationRule):
    def can_combine(self, item_a: IItem, item_b: IItem) -> bool:
        return ((item_a.name == ItemName.CHAINSAW and item_b.name == ItemName.GASOLINE) or
                (item_b.name == ItemName.CHAINSAW and item_a.name == ItemName.GASOLINE))
    
    def combine(self, item_a: IItem, item_b: IItem) -> CombinationResult:
        chainsaw = None
        gasoline = None
        
        if item_a.name == ItemName.CHAINSAW:
            chainsaw = item_a
            gasoline = item_b
        else:
            chainsaw = item_b
            gasoline = item_a
        
        if isinstance(chainsaw, SpecialWeaponItem):
            chainsaw.add_uses(GASOLINE_CHAINSAW_USES)
        
        gasoline.use()
        
        consumed = []
        if gasoline.uses_remaining <= 0:
            consumed.append(gasoline)
        
        return CombinationResult(
            kills_all_zombies=False,
            items_consumed=consumed
        )