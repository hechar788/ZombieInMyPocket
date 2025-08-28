import unittest
from src.model.item.item_config import ItemConfig, ITEM_CONFIGS, GASOLINE_CHAINSAW_USES
from src.enums_and_types import ItemName, ItemType


class TestItemConfig(unittest.TestCase):

    def test_item_config_initialization_with_defaults(self):
        # Arrange & Act
        config = ItemConfig(
            name=ItemName.MACHETE,
            description="Sharp blade",
            item_type=ItemType.WEAPON
        )
        
        # Assert
        self.assertEqual(config.name, ItemName.MACHETE)
        self.assertEqual(config.description, "Sharp blade")
        self.assertEqual(config.item_type, ItemType.WEAPON)
        self.assertEqual(config.attack_bonus, 0)
        self.assertEqual(config.heal_amount, 0)
        self.assertEqual(config.uses, 1)
        self.assertEqual(config.combinable_with, [])

    def test_item_config_initialization_with_all_parameters(self):
        # Arrange & Act
        config = ItemConfig(
            name=ItemName.CHAINSAW,
            description="Motorized weapon",
            item_type=ItemType.WEAPON,
            attack_bonus=3,
            heal_amount=0,
            uses=2,
            combinable_with=[ItemName.GASOLINE]
        )
        
        # Assert
        self.assertEqual(config.name, ItemName.CHAINSAW)
        self.assertEqual(config.description, "Motorized weapon")
        self.assertEqual(config.item_type, ItemType.WEAPON)
        self.assertEqual(config.attack_bonus, 3)
        self.assertEqual(config.heal_amount, 0)
        self.assertEqual(config.uses, 2)
        self.assertEqual(config.combinable_with, [ItemName.GASOLINE])

    def test_item_config_post_init_sets_empty_list(self):
        # Arrange & Act
        config = ItemConfig(
            name=ItemName.MACHETE,
            description="Sharp blade",
            item_type=ItemType.WEAPON,
            combinable_with=None
        )
        
        # Assert
        self.assertEqual(config.combinable_with, [])


class TestItemConfigs(unittest.TestCase):

    def test_all_item_names_have_configs(self):
        # Arrange
        all_item_names = list(ItemName)
        
        # Act & Assert
        for item_name in all_item_names:
            with self.subTest(item=item_name):
                self.assertIn(item_name, ITEM_CONFIGS)

    def test_item_configs_count(self):
        # Arrange & Act
        config_count = len(ITEM_CONFIGS)
        item_name_count = len(ItemName)
        
        # Assert
        self.assertEqual(config_count, item_name_count)

    def test_oil_config(self):
        # Arrange & Act
        config = ITEM_CONFIGS[ItemName.OIL]
        
        # Assert
        self.assertEqual(config.name, ItemName.OIL)
        self.assertEqual(config.item_type, ItemType.ESCAPE)
        self.assertEqual(config.attack_bonus, 0)
        self.assertEqual(config.heal_amount, 0)
        self.assertEqual(config.uses, 1)
        self.assertEqual(config.combinable_with, [ItemName.CANDLE])
        self.assertIn("Throw as you run away", config.description)

    def test_gasoline_config(self):
        # Arrange & Act
        config = ITEM_CONFIGS[ItemName.GASOLINE]
        
        # Assert
        self.assertEqual(config.name, ItemName.GASOLINE)
        self.assertEqual(config.item_type, ItemType.COMBINE_ONLY)
        self.assertEqual(config.combinable_with, [ItemName.CANDLE, ItemName.CHAINSAW])
        self.assertIn("Combine with Candle", config.description)

    def test_chainsaw_config(self):
        # Arrange & Act
        config = ITEM_CONFIGS[ItemName.CHAINSAW]
        
        # Assert
        self.assertEqual(config.name, ItemName.CHAINSAW)
        self.assertEqual(config.item_type, ItemType.WEAPON)
        self.assertEqual(config.attack_bonus, 3)
        self.assertEqual(config.uses, 2)
        self.assertEqual(config.combinable_with, [ItemName.GASOLINE])
        self.assertIn("fuel for 2 battles", config.description)

    def test_can_of_soda_config(self):
        # Arrange & Act
        config = ITEM_CONFIGS[ItemName.CAN_OF_SODA]
        
        # Assert
        self.assertEqual(config.name, ItemName.CAN_OF_SODA)
        self.assertEqual(config.item_type, ItemType.HEALING)
        self.assertEqual(config.heal_amount, 2)
        self.assertEqual(config.uses, 1)
        self.assertEqual(config.combinable_with, [])

    def test_candle_config(self):
        # Arrange & Act
        config = ITEM_CONFIGS[ItemName.CANDLE]
        
        # Assert
        self.assertEqual(config.name, ItemName.CANDLE)
        self.assertEqual(config.item_type, ItemType.COMBINE_ONLY)
        self.assertEqual(config.combinable_with, [ItemName.OIL, ItemName.GASOLINE])
        self.assertIn("Combine with Oil or Gasoline", config.description)

    def test_weapon_configs(self):
        # Arrange
        weapon_configs = [
            (ItemName.BOARD_WITH_NAILS, 1),
            (ItemName.GRISLY_FEMUR, 1),
            (ItemName.GOLF_CLUB, 1),
            (ItemName.MACHETE, 2),
            (ItemName.CHAINSAW, 3)
        ]
        
        # Act & Assert
        for weapon_name, expected_attack in weapon_configs:
            with self.subTest(weapon=weapon_name):
                config = ITEM_CONFIGS[weapon_name]
                self.assertEqual(config.item_type, ItemType.WEAPON)
                self.assertEqual(config.attack_bonus, expected_attack)
                if weapon_name != ItemName.CHAINSAW:
                    self.assertEqual(config.uses, 99)
                    self.assertEqual(config.combinable_with, [])

    def test_all_configs_have_descriptions(self):
        # Arrange & Act & Assert
        for item_name, config in ITEM_CONFIGS.items():
            with self.subTest(item=item_name):
                self.assertIsInstance(config.description, str)
                self.assertGreater(len(config.description), 0)

    def test_all_configs_have_valid_types(self):
        # Arrange
        valid_types = [ItemType.WEAPON, ItemType.HEALING, ItemType.COMBINE_ONLY, ItemType.ESCAPE]
        
        # Act & Assert
        for item_name, config in ITEM_CONFIGS.items():
            with self.subTest(item=item_name):
                self.assertIn(config.item_type, valid_types)

    def test_gasoline_chainsaw_uses_constant(self):
        # Arrange & Act & Assert
        self.assertEqual(GASOLINE_CHAINSAW_USES, 2)
        self.assertIsInstance(GASOLINE_CHAINSAW_USES, int)

    def test_combinable_items_reference_existing_items(self):
        # Arrange
        all_item_names = set(ItemName)
        
        # Act & Assert
        for item_name, config in ITEM_CONFIGS.items():
            with self.subTest(item=item_name):
                for combinable_item in config.combinable_with:
                    self.assertIn(combinable_item, all_item_names)

    def test_symmetric_combinable_relationships(self):
        # Arrange & Act & Assert
        for item_name, config in ITEM_CONFIGS.items():
            for combinable_item_name in config.combinable_with:
                with self.subTest(item=item_name, combinable=combinable_item_name):
                    combinable_config = ITEM_CONFIGS[combinable_item_name]
                    self.assertIn(item_name, combinable_config.combinable_with,
                                f"{item_name} can combine with {combinable_item_name}, "
                                f"but {combinable_item_name} cannot combine with {item_name}")


if __name__ == '__main__':
    unittest.main()