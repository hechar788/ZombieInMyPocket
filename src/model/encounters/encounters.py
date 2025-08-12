from abc import ABC, abstractmethod

class IEncounter(ABC):
    """Abstract Class for building other Encounter Classes"""
    @abstractmethod
    def set_values(self, value):
        ...

    @abstractmethod
    def handle_encounter(self, player):
        ...

class HealthEncounter(IEncounter):
    """Handles Health Encounters"""
    def __init__(self):
        self.health = 0

    def set_values(self, value):
        self.health = value

    def handle_encounter(self, player):
        player.heal(self.health)
        return player

class ItemEncounter(IEncounter):
    """Handles Item Encounters"""
    def __init__(self):
        self.item = None

    def set_values(self, new_item):
        self.item = new_item

    def handle_encounter(self, player):
        player.add_item_to_inventory(self.item)
        return player

class MessageEncounter(IEncounter):
    """Handles Message Encounters"""
    def __init__(self):
        self.message_code = 0

    def set_values(self, new_code):
        self.message_code = new_code

    def handle_encounter(self, player):
        pass


class TotemEncounter(IEncounter):
    """Handles Item Encounters"""
    def __init__(self):
        pass

    def set_values(self, new_item):
        pass

    def handle_encounter(self, player):
        pass
