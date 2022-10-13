import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt


TRIALS = 1000
VELOCITY = 10 #m/s

def random_walk():
    
    pos = [0,0]
    food_reached = False
    counter = 0
    while food_reached == False:
        direction = rnd.randint(4)
        if direction == 0:
            pos[0] = pos[0]+10
            counter = counter + 1
            if np.sqrt(pos[0]**2) == 20 or np.sqrt(pos[1]**2) == 20:
                food_reached = True
             
        elif direction == 1:
            pos[0] = pos[0]-10
            counter = counter + 1
            if np.sqrt(pos[0]**2) == 20 or np.sqrt(pos[1]**2) == 20:
                food_reached = True
              
        elif direction == 2:
            pos[1] = pos[1]+10
            counter = counter + 1
            if np.sqrt(pos[0]**2) == 20 or np.sqrt(pos[1]**2) == 20:
                food_reached = True
                
        elif direction == 3:
            pos[1] = pos[1]-10
            counter = counter + 1
            if np.sqrt(pos[0]**2) == 20 or np.sqrt(pos[1]**2) == 20:
                food_reached = True
    return counter
            
        
def _main_():
    times = []
    for iteration in range(TRIALS):
        experiment = random_walk()
        times = np.append(times, experiment)
    average = np.mean(times)
    standard_deviation = np.std(times)/np.sqrt(TRIALS)
    return average, standard_deviation
         

         
result, uncertainty = _main_()
print(round(result), "+/-", uncertainty)
#------------------------------------     



