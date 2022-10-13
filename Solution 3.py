#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 15:59:37 2022

@author: qinohr
"""

import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt

TRIALS = 1000
VELOCITY = 10 #m/s

def boundary_conditon_3(x,y):
    boolean = False
    if ((x-2.5)/30)**2+((y-2.5)/40)**2 >= 1:
        boolean = True
    return boolean

def random_walk_3():
    
    pos = [0,0]
    food_reached = False
    counter = 0
    while food_reached == False:
        direction = rnd.randint(0,4,1)
        if direction == 0:
            pos[0] = pos[0]+10
            counter = counter + 1
            condition = boundary_conditon_3(pos[0],pos[1])
            if condition == True:
                food_reached = True
        elif direction == 1:
            pos[0] = pos[0]-10
            counter = counter + 1
            condition = boundary_conditon_3(pos[0],pos[1])
            if condition == True:
                food_reached = True  
        elif direction == 2:
            pos[1] = pos[1]+10
            counter = counter + 1
            condition = boundary_conditon_3(pos[0],pos[1])
            if condition == True:
                food_reached = True
        elif direction == 3:
            pos[1] = pos[1]-10
            counter = counter + 1
            condition = boundary_conditon_3(pos[0],pos[1])
            if condition == True:
                food_reached = True
    return counter

def _main3_():
    times = []
    for iteration in range(TRIALS):
        experiment = random_walk_3()
        times = np.append(times, experiment)
    average = np.mean(times)
    standard_deviation = np.std(times)/np.sqrt(TRIALS)
    return average, standard_deviation

result, uncertainty = _main3_()
print(round(result), "+/-", uncertainty)