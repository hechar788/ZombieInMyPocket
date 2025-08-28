import unittest
from src.model.item import get_item, combine_items
from src.model.item.base_item import SpecialWeaponItem
from src.enums_and_types import ItemName


class TestCombinationEngine(unittest.TestCase):

    def test_combine_candle_with_oil_kills_all_zombies(self):
        # Arrange
        candle = get_item(ItemName.CANDLE)
        oil = get_item(ItemName.OIL)
        
        # Act
        result = combine_items(candle, oil)
        
        # Assert
        self.assertTrue(result)
        self.assertEqual(candle.uses_remaining, 0)
        self.assertEqual(oil.uses_remaining, 0)

    def test_combine_candle_with_gasoline_kills_all_zombies(self):
        # Arrange
        candle = get_item(ItemName.CANDLE)
        gasoline = get_item(ItemName.GASOLINE)
        
        # Act
        result = combine_items(candle, gasoline)
        
        # Assert
        self.assertTrue(result)
        self.assertEqual(candle.uses_remaining, 0)
        self.assertEqual(gasoline.uses_remaining, 0)

    def test_combine_oil_with_candle_kills_all_zombies(self):
        # Arrange
        oil = get_item(ItemName.OIL)
        candle = get_item(ItemName.CANDLE)
        
        # Act
        result = combine_items(oil, candle)
        
        # Assert
        self.assertTrue(result)
        self.assertEqual(oil.uses_remaining, 0)
        self.assertEqual(candle.uses_remaining, 0)

    def test_combine_gasoline_with_candle_kills_all_zombies(self):
        # Arrange
        gasoline = get_item(ItemName.GASOLINE)
        candle = get_item(ItemName.CANDLE)
        
        # Act
        result = combine_items(gasoline, candle)
        
        # Assert
        self.assertTrue(result)
        self.assertEqual(gasoline.uses_remaining, 0)
        self.assertEqual(candle.uses_remaining, 0)

    def test_combine_chainsaw_with_gasoline_adds_uses(self):
        # Arrange
        chainsaw = get_item(ItemName.CHAINSAW)
        gasoline = get_item(ItemName.GASOLINE)
        initial_chainsaw_uses = chainsaw.uses_remaining
        
        # Act
        result = combine_items(chainsaw, gasoline)
        
        # Assert
        self.assertFalse(result)  # Doesn't kill all zombies
        self.assertEqual(chainsaw.uses_remaining, initial_chainsaw_uses + 2)
        self.assertEqual(gasoline.uses_remaining, 0)

    def test_combine_gasoline_with_chainsaw_adds_uses(self):
        # Arrange
        gasoline = get_item(ItemName.GASOLINE)
        chainsaw = get_item(ItemName.CHAINSAW)
        initial_chainsaw_uses = chainsaw.uses_remaining
        
        # Act
        result = combine_items(gasoline, chainsaw)
        
        # Assert
        self.assertFalse(result)  # Doesn't kill all zombies
        self.assertEqual(chainsaw.uses_remaining, initial_chainsaw_uses + 2)
        self.assertEqual(gasoline.uses_remaining, 0)

    def test_combine_incompatible_items_raises_error(self):
        # Arrange
        chainsaw = get_item(ItemName.CHAINSAW)
        oil = get_item(ItemName.OIL)
        
        # Act & Assert
        with self.assertRaises(ValueError):
            combine_items(chainsaw, oil)

    def test_combine_non_combinable_items_raises_error(self):
        # Arrange
        machete = get_item(ItemName.MACHETE)
        golf_club = get_item(ItemName.GOLF_CLUB)
        
        # Act & Assert
        with self.assertRaises(ValueError):
            combine_items(machete, golf_club)

    def test_combine_item_with_itself_raises_error(self):
        # Arrange
        candle = get_item(ItemName.CANDLE)
        
        # Act & Assert
        with self.assertRaises(ValueError):
            combine_items(candle, candle)

    def test_combine_can_of_soda_with_anything_raises_error(self):
        # Arrange
        soda = get_item(ItemName.CAN_OF_SODA)
        candle = get_item(ItemName.CANDLE)
        
        # Act & Assert
        with self.assertRaises(ValueError):
            combine_items(soda, candle)

    def test_multiple_gasoline_combinations_with_chainsaw(self):
        # Arrange
        chainsaw = get_item(ItemName.CHAINSAW)
        gasoline1 = get_item(ItemName.GASOLINE)
        gasoline2 = get_item(ItemName.GASOLINE)
        initial_uses = chainsaw.uses_remaining
        
        # Act
        combine_items(chainsaw, gasoline1)
        combine_items(chainsaw, gasoline2)
        
        # Assert
        self.assertEqual(chainsaw.uses_remaining, initial_uses + 4)
        self.assertEqual(gasoline1.uses_remaining, 0)
        self.assertEqual(gasoline2.uses_remaining, 0)

    def test_chainsaw_add_uses_method_works(self):
        # Arrange
        chainsaw = get_item(ItemName.CHAINSAW)
        initial_uses = chainsaw.uses_remaining
        
        # Act
        if isinstance(chainsaw, SpecialWeaponItem):
            chainsaw.add_uses(3)
        
        # Assert
        self.assertEqual(chainsaw.uses_remaining, initial_uses + 3)

    def test_combination_preserves_item_properties(self):
        # Arrange
        candle = get_item(ItemName.CANDLE)
        oil = get_item(ItemName.OIL)
        
        original_candle_name = candle.name
        original_candle_type = candle.type
        original_oil_name = oil.name
        original_oil_type = oil.type
        
        # Act
        combine_items(candle, oil)
        
        # Assert - Properties should remain unchanged
        self.assertEqual(candle.name, original_candle_name)
        self.assertEqual(candle.type, original_candle_type)
        self.assertEqual(oil.name, original_oil_name)
        self.assertEqual(oil.type, original_oil_type)


if __name__ == '__main__':
    unittest.main()