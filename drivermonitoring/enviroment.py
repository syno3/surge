# we detect resolution, brightness, saturation

import cv2
from logging import error
import math
import time
import numpy as np

# main class
class enviroment:
    def __init__(self) -> None:
        
        # exposure values
        self._no_exposure = 0
        self._little_exposure = 65
        self._slight_exposure = 130
        self._normal_exposure = 194
        self._over_exposure = 255

        # saturation values
        self._no_saturation = 0
        self._little_saturation = 65
        self._slight_saturation = 130
        self._normal_saturation = 194
        self._over_saturation = 255

        #frames per second values
        self.prev_frame_time = 0
        self.new_frame_time = 0


    def brightness_level(self, frame: np.ndarray) -> str:

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        we take frame and convert to HSV color space. We get the last V value and calculate the mean of the value.

        using the mean we determine the level of brightness : 1. no brightness, 2. little brightness 3. Normal brightness 4. Over brightness
        
        return
        _______

        str : the output string of the levels of brightness

        """
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        value = hsv[...,2].mean()
        response = []

        if value == self._no_exposure:
            response.append('No exposure')
    
        if value > self._no_exposure and value <self._little_exposure:
            response.append('Minimal exposure')

        if value > self._little_exposure  and value < self._slight_exposure:
            response.append('slight exposure')

        if value > self._slight_exposure  and value < self._normal_exposure:
            response.append('Normal exposure')

        if value > self._normal_exposure  and value < self._over_exposure:
            response.append('over exposure')

        return response[0]

    def saturation_level(self, frame: np.ndarray) ->str:

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        we take frame and convert to HSV color space. We get the last S value and calculate the mean of the value.

        using the mean we determine the level of brightness : 1. no staturation, 2. little staturation 3. Normal staturation 4. Over staturation
        
        return
        _______

        str : the output string of the levels of saturation

        """
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        value = hsv[...,1].mean()
        response = []

        if value == self._no_saturation:
            response.append('No saturation')
    
        if value > self._no_saturation and value <self._little_saturation:
            response.append('Minimal saturation')

        if value > self._little_saturation  and value < self._slight_saturation:
            response.append('slight saturation')

        if value > self._slight_saturation  and value < self._normal_saturation:
            response.append('Normal saturation')

        if value > self._normal_saturation  and value < self._over_saturation:
            response.append('over saturation')

        return response[0]

    def frames_per_second(self) ->int:

        """ 
        parameters
        _________

        None

        function
        ________

        we determine the number of frames per second of the frames

        
        return
        _______

        int : the number of frames per second

        """
        self.new_frame_time = time.time()

        fps = 1/(self.new_frame_time-self.prev_frame_time)

        self.prev_frame_time = self.new_frame_time

        fps = int(fps)

        return fps

if __name__ == "__main__":
    run = enviroment()