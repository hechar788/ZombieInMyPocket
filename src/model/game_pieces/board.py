from game_pieces import *
from src.enums_and_types.types import Position
from ...enums_and_types.enums import Rotation, Direction

type TileDict = dict[Position, ITile]


class Board:

    def __init__(self) -> None:
        self._all_tiles: TileDict = {}

        # Keep track of the number of exits so we know if we
        # are stuck
        self._exits_available = 0

    def reset(self):
        self._all_tiles = {}

    def get_all_tiles(self) -> TileDict:
        return self._all_tiles

    def get_tile(self, position: Position) -> ITile:
        return self._all_tiles[position]

    def place_tile(self, tile: ITile, position: Position,
                   rotation: Rotation) -> None:
        assert position not in self._all_tiles, \
            f"There is already a tile at position {position}"
        tile.set_rotation(rotation)
        self._all_tiles[position] = tile

        # Keep track of exits available
        self._exits_available += len(tile.get_exits())
        if len(self._all_tiles) > 1:
            self._exits_available -= 2

    def can_place_tile(self, tile: ITile, position: Position,
                       position_from: Position, rotation: Rotation) -> bool:
        tile.set_rotation(rotation)

        # Can't add a tile where one already exists
        if position in self._all_tiles:
            return False

        if position_from not in self._all_tiles:
            return False
        tile_from = self._all_tiles[position_from]

        direction = self._direction_from_position(position_from, position)
        if direction == None:
            return False

        reverse_direction = Direction((direction.value + 2) % 4)

        # Handle indoor to outdoor
        if tile_from.is_outdoors() != tile.is_outdoors():

            # Both tiles must have a front door
            if tile_from.get_front_door() == None or \
                    tile.get_front_door() == None:
                return False

            return tile_from.get_front_door() == direction and \
                tile.get_front_door() == reverse_direction

        return direction in tile_from.get_exits() and \
            reverse_direction in tile.get_exits()

    def is_stuck(self) -> bool:
        return self._exits_available <= 0

    def _direction_from_position(self,
                                 position_from: Position,
                                 position_to: Position) -> Direction | None:
        x = position_to[0] - position_from[0]
        y = position_to[1] - position_from[1]

        if x == 1 and y == 0:
            return Direction.EAST
        elif x == -1 and y == 0:
            return Direction.WEST
        elif x == 0 and y == 1:
            return Direction.NORTH
        elif x == 0 and y == -1:
            return Direction.SOUTH
        else:
            return None