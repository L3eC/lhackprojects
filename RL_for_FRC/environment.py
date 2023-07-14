from typing import Tuple
from math import copysign
import numpy as np

class Environment():
    def __init__(self):
        # all units are feet
        self.robot_x = 0 # viewed from the red alliance area, so positive y is away from the drivers
        self.robot_y = 0
        self.exited_comm = False
        self.docked = False
        self.elapsed_time = 0 # in seconds
        self.score = 0
    
    def reset(self):
        self.__init__()
        print("** RESET **")
        return np.array([self.robot_x, self.robot_y, self.elapsed_time])

    def step(self, action: Tuple[float, float]):
        print("action: ", action)
        # Cap robot x and y at +- 1
        self.robot_x += copysign(1, action[0])/50 if action[0] > 1 else action[0]/50
        self.robot_y += copysign(1, action[1])/50 if action[1] > 1 else action[1]/50

        # Attempt at displaying robot position on field, kinda works
        display = [['-']*10]*10

        if 0 <= self.robot_x <= 9: 
            index_x = int(self.robot_x)
        else: index_x = 9

        if 0 <= self.robot_y <= 9: 
            index_y = 9 - int(self.robot_y)
        else: index_y = 0

        display[index_x][index_y] = '⬛' # it's not an ascii character I know

        print(f"Robot x: {self.robot_x} Robot y: {self.robot_y}")

        for row in display: print(' '.join(row) + '\n')

        # If you exit a certain area called a community, you're awarded 3 points.
        if (self.robot_y > 16.104 or (self.robot_x > 4.5 and self.robot_y > 11.031)) and self.exited_comm == False:
            print("** Exited community! **")
            self.score += 3
            self.exited_comm = True # You only get awarded points once

        # If you go onto a certain platform, you earn 10 points
        if 6 < self.robot_y < 12 and 3 < self.robot_x < 6 and self.docked == False:
            print("** Docked! **")
            self.score += 10
            self.docked = False

        self.elapsed_time += 1/50 # Robot processor updates 50 times per second

        print(f"Score: {self.score}")

        return (np.array([self.robot_x, self.robot_y, self.elapsed_time]),
                self.score,
                self.get_finished())

    def get_finished(self) -> bool:
            # Autonomous period ends after 15 seconds
            return True if self.elapsed_time > 15 else False

if False: # testing
    myEnv = Environment()
    for i in range(1000):
        print(f"Score: {myEnv.score} robot_x: {myEnv.robot_x} robot_y: {myEnv.robot_y}")
        myEnv.step((0.001, 1))