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

