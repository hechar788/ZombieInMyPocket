from ..interfaces.i_dev_card import IDevCard
from ..interfaces.i_item import IItem
from ..interfaces.i_encounter import IEncounter
from ..item import get_item
from src.enums_and_types import ItemName
from ..encounters.encounters import MessageEncounter


class DevCard(IDevCard):

    def __init__(self, item: IItem,
                 encounter_9pm: IEncounter,
                 encounter_10pm: IEncounter,
                 encounter_11pm: IEncounter) -> None:
        self._item = item
        self._encounters = (encounter_9pm, encounter_10pm, encounter_11pm)

    def get_item(self) -> IItem:
        return self._item

    def get_encounter(self, time: int) -> IEncounter:
        assert 9 <= time <= 11, \
            f"Cannot get an ecounter from dev card at time {time}pm"
        return self._encounters[time - 9]

    @staticmethod
    def get_dev_cards() -> list[IDevCard]:
        return [
            DevCard(
                get_item(ItemName.OIL),
                MessageEncounter()
            )
        ]

        def create_encounter(encounter: IEncounter, values) -> IEncounter:
            encounter.set_values(values)
            return encounter
