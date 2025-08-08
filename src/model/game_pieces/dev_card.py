from model.game_pieces.i_dev_card import IDevCard
from model.item.i_item import IItem
from model.encounter.i_encounter import IEncounter

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