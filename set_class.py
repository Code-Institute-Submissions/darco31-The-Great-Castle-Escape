class Weapon:
    def __init__(self, weapon_type, condition):
        self.weapon_type = weapon_type
        self.condition = condition

    def __str__(self):
        return "{self.weapon_type}, {self.condition}"
