from ..interfaces.i_encounter import IEncounter

class ItemEncounter(IEncounter):
    """Handles Item Encounters"""
    def __init__(self):
        self.item = None
        self.status_message = None

    def set_values(self, new_item):
        self.item = new_item

    def handle_encounter(self, player):
        player.add_item_to_inventory(self.item)
        return player

    def handle_status_message(self, message):
        self.status_message = message

class TotemEncounter(IEncounter):
    """Handles Item Encounters"""
    def __init__(self):
        pass

    def set_values(self, new_item):
        pass

    def handle_encounter(self, player):
        pass

    def handle_status_message(self, message):
        pass

class HealthEncounter(IEncounter):
    """Handles Health Encounters"""
    def __init__(self):
        self.health = 0

    def set_values(self, value):
        self.health = value

    def handle_encounter(self, player):
        player.heal(self.health)
        return player

    def handle_status_message(self, message):
        pass
