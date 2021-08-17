#### we build the kalman filter

from typing import ClassVar


try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import logging
except Exception as e:
    logging.error('please fix error {}').format(e)
    
class KalmanFilter:
    def __init__(self, initial_x: float, initial_y: float, a: float):
        # mean of state GRV
        self.x = np.array([initial_x, initial_y])
        self.accel_variance = a
        # covariance of state GRV
        self.p = np.eye(2) 
    @property  
    def __float__(self):
        """ 
        return
        ______
        
        self.x[0] = x
        self.y[1] = y
        """
        return self.x[0], self.x[1]
    def predict(self, dt: float):
        # F = [
        #    [1, dt],
        #    [0, 1]
        #]
        # G = [0.5*dt**2, dt]
        # X = F X
        # P = F P FT + G GT a
        F = np.array([
            [1, dt],
            [0, 1]
        ])
        G = np.array([0.5*dt**2, dt]).reshape(2,1)
        new_x = F.dot(self.x)
        new_p = F.dot(self.p).dot(F.T) + G.dot(G.T) * self.accel_variance
        
        self.p = new_p
        self.x = new_x
    @property
    def mean_cov(self):
        return self.p, self.x
    def update(self, meas_value: float, meas_variance: float):
        # Y = Z - H X
        # S = H P HT + R
        # K = P HT S^-1
        # X = X + K Y
        # P = (I - K H) + P
        
        Z = np.array([meas_value])
        R = np.array([meas_variance])
        H = np.array([1, 0]).reshape(1, 2)
        
        Y = Z - H.dot(self.x)
        S = H.dot(self.p).dot(H.T) + R
        
        K = self.p.dot(H.T).dot(np.linalg.inv(S))
        
        new_x = self.x + K.dot(Y)
        new_p = (np.eye(2), - K.dot(H)).dot(self.p)
        
        self.p = new_p
        self.x = new_x
        
KF = KalmanFilter(initial_x=0.2, initial_y=0.5, a=0.0)
DT = 0.1    
NUM_STEPS = 1000

MEANS = []
COVS = []

for i in range (NUM_STEPS):
    COVS.append(KF.mean_cov[0])
    MEANS.append(KF.mean_cov[1])
    
    
    KF.predict(dt=DT)

plt.ion()
plt.figure

plt.subplot(2, 1, 1)
plt.title('position')
plt.plot([mu[0] for mu in MEANS], 'r--')

plt.subplot(2, 1, 2)
plt.title('Velocity')
plt.plot([mu[1] for mu in MEANS])

plt.show()
plt.ginput(1)

