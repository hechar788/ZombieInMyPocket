from enums_and_types import *
from model.game_pieces.i_tile import ITile
from model.encounter.i_encounter import IEncounter

class Tile(ITile):
    
    def __init__(self,
                 name: str,
                 is_outdoors: bool,
                 exits: tuple[Direction, ...],
                 front_door: Direction | None,
                 encounter: IEncounter | None
                 ) -> None:
        self._name = name
        self._is_outdoors = is_outdoors
        self._exits = exits
        self._front_door = front_door
        self._encounter = encounter
    
    def get_name(self) -> str:
        return self._name
    
    def is_outdoors(self) -> bool:
        return self._is_outdoors
    
    def get_exits(self, rotation: Rotation) -> tuple[Direction, ...]:

        # This only works if the rotation and direction enums
        # are in a specific way
        return tuple(Direction(
            (x.value + rotation.value) % 4) for x in self._exits)

    def get_front_door(self, rotation: Rotation) -> Direction | None:
        if self._front_door is None:
            return None
        else:
            return Direction((self._front_door.value + rotation.value) % 4)
    
    def get_encounter(self) -> IEncounter | None:
        return self._encounter