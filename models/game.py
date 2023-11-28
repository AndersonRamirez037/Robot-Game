from models.robot import Robot
from models.logic.messages import *
from models.logic.template.robot_template import colors

class Game():
    def __init__(self):
        print("Available colors: ")
        self.color_menu(colors)
        self.robot1 = Robot(input(FIRST_ROBOT_NAME), color_code=input(COLOR_CODE).title())
        self.robot2 = Robot(input(SECOND_ROBOT_NAME), color_code=input(COLOR_CODE).title())
        print(f"\n\t{self.robot1.name} Vs. {self.robot2.name}\n")

    def color_menu(self, dict):
        for index, key in enumerate(dict):
            print(f"{index}: {key}")
        print()
    
    def play(self):  
        final_text_color = "White"      
        game_over = False 
        while not game_over:
            robot_list = [self.robot1, self.robot2]
            for current_robot in robot_list:  
                print(f"\n{colors[current_robot.color_code]}------- It's {current_robot.name}'s turn -------")
                print(f"{TOTAL_ENERGY}{current_robot.energy}")
                current_robot.attack(robot_list)                
                if current_robot.energy > 0:
                    print(f"{ENERGY_REDUCE}{current_robot.energy}%\n")
                else:
                    winner = [robot for robot in robot_list if robot != current_robot][0]
                    print(f"{colors[final_text_color]}\nYou are dead! The Robot {winner.name} is the winner!!")
                    game_over = True 
                    break