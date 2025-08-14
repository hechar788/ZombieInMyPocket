from abc import abstractmethod

class IGameStateManager():
    """Interface for win/loss outcomes. Also known as IWinLossHandler"""
    @abstractmethod
    def is_game_finished(self) -> bool:
        pass

    @abstractmethod
    def reset_game(self):
        """Resets game to start state for new game play"""
        pass

    @abstractmethod
    def stop_game(self):
        """stops all player actions and locks game interactions (e.g. drawing dev cards, moving through tiles, picking items)"""
        pass

