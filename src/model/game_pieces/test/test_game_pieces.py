import unittest
from .. import GamePieces, Tile
from enums_and_types import *

class TestGamePieces(unittest.TestCase):

    def setUp(self) -> None:
        self.game_pieces = GamePieces()

        self.bathroom_tile = Tile("Bathroom", False,
                (Direction.NORTH,),
                None, None)
        
        self.dining_room_tile = Tile("Dining Room", False,
                (Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST),
                Direction.NORTH, None)
        
        self.family_room_tile = Tile("Family Room", False,
                (Direction.NORTH, Direction.EAST, Direction.WEST),
                None, None)
        
        self.patio_tile = Tile("Patio", True,
                (Direction.NORTH, Direction.EAST, Direction.SOUTH),
                Direction.NORTH, None)
        
        self.garden_tile = Tile("Garden", True,
                (Direction.EAST, Direction.SOUTH, Direction.WEST),
                None, None)
    
    def test_seven_indoor_cards(self):
        self.assertEqual(self.game_pieces.indoor_tiles_remaining(), 7)
    
    def test_eight_outdoor_cards(self):
        self.assertEqual(self.game_pieces.outdoor_tiles_remaining(), 8)

    def test_draw_indoor_card_decrements_count(self):
        self.game_pieces.draw_indoor_tile()
        self.assertEqual(self.game_pieces.indoor_tiles_remaining(), 6)
    
    def test_draw_outdoor_card_decrements_count(self):
        self.game_pieces.draw_outdoor_tile()
        self.assertEqual(self.game_pieces.outdoor_tiles_remaining(), 7)

    def test_foyer_is_at_origin(self):
        self.assertEqual(
            self.game_pieces.get_tile((0, 0)).get_name(), "Foyer")

    def test_can_add_upside_down_bathroom_above(self):
        self.assertTrue(self.game_pieces.can_place_tile(
            self.bathroom_tile, (0, 1), (0, 0), Rotation.UPSIDE_DOWN
        ))

        self.assertFalse(self.game_pieces.can_place_tile(
            self.bathroom_tile, (0, 1), (0, 0), Rotation.NONE
        ))
        self.assertFalse(self.game_pieces.can_place_tile(
            self.bathroom_tile, (0, 1), (0, 0), Rotation.CLOCKWISE
        ))
        self.assertFalse(self.game_pieces.can_place_tile(
            self.bathroom_tile, (0, 1), (0, 0), Rotation.ANTICLOCKWISE
        ))
        self.game_pieces.place_tile(self.bathroom_tile,
                                    (0, 1), Rotation.UPSIDE_DOWN)
        self.assertEqual(
            self.game_pieces.get_tile((0, 1)).get_name(), "Bathroom")
    
    def test_can_not_go_out_front_door_to_garden(self):
        self.game_pieces.place_tile(self.dining_room_tile,
                                    (0, 1), Rotation.NONE)
        self.assertTrue(self.game_pieces.can_place_tile(
            self.bathroom_tile, (0, 2), (0, 1), Rotation.UPSIDE_DOWN
        ))
        self.assertFalse(self.game_pieces.can_place_tile(
            self.garden_tile, (0, 2), (0, 1), Rotation.NONE
        ))
    
    def test_can_not_go_out_front_door_to_patio_not_rotated(self):
        self.game_pieces.place_tile(self.dining_room_tile,
                                    (0, 1), Rotation.NONE)
        self.assertFalse(self.game_pieces.can_place_tile(
            self.patio_tile, (0, 2), (0, 1), Rotation.NONE
        ))
    
    def test_can_go_out_front_door_to_patio_upside_down(self):
        self.game_pieces.place_tile(self.dining_room_tile,
                                    (0, 1), Rotation.NONE)
        self.assertTrue(self.game_pieces.can_place_tile(
            self.patio_tile, (0, 2), (0, 1), Rotation.UPSIDE_DOWN
        ))
    
    def test_is_stuck_starts_false(self):
        self.assertFalse(self.game_pieces.is_stuck())

    def test_is_stuck_is_true_with_bathroom_above(self):
        self.game_pieces.place_tile(self.bathroom_tile,
                                    (0, 1), Rotation.UPSIDE_DOWN)
        self.assertTrue(self.game_pieces.is_stuck())
    
    def test_complex_stuck_scenario(self):
        self.game_pieces.place_tile(self.family_room_tile,
                                    (0, 1), Rotation.UPSIDE_DOWN)
        self.game_pieces.place_tile(self.bathroom_tile,
                                    (1, 1), Rotation.CLOCKWISE)
        
        self.assertFalse(self.game_pieces.is_stuck())
        self.game_pieces.place_tile(self.bathroom_tile,
                                    (-1, 1), Rotation.ANTICLOCKWISE)
        self.assertTrue(self.game_pieces.is_stuck())
        
