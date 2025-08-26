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

class CowerEncounter(IEncounter):
    """Handles Cower Encounter"""
    def __init__(self):
        self.health_increase = 3

    def set_values(self, value):
        """No values to set"""
        #added by Josiah O'Neill
        pass

    def handle_encounter(self, player):
        player.heal(self.health_increase)
        return player

class CombatEncounter(IEncounter):
    """Handles Combat Encounters"""
    def __init__(self):
        self.zombies = 0

    def set_values(self, value):
        self.zombies = value

    def handle_encounter(self, player):
        damage = self.zombies - player.attack_power
        if damage > 4:
            damage = 4
        elif damage < 0:
            damage = 0
        player.take_damage(damage)
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