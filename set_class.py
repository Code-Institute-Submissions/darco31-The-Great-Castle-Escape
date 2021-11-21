"""
Class setup for the games weapons
"""


class Weapon:
    """
    Class setup for a weapon type and the condition
    of the weapons.
    """
    def __init__(self, weapon_type, condition, weight):
        self.weapon_type = weapon_type
        self.condition = condition
        self.weight = weight

    def __str__(self):
        return "{self.weapon_type}, {self.condition}, {self.weight}"
