# distutils: language = c++
# cython: language_level = 3

# -*- coding: utf-8 -*-
# cython: language_level=3
from __future__ import print_function

cimport cython
import cv2
import time
import numpy as np
cimport numpy as np

np.import_array()
DTYPE = np.int
ctypedef np.int_t DTYPE_t

# main class
# we need to use numpy to optimize the code, // learn opencv optimization
cdef class enviroment:
    cdef int _no_exposure, _little_exposure, _slight_exposure, _normal_exposure, _over_exposure
    cdef int _no_saturation, _little_saturation, _slight_saturation, _normal_saturation, _over_saturation
    cdef np.ndarray frame

    print('\033[95m'"enviroment class imported"'\033[0m')

    def __cinit__(self):    
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
        #self.prev_frame_time = 0.0
        #self.new_frame_time = 0.0

    cdef inline (char*, int) brightness_level(self, np.ndarray frame):

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
        # we define the return types

        cdef np.ndarray hsv  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cdef float value = hsv[...,1].mean()
        cdef list response = []

        if value == self._no_exposure:
            response.append("no saturation")
    
        if value > self._no_exposure and value <self._little_exposure:
            response.append('Minimal exposure')

        if value > self._little_exposure  and value < self._slight_exposure:
            response.append('slight exposure')

        if value > self._slight_exposure  and value < self._normal_exposure:
            response.append('Normal exposure')

        if value > self._normal_exposure  and value < self._over_exposure:
            response.append('over exposure')

        return response[0]

    cdef inline (char*, float) saturation_level(self, np.ndarray frame):

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
        # we define the data types

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cdef float value = hsv[...,1].mean()
        cdef list response = []

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

        return response[0], value

    @cython.cdivision(True)
    cdef inline float frames_per_second(self):

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
        ## type declarations
        cdef double fps
        cdef double new_frame_time = 0.0, prev_frame_time = 0.0

        new_frame_time = time.time()

        fps = 1.0/(new_frame_time-prev_frame_time)

        prev_frame_time = new_frame_time

        return fps
