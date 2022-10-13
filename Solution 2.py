#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 15:29:43 2022

Question 2:
Solution: The time is infinity as the ant is not (closed off)
@author: qinohr
"""

import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt

TRIALS = 15
VELOCITY = 10 #m/s

def boundary_condition_2(move):
    boolean = False
    if move[1]+move[0] >= 10:
        boolean = True
    return boolean

def random_walk_2():
    
    pos = [0,0]
    food_reached = False
    counter = 0
    while food_reached == False:
        direction = rnd.randint(0,4,1)
        if direction == 0:
            pos[0] = pos[0]+10
            counter = counter + 1
            condition = boundary_condition_2(pos)
            if condition == True:
                food_reached = True
        elif direction == 1:
            pos[0] = pos[0]-10
            counter = counter + 1
            condition = boundary_condition_2(pos)
            if condition == True:
                food_reached = True  
        elif direction == 2:
            pos[1] = pos[1]+10
            counter = counter + 1
            condition = boundary_condition_2(pos)
            if condition == True:
                food_reached = True
        elif direction == 3:
            pos[1] = pos[1]-10
            counter = counter + 1
            condition = boundary_condition_2(pos)
            if condition == True:
                food_reached = True
    return counter
            
def _main2_():
    times = []
    for iteration in range(TRIALS):
        experiment = random_walk_2()
        times = np.append(times, experiment)
    average = np.mean(times)
    standard_deviation = np.std(times)/np.sqrt(TRIALS)
    return average, standard_deviation

result, uncertainty = _main2_()
print(round(result), "+/-", uncertainty)
#--------------------------
