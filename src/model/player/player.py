from ..interfaces.i_player import IPlayer
from ..interfaces.i_item import IItem
from enums_and_types.types import Position


class Player(IPlayer):
    """Wrapper class that implements the IPlayer interface."""
    def __init__(self, initial_health: int = 100,
                 initial_position: Position = (0, 0),
                 base_attack_power: int = 10):
        self.__player_impl = PlayerImplementation(
            initial_health, initial_position, base_attack_power)

    def get_health(self) -> int:
        return self.__player_impl.health

    def get_attack_power(self) -> int:
        return self.__player_impl.attack_power

    def get_position(self) -> Position:
        return self.__player_impl.position

    def set_position(self, position: Position) -> None:
        self.__player_impl.position = position

    def get_inventory(self) -> list[IItem]:
        return self.__player_impl.inventory

    def take_damage(self, amount: int) -> None:
        self.__player_impl.take_damage(amount)

    def heal(self, amount: int) -> None:
        self.__player_impl.heal(amount)

    def has_totem(self) -> bool:
        return self.__player_impl.has_totem

    def use_item(self, item: IItem) -> None:
        self.__player_impl.use_item(item)

    def add_item_to_inventory(self, item: IItem) -> None:
        self.__player_impl.add_item_to_inventory(item)

    def remove_item_from_inventory(self, item: IItem) -> None:
        self.__player_impl.remove_item_from_inventory(item)

    def combine_items_from_inventory(self) -> None:
        self.__player_impl.combine_items_from_inventory()


class PlayerImplementation:
    """Concrete implementation of the IPlayer interface."""

    def __init__(self, initial_health: int, initial_position: Position,
                 base_attack_power: int):
        self._health = initial_health
        self._base_attack_power = base_attack_power
        self._inventory: list[IItem] = []
        self._position = initial_position
        self._has_totem = False

    @property
    def health(self) -> int:
        return self._health

    @property
    def attack_power(self) -> int:
        item_bonus = sum(item.attack_bonus for item in self._inventory)
        return self._base_attack_power + item_bonus

    @property
    def has_totem(self) -> bool:
        return self._has_totem

    @property
    def inventory(self) -> list[IItem]:
        return self._inventory.copy()

    @property
    def position(self) -> Position:
        return self._position

    @position.setter
    def position(self, position: Position) -> None:
        self._position = position

    def take_damage(self, amount: int) -> None:
        self._health = max(0, self._health - amount)

    def heal(self, amount: int) -> None:
        self._health += amount

    def use_item(self, item: IItem) -> None | int:
        if item in self._inventory:
            if item.type.value == 1:
                self.heal(item.heal_amount)
            
            if item.is_single_use:
                self._inventory.remove(item)

    def add_item_to_inventory(self, item: IItem) -> None:
        self._inventory.append(item)

    def remove_item_from_inventory(self, item: IItem) -> None:
        if item in self._inventory:
            self._inventory.remove(item)

    def combine_items_from_inventory(self) -> None:
        pass
