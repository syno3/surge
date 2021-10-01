# distutils: language = c
# cython: language_level = 3

# we require ubuntu
import cv2
import time
import numpy as np
import cython

# we optimize the code
import cython
from libcpp cimport bool


# main class
# we need to use numpy to optimize the code, // learn opencv optimization
cdef class enviroment:
    # cython variables
    cdef int _no_exposure, _little_exposure, _slight_exposure, _normal_exposure, _over_exposure, _no_saturation, _little_saturation, _slight_saturation, _normal_saturation, _over_saturation
    cdef float prev_frame_time, new_frame_time

    def __init__(self):
        
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
        self.prev_frame_time = 0.0
        self.new_frame_time = 0.0


    cdef char* brightness_level(self, list frame):

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
        # initilize variables

        cdef float value
        cdef list hsv, response 
        cdef char* out

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

        out = response[0]

        return out

    cdef char* saturation_level(self, list frame):

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
        # we declare variables
        cdef double value
        cdef list response 
        cdef char* out

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

        out = response[0]

        return out

    cdef double frames_per_second(self):

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
        # initilize variables
        cdef double fps

        self.new_frame_time = time.time()

        fps = 1/(self.new_frame_time-self.prev_frame_time)

        self.prev_frame_time = self.new_frame_time


        return fps