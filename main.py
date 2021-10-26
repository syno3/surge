### the main entry file
# - we perform collison detection and avoidance
# - we perform lane detection(CNN)
# - we perform object detection
# - we perform segementation
# - we perform traffic sign detection
# - we perform object tracking

import os
import sys
import cv2
import numpy as np

# file imports
from Percieve.collision import collision # we do collison detection



class output:
    def __init__(self) -> None:
        pass
    
    def debug(self):
        pass
    
    
if __name__ == "__main__":
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable() 
      
    run = output()
    run.debug() # we run the actual video when the file is called
    
    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.dump_stats(filename='stats/self_driving_stats.prof') # we dump the debug file