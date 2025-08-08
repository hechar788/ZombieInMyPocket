from abc import ABC, abstractmethod

class game_pieces(ABC):
    
    @abstractmethod
    def setup():
        pass
    
    @abstractmethod
    def draw_dev_card():
        pass