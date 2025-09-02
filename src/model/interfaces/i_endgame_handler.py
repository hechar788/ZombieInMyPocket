# Arsenie: [1] Component for User Story 12 - Game set-up start thing
# Used by game_session_manager

class IEndGameHandler(Protocol):
    """Interface for win/loss outcomes. Also known as IWinLossHandler"""
    @abstractmethod
    def handle_win(self, player: Player, condition: EndCondition):
        pass

    @abstractmethod
    def handle_loss(self, player: Player, condition: EndCondition):
        pass

    @abstractmethod
    def reset_game(self):
        pass

