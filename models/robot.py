from models.parts import Part

class Robot(Part): 
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15, defense_level=1, energy_consumption=10),
            Part("Left arm", attack_level=3, defense_level=20, energy_consumption=10),
            Part("Right arm", attack_level=6, defense_level=20, energy_consumption=10),
            Part("Left leg", attack_level=4, defense_level=20, energy_consumption=15),
            Part("Right leg", attack_level=8, defense_level=20, energy_consumption=15),
        ]