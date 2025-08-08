from abc import ABC, abstractmethod
from dev_card import DevCard
from tile import Tile
from enums_and_types import *

class game_pieces(ABC):
    
    @abstractmethod
    def setup(self) -> None:
        pass
    
    @abstractmethod
    def draw_dev_card(self) -> DevCard:
        pass

    @abstractmethod
    def dev_cards_remaining(self) -> int:
        pass

    @abstractmethod
    def draw_indoor_tile(self) -> Tile:
        pass

    @abstractmethod
    def indoor_tiles_remaining(self) -> int:
        pass

    @abstractmethod
    def draw_outdoor_tile(self) -> Tile:
        pass

    @abstractmethod
    def outdoor_tiles_remaining(self) -> int:
        pass

    @abstractmethod
    def can_place_tile(self, position: Position, rotation: Rotation) -> bool:
        pass

    @abstractmethod
    def place_tile(self, position: Position, rotation: Rotation) -> None:
        pass