from model.game_pieces.tile import Tile
import unittest
from enums_and_types import *

class TestTile(unittest.TestCase):

    def setUp(self) -> None:
        self.family_room_tile = Tile(
            "Family Room",
            False,
            (Direction.WEST, Direction.NORTH, Direction.EAST),
            None,
            None
        )

        self.patio_tile = Tile(
            "Patio",
            True,
            (Direction.NORTH, Direction.EAST, Direction.SOUTH),
            Direction.NORTH,
            None
        )

    def test_get_name(self):
        self.assertEqual(self.family_room_tile.get_name(), "Family Room")

    def test_is_outdoors(self):
        self.assertTrue(self.patio_tile.is_outdoors())
        self.assertFalse(self.family_room_tile.is_outdoors())
    
    def test_get_exits_no_rotation(self):
        self.assertIn(Direction.WEST,
                      self.family_room_tile.get_exits(Rotation.NONE))
        self.assertIn(Direction.NORTH,
                      self.family_room_tile.get_exits(Rotation.NONE))
        self.assertIn(Direction.EAST,
                      self.family_room_tile.get_exits(Rotation.NONE))
        self.assertNotIn(Direction.SOUTH,
                      self.family_room_tile.get_exits(Rotation.NONE))

    def test_get_exits_clockwise(self):
        self.assertIn(Direction.NORTH,
                      self.family_room_tile.get_exits(Rotation.CLOCKWISE))
        self.assertIn(Direction.EAST,
                      self.family_room_tile.get_exits(Rotation.CLOCKWISE))
        self.assertIn(Direction.SOUTH,
                      self.family_room_tile.get_exits(Rotation.CLOCKWISE))
        self.assertNotIn(Direction.WEST,
                      self.family_room_tile.get_exits(Rotation.CLOCKWISE))
    
    def test_get_exits_anticlockwise(self):
        self.assertIn(Direction.SOUTH,
                      self.family_room_tile.get_exits(Rotation.ANTICLOCKWISE))
        self.assertIn(Direction.WEST,
                      self.family_room_tile.get_exits(Rotation.ANTICLOCKWISE))
        self.assertIn(Direction.NORTH,
                      self.family_room_tile.get_exits(Rotation.ANTICLOCKWISE))
        self.assertNotIn(Direction.EAST,
                      self.family_room_tile.get_exits(Rotation.ANTICLOCKWISE))
    
    def test_get_exits_upside_down(self):
        self.assertIn(Direction.EAST,
                      self.family_room_tile.get_exits(Rotation.UPSIDE_DOWN))
        self.assertIn(Direction.SOUTH,
                      self.family_room_tile.get_exits(Rotation.UPSIDE_DOWN))
        self.assertIn(Direction.WEST,
                      self.family_room_tile.get_exits(Rotation.UPSIDE_DOWN))
        self.assertNotIn(Direction.NORTH,
                      self.family_room_tile.get_exits(Rotation.UPSIDE_DOWN))
    
    def test_get_front_door_no_rotation(self):
        self.assertIsNone(self.family_room_tile.get_front_door(Rotation.NONE))
        self.assertEqual(self.patio_tile.get_front_door(Rotation.NONE),
                         Direction.NORTH)
    
    def test_get_front_door_clockwise(self):
        self.assertEqual(self.patio_tile.get_front_door(Rotation.CLOCKWISE),
                         Direction.EAST)
        
    def test_get_front_door_anticlockwise(self):
        self.assertEqual(self.patio_tile.get_front_door(Rotation.ANTICLOCKWISE),
                         Direction.WEST)
    
    def test_get_front_door_upside_down(self):
        self.assertEqual(self.patio_tile.get_front_door(Rotation.UPSIDE_DOWN),
                         Direction.SOUTH)