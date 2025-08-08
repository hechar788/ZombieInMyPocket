from abc import ABC, abstractmethod
from model.game_pieces.i_dev_card import IDevCard
from model.game_pieces.i_tile import ITile
from enums_and_types import *

class IGamePieces(ABC):
    
    @abstractmethod
    def setup(self) -> None:
        pass
    
    @abstractmethod
    def draw_dev_card(self) -> IDevCard:
        pass

    @abstractmethod
    def dev_cards_remaining(self) -> int:
        pass

    @abstractmethod
    def draw_indoor_tile(self) -> ITile:
        pass

    @abstractmethod
    def indoor_tiles_remaining(self) -> int:
        pass

    @abstractmethod
    def draw_outdoor_tile(self) -> ITile:
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