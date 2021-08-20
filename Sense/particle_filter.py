#### we build a particle filter python
from math import cos, exp, pi, sin, sqrt

from numpy.random.mtrand import rand


try:
    import numpy as np
    import random
    import logging
    import math
except Exception as e:
    logging.error('please fix the error {}').format(e)
    
#### we initialize some global variables
landmarks = np.array([[20.0, 20.0], [80.0, 80.0], [20.0, 80.0], [80.0, 20.0]])
world_size = float(100)


class Robot:
    def __init__(self):
        self._x = random.random() * world_size ### we initialize with random value and multiply with 100
        self._y = random.random() * world_size
        self._orientation = int(random.random() * 2.0 * pi) ## we initalize the original orientation of the vehicle
        
        self.foward_noise = 0.0
        self.turn_noise = 0.0
        self.sense_noise = 0.0
        
    def set(self, new_x: float, new_y: float, new_orientation: int):
        """ 
        we check if the values given are valid and the store the data in the initialized value
        
        """
        if new_x < 0 or new_x >= world_size:
            logging.critical('X coordinate is out of bound') 
    
        if new_x < 0 or new_x >= world_size:
            logging.critical('X coordinate is out of bound') 
            
        if new_orientation < 0 or new_orientation >= 2 * pi:
            logging.critical('orientation must be in [0...2pi]')
            
        else:
            self._x = float(new_x)
            self._y = float(new_y)
            
            
    def set_noise(self, new_f_noise : float, new_t_noise : float, new_s_noise : float):
        """ 
        parameter
        _________
        
        
        new_f_noise - foward_noise
        new_t_noise - turn_noise
        new_s_noise - sense_noise
        
        return
        ______
        
        None
        
        
        we add noise to the parameter and update the initialized noise
        
        """
        self.foward_noise = float(new_f_noise)
        self.turn_noise = float(new_t_noise)
        self.sense_noise = float(new_s_noise)
        
        
    def sense(self):
        """ 
        parameter
        _________
        
        None
        
        return
        ______
        
        Z - list containing the distance calculated between the landmarks and the robot
        
        
        create an empty list, iterate over the number of times the values are in the landmarks list
        calculate the distance ((x - XR)^2 + (y - YR)^2)^2
        add the value stored to gaussian value from random.gauss
        return numpy array
        
        """
        
        z = []
        for i in range(len(landmarks)):
            dist = sqrt((self._x - landmarks[i][0]) ** 2 + (self._y - landmarks[i][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            z.append(dist)
            
        return np.array(z)
    def Gaussian(self, mu, sigma, x):
        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))
    
    def measurement_prob(self, measurement):
        # calculates how likely a measurement should be
        prob = 1.0
        for i in range(len(landmarks)):
            dist = sqrt((self._x - landmarks[i][0]) ** 2 + (self._y - landmarks[i][1]) ** 2)
            prob *= self.Gaussian(dist, self.sense_noise, measurement[i])
        return prob
    
    def move(self, turn: float , foward: float):
        if foward < 0:
            logging.critical('Foward value is incorrent, cannot move backwards')
        ### turning produces the orientation, we add randomness
        orientation = float(turn) + self._orientation + random.gauss(0.0, self.turn_noise)
        orientation %= 2 * pi 
        
        ### move and add randomness to the motion command
        dist = float(foward) + random.gauss(0.0, self.foward_noise)
        x = self._x + (cos(orientation) * dist)
        y = self._y + (sin(orientation) * dist)
        
        x %= world_size
        y %= world_size
        
        #### set the particle filter
        
        robot = Robot()
        robot.set(x, y, orientation)
        robot.set_noise(self.foward_noise, self.turn_noise, self.sense_noise)
        
        return robot
        
        
        
                
            
res = Robot()
res = res.move(0.2, 5.0)
sense = res.sense()

#### we generate randome particles

N = 1000
p = []

for _ in range(N):
    x = Robot()
    x.set_noise(0.05, 0.05, 5.0)  # add noise
    p.append(x)

w = []

for rob in p:
    prob = rob.measurement_prob(sense)  # Z remains the same
    w.append(prob)
    
print(np.array(w))