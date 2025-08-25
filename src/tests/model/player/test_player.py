import unittest
from unittest.mock import Mock, patch
from src.model.player.player import Player, PlayerImplementation
from src.model.interfaces.i_item import IItem

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.custom_player = Player(initial_health=50, initial_position=(5, 10), base_attack_power=3)

    def test_init_default_values(self):
        player = Player()
        self.assertEqual(player.get_health(), 100)
        self.assertEqual(player.get_position(), (0, 0))
        self.assertEqual(player.get_attack_power(), 1)

    def test_init_custom_values(self):
        player = Player(initial_health=75, initial_position=(3, 7), base_attack_power=5)
        self.assertEqual(player.get_health(), 75)
        self.assertEqual(player.get_position(), (3, 7))
        self.assertEqual(player.get_attack_power(), 5)

    def test_get_health(self):
        self.assertEqual(self.player.get_health(), 100)
        self.assertEqual(self.custom_player.get_health(), 50)

    def test_get_attack_power(self):
        self.assertEqual(self.player.get_attack_power(), 1)
        self.assertEqual(self.custom_player.get_attack_power(), 3)

    def test_get_position(self):
        self.assertEqual(self.player.get_position(), (0, 0))
        self.assertEqual(self.custom_player.get_position(), (5, 10))

    def test_set_position(self):
        new_position = (10, 20)
        self.player.set_position(new_position)
        self.assertEqual(self.player.get_position(), new_position)

    def test_get_inventory(self):
        inventory = self.player.get_inventory()
        self.assertEqual(inventory, [])
        self.assertIsInstance(inventory, list)

    def test_take_damage(self):
        self.player.take_damage(30)
        self.assertEqual(self.player.get_health(), 70)

    def test_heal(self):
        self.player.heal(20)
        self.assertEqual(self.player.get_health(), 120)

    def test_has_totem(self):
        self.assertFalse(self.player.has_totem())

    def test_use_item(self):
        mock_item = Mock(spec=IItem)
        self.player.use_item(mock_item)
        # Verify the method calls through to implementation

    def test_add_item_to_inventory(self):
        mock_item = Mock(spec=IItem)
        self.player.add_item_to_inventory(mock_item)
        # Verify the method calls through to implementation

    def test_remove_item_from_inventory(self):
        mock_item = Mock(spec=IItem)
        self.player.remove_item_from_inventory(mock_item)
        # Verify the method calls through to implementation

    def test_combine_items_from_inventory(self):
        self.player.combine_items_from_inventory()
        # Verify the method calls through to implementation


class TestPlayerImplementation(unittest.TestCase):

    def setUp(self):
        self.player_impl = PlayerImplementation(initial_health=100, initial_position=(0, 0), base_attack_power=1)
        self.custom_player_impl = PlayerImplementation(initial_health=50, initial_position=(5, 10), base_attack_power=3)

    def test_init(self):
        impl = PlayerImplementation(75, (3, 7), 5)
        self.assertEqual(impl.health, 75)
        self.assertEqual(impl.position, (3, 7))
        self.assertEqual(impl.attack_power, 5)
        self.assertEqual(impl.inventory, [])
        self.assertFalse(impl.has_totem)

    def test_health_property(self):
        self.assertEqual(self.player_impl.health, 100)
        self.assertEqual(self.custom_player_impl.health, 50)

    def test_attack_power_property(self):
        self.assertEqual(self.player_impl.attack_power, 1)
        self.assertEqual(self.custom_player_impl.attack_power, 3)

    def test_has_totem_property(self):
        self.assertFalse(self.player_impl.has_totem)

    def test_inventory_property_returns_copy(self):
        mock_item = Mock(spec=IItem)
        self.player_impl._inventory.append(mock_item)
        
        inventory_copy = self.player_impl.inventory
        self.assertEqual(len(inventory_copy), 1)
        
        # Modify the copy and ensure original is unchanged
        inventory_copy.clear()
        self.assertEqual(len(self.player_impl._inventory), 1)

    def test_position_property_getter(self):
        self.assertEqual(self.player_impl.position, (0, 0))
        self.assertEqual(self.custom_player_impl.position, (5, 10))

    def test_position_property_setter(self):
        new_position = (15, 25)
        self.player_impl.position = new_position
        self.assertEqual(self.player_impl.position, new_position)

    def test_take_damage_normal(self):
        self.player_impl.take_damage(30)
        self.assertEqual(self.player_impl.health, 70)

    def test_take_damage_excessive(self):
        self.player_impl.take_damage(150)
        self.assertEqual(self.player_impl.health, 0)

    def test_take_damage_zero(self):
        self.player_impl.take_damage(0)
        self.assertEqual(self.player_impl.health, 100)

    def test_heal(self):
        self.player_impl._health = 50
        self.player_impl.heal(30)
        self.assertEqual(self.player_impl.health, 80)

    def test_heal_zero(self):
        original_health = self.player_impl.health
        self.player_impl.heal(0)
        self.assertEqual(self.player_impl.health, original_health)

    def test_use_item_healing_type(self):
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 1  # HEALING
        mock_item.heal_amount = 25
        mock_item.uses_remaining = 1
        
        self.player_impl._inventory = [mock_item]
        self.player_impl._health = 75
        
        result = self.player_impl.use_item(mock_item)
        
        self.assertEqual(self.player_impl.health, 100)
        self.assertIsNone(result)

    def test_use_item_weapon_type(self):
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 0  # WEAPON
        mock_item.attack_bonus = 5
        mock_item.uses_remaining = 1
        
        self.player_impl._inventory = [mock_item]
        
        result = self.player_impl.use_item(mock_item)
        
        self.assertEqual(result, 6)  # base_attack_power (1) + attack_bonus (5)

    def test_use_item_removes_when_no_uses_remaining(self):
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 1  # HEALING
        mock_item.heal_amount = 25
        mock_item.uses_remaining = 0
        
        self.player_impl._inventory = [mock_item]
        
        self.player_impl.use_item(mock_item)
        
        self.assertEqual(len(self.player_impl._inventory), 0)

    def test_use_item_not_in_inventory(self):
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 1
        mock_item.heal_amount = 25
        
        result = self.player_impl.use_item(mock_item)
        
        self.assertIsNone(result)
        self.assertEqual(self.player_impl.health, 100)  # Unchanged

    def test_use_item_other_type(self):
        mock_item = Mock(spec=IItem)
        mock_item.type.value = 2  # Neither HEALING nor WEAPON
        mock_item.uses_remaining = 1
        
        self.player_impl._inventory = [mock_item]
        
        result = self.player_impl.use_item(mock_item)
        
        self.assertIsNone(result)

    def test_add_item_to_inventory_under_limit(self):
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        
        self.player_impl.add_item_to_inventory(mock_item1)
        self.assertEqual(len(self.player_impl._inventory), 1)
        
        self.player_impl.add_item_to_inventory(mock_item2)
        self.assertEqual(len(self.player_impl._inventory), 2)

    def test_add_item_to_inventory_at_limit(self):
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        mock_item3 = Mock(spec=IItem)
        
        self.player_impl.add_item_to_inventory(mock_item1)
        self.player_impl.add_item_to_inventory(mock_item2)
        self.player_impl.add_item_to_inventory(mock_item3)  # Should not be added
        
        self.assertEqual(len(self.player_impl._inventory), 2)
        self.assertNotIn(mock_item3, self.player_impl._inventory)

    def test_remove_item_from_inventory_item_exists(self):
        mock_item = Mock(spec=IItem)
        self.player_impl._inventory = [mock_item]
        
        self.player_impl.remove_item_from_inventory(mock_item)
        
        self.assertEqual(len(self.player_impl._inventory), 0)

    def test_remove_item_from_inventory_item_not_exists(self):
        mock_item1 = Mock(spec=IItem)
        mock_item2 = Mock(spec=IItem)
        self.player_impl._inventory = [mock_item1]
        
        self.player_impl.remove_item_from_inventory(mock_item2)
        
        self.assertEqual(len(self.player_impl._inventory), 1)
        self.assertIn(mock_item1, self.player_impl._inventory)

    @patch('src.model.player.player.combine_items')
    def test_combine_items_from_inventory_success(self, mock_combine_items):
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 0
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 1
        
        self.player_impl._inventory = [mock_item1, mock_item2]
        mock_combine_items.return_value = True
        
        result = self.player_impl.combine_items_from_inventory()
        
        self.assertTrue(result)
        mock_combine_items.assert_called_once_with(mock_item1, mock_item2)
        self.assertEqual(len(self.player_impl._inventory), 1)
        self.assertNotIn(mock_item1, self.player_impl._inventory)
        self.assertIn(mock_item2, self.player_impl._inventory)

    @patch('src.model.player.player.combine_items')
    def test_combine_items_from_inventory_both_items_depleted(self, mock_combine_items):
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 0
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 0
        
        self.player_impl._inventory = [mock_item1, mock_item2]
        mock_combine_items.return_value = True
        
        result = self.player_impl.combine_items_from_inventory()
        
        self.assertTrue(result)
        self.assertEqual(len(self.player_impl._inventory), 0)

    @patch('src.model.player.player.combine_items')
    def test_combine_items_from_inventory_assertion_error(self, mock_combine_items):
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 1
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 1
        
        self.player_impl._inventory = [mock_item1, mock_item2]
        mock_combine_items.side_effect = AssertionError("Cannot combine these items")
        
        result = self.player_impl.combine_items_from_inventory()
        
        self.assertFalse(result)
        self.assertEqual(len(self.player_impl._inventory), 2)  # Items remain

    def test_combine_items_from_inventory_less_than_two_items(self):
        mock_item = Mock(spec=IItem)
        self.player_impl._inventory = [mock_item]
        
        result = self.player_impl.combine_items_from_inventory()
        
        self.assertFalse(result)

    def test_combine_items_from_inventory_empty_inventory(self):
        result = self.player_impl.combine_items_from_inventory()
        
        self.assertFalse(result)

    @patch('src.model.player.player.combine_items')
    def test_combine_items_from_inventory_no_items_depleted(self, mock_combine_items):
        mock_item1 = Mock(spec=IItem)
        mock_item1.uses_remaining = 2
        mock_item2 = Mock(spec=IItem)
        mock_item2.uses_remaining = 3
        
        self.player_impl._inventory = [mock_item1, mock_item2]
        mock_combine_items.return_value = True
        
        result = self.player_impl.combine_items_from_inventory()
        
        self.assertTrue(result)
        self.assertEqual(len(self.player_impl._inventory), 2)  # Both items remain


if __name__ == '__main__':
    unittest.main()