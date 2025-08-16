from typing import Callable

class UserInterface:
    """A mock user interface."""
    def get_input(self, prompt: str, options: list[str]) -> str:
        user_input = ""
        while user_input not in options:
            user_input = input(prompt)
        return user_input

