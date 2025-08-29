from ..interfaces import IItem
from .combination_rules import (
    CombinationRule,
    CombinationResult,
    CandleWithFlammableRule,
    ChainsawWithGasolineRule
)


class CombinationEngine:
    def __init__(self):
        self._rules: list[CombinationRule] = [
            CandleWithFlammableRule(),
            ChainsawWithGasolineRule()
        ]

    def can_combine(self, item_a: IItem, item_b: IItem) -> bool:
        if not self._basic_combination_check(item_a, item_b):
            return False

        return any(rule.can_combine(item_a, item_b) for rule in self._rules)

    def combine(self, item_a: IItem, item_b: IItem) -> CombinationResult:
        if not self._basic_combination_check(item_a, item_b):
            raise ValueError("Items cannot be combined")

        for rule in self._rules:
            if rule.can_combine(item_a, item_b):
                return rule.combine(item_a, item_b)

        raise ValueError("No combination rule found for these items")

    def _basic_combination_check(self, item_a: IItem, item_b: IItem) -> bool:
        return (item_a.name in item_b.combinable_with and
                item_b.name in item_a.combinable_with)


_combination_engine = CombinationEngine()


def combine_items(item_a: IItem, item_b: IItem) -> bool:
    if not _combination_engine.can_combine(item_a, item_b):
        raise ValueError("Items cannot be combined")

    result = _combination_engine.combine(item_a, item_b)
    return result.kills_all_zombies
