import typing
from abc import ABC, abstractmethod

class State(object, ABC):
    """The parent state class"""
    @abstractmethod
    def enter(self):
        """run when the state is entered"""
        pass

    @abstractmethod
    def handle_request(self, data):
        """resumes for where the state left off"""
        pass

    @abstractmethod
    def exit(self):
        """run when the state is exited"""
        pass

