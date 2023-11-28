from models.logic.robot_attack import Attack
from models.logic.template.robot_template import robot_art

class Part(Attack):
    def __init__(self, name, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name 
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption

    
    # Function that returns a dictionary with the robot's statistics 
    def part_name(self):
        all_parts = {}
        for index, part in enumerate(self.parts):
            part_key = part.name.lower().replace(" ","_")
            part = {
                f"{part_key}_name": part.name,
                f"{part_key}_status": part.is_available(),
                f"{part_key}_attack": part.attack_level,
                f"{part_key}_defense": part.defense_level,
                f"{part_key}_energy_consump": part.energy_consumption,
            }
            all_parts.update(part)
        return all_parts

    # Function that checks if a robot part is available
    def is_available(self):        
        return self.defense_level > 0

    
    # Function that prints the robot_art with the respective values
    def get_status(self):
        robot_stats = self.part_name()
        colored_robot_art = robot_art.format(**robot_stats)
        print(colored_robot_art)