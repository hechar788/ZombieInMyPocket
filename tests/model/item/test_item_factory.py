import unittest
from src.model.item import get_item, get_all_items
from src.model.item.base_item import ConsumableItem, WeaponItem, CombinableItem, SpecialWeaponItem
from src.enums_and_types import ItemName, ItemType


class TestItemFactory(unittest.TestCase):

    def test_get_item_chainsaw_returns_special_weapon(self):
        # Arrange & Act
        item = get_item(ItemName.CHAINSAW)
        
        # Assert
        self.assertIsInstance(item, SpecialWeaponItem)
        self.assertEqual(item.name, ItemName.CHAINSAW)
        self.assertEqual(item.type, ItemType.WEAPON)
        self.assertEqual(item.attack_bonus, 3)
        self.assertEqual(item.uses_remaining, 2)
        self.assertIn(ItemName.GASOLINE, item.combinable_with)

    def test_get_item_can_of_soda_returns_consumable(self):
        # Arrange & Act
        item = get_item(ItemName.CAN_OF_SODA)
        
        # Assert
        self.assertIsInstance(item, ConsumableItem)
        self.assertEqual(item.name, ItemName.CAN_OF_SODA)
        self.assertEqual(item.type, ItemType.HEALING)
        self.assertEqual(item.heal_amount, 2)
        self.assertEqual(item.uses_remaining, 1)

    def test_get_item_machete_returns_weapon(self):
        # Arrange & Act
        item = get_item(ItemName.MACHETE)
        
        # Assert
        self.assertIsInstance(item, WeaponItem)
        self.assertEqual(item.name, ItemName.MACHETE)
        self.assertEqual(item.type, ItemType.WEAPON)
        self.assertEqual(item.attack_bonus, 2)
        self.assertEqual(item.uses_remaining, 99)

    def test_get_item_oil_returns_combinable(self):
        # Arrange & Act
        item = get_item(ItemName.OIL)
        
        # Assert
        self.assertIsInstance(item, CombinableItem)
        self.assertEqual(item.name, ItemName.OIL)
        self.assertEqual(item.type, ItemType.ESCAPE)
        self.assertEqual(item.uses_remaining, 1)
        self.assertIn(ItemName.CANDLE, item.combinable_with)

    def test_get_item_candle_returns_combinable(self):
        # Arrange & Act
        item = get_item(ItemName.CANDLE)
        
        # Assert
        self.assertIsInstance(item, CombinableItem)
        self.assertEqual(item.name, ItemName.CANDLE)
        self.assertEqual(item.type, ItemType.COMBINE_ONLY)
        self.assertIn(ItemName.OIL, item.combinable_with)
        self.assertIn(ItemName.GASOLINE, item.combinable_with)

    def test_get_item_gasoline_returns_combinable(self):
        # Arrange & Act
        item = get_item(ItemName.GASOLINE)
        
        # Assert
        self.assertIsInstance(item, CombinableItem)
        self.assertEqual(item.name, ItemName.GASOLINE)
        self.assertEqual(item.type, ItemType.COMBINE_ONLY)
        self.assertIn(ItemName.CANDLE, item.combinable_with)
        self.assertIn(ItemName.CHAINSAW, item.combinable_with)

    def test_get_item_all_weapons(self):
        # Arrange
        weapon_names = [
            ItemName.BOARD_WITH_NAILS,
            ItemName.GRISLY_FEMUR,
            ItemName.GOLF_CLUB,
            ItemName.MACHETE,
            ItemName.CHAINSAW
        ]
        
        # Act & Assert
        for weapon_name in weapon_names:
            with self.subTest(weapon=weapon_name):
                item = get_item(weapon_name)
                self.assertEqual(item.type, ItemType.WEAPON)
                self.assertGreater(item.attack_bonus, 0)

    def test_get_all_items_returns_all_nine_items(self):
        # Arrange & Act
        all_items = get_all_items()
        
        # Assert
        self.assertEqual(len(all_items), 9)
        item_names = [item.name for item in all_items]
        
        expected_names = [
            ItemName.OIL,
            ItemName.GASOLINE,
            ItemName.BOARD_WITH_NAILS,
            ItemName.CAN_OF_SODA,
            ItemName.GRISLY_FEMUR,
            ItemName.GOLF_CLUB,
            ItemName.CANDLE,
            ItemName.CHAINSAW,
            ItemName.MACHETE
        ]
        
        for expected_name in expected_names:
            self.assertIn(expected_name, item_names)

    def test_get_all_items_creates_unique_instances(self):
        # Arrange & Act
        all_items_1 = get_all_items()
        all_items_2 = get_all_items()
        
        # Assert
        self.assertEqual(len(all_items_1), len(all_items_2))
        
        # Each call should create new instances
        for i in range(len(all_items_1)):
            self.assertIsNot(all_items_1[i], all_items_2[i])
            self.assertEqual(all_items_1[i].name, all_items_2[i].name)

    def test_get_item_creates_unique_instances(self):
        # Arrange & Act
        item1 = get_item(ItemName.CHAINSAW)
        item2 = get_item(ItemName.CHAINSAW)
        
        # Assert
        self.assertIsNot(item1, item2)
        self.assertEqual(item1.name, item2.name)
        self.assertEqual(item1.uses_remaining, item2.uses_remaining)


if __name__ == '__main__':
    unittest.main()