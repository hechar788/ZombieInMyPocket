from typing import Callable, Any
from threading import Timer

class UserInterface:
    """A mock user interface."""
    def get_input_with_callback(self, prompt: str, options: list[str], callback: Callable[[Any], None]) -> None:
        """adds mock callback behavior."""
        def delay_call():
            result = self.get_input(prompt, options)
            callback(result)
        Timer(1, delay_call).start()

    @staticmethod
    def get_input(prompt: str, options: list[str]) -> str:
        user_input = ""
        while user_input not in options:
            user_input = input(prompt)
        return user_input