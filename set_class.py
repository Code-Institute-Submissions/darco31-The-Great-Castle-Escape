class Weapon:
    def __init__(self, weapon_type, condition):
        self.weapon_type = weapon_type
        self.condition = condition

    def __str__(self):
        return f"I found a {self.weapon_type } that was very {self.condition}."