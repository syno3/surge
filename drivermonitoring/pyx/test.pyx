#distutils: language = c++
# cython: language_level = 3

import cython
import cv2
from libcpp.vector cimport vector

cdef class test:
    cpdef hello(self, frame):
        hsv  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        value = hsv[...,1].mean()
        response = []
        if value > 0:
            response.append("no saturation")
            print(response[0])

cdef class say:
    cpdef smth(self):
        print('hello there')