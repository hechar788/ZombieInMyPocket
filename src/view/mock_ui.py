from typing import Callable


def get_input(prompt: str, options: list[str]) -> str:
    user_input = ""
    while user_input not in options:
        user_input = input(prompt)
    return user_input

