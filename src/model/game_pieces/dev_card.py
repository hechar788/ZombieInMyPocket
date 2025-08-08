from abc import ABC, abstractmethod
from model.game_pieces.item import Item

class DevCard(ABC):

    def get_item() -> Item:
        pass