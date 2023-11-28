from models.logic.template.robot_template import robot_art
from models.logic.messages import *
import random 

class Attack():
    def get_user_input(self, prompt):
        while True:
            try: 
                user_input = int(input(prompt))
                if 0 <= user_input < len(self.parts):
                    return user_input
                else:
                    print(INVALID_OPTION)
            except ValueError:
                print(INVALID_INPUT)
        
    def choose_attack_part(self):
        self.get_status()
        part_to_attack = self.get_user_input(PART_TO_ATTACK)
        while not self.parts[part_to_attack].is_available():
            print(INVALID_PART)
            part_to_attack = self.get_user_input(PART_TO_ATTACK)
        return part_to_attack
    
    def choose_target_part(self, enemy_robot):
        target_part = self.get_user_input(TARGET_PART)
        while not enemy_robot.parts[target_part].is_available():
            print(BROKEN_PART)
            target_part = self.get_user_input(TARGET_PART)
        return target_part
        
    def attack(self, robot_list):       
        part_to_attack = self.choose_attack_part()
        potential_targets = [robot for robot in robot_list if robot != self]
        target_robot = random.choice(potential_targets)
        target_part = self.choose_target_part(target_robot)
        self.energy = self.energy - self.parts[part_to_attack].energy_consumption
        damage = self.parts[part_to_attack].attack_level
        target_robot.reduce_defense(target_part, damage)
    
    def reduce_defense(self, target_part, damage):
        self.parts[target_part].defense_level -= damage
        if self.parts[target_part].defense_level < 0:
            self.parts[target_part].defense_level = 0