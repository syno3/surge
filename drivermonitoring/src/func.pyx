# distutils: language = c++
# cython: language_level = 3

# -*- coding: utf-8 -*-
# cython: language_level=3
from __future__ import print_function

cimport cython
import os
import cv2
import imutils
import numpy as np
cimport numpy as np # we import cython numpy api
import mediapipe as mp
from libcpp cimport bool
from libcpp.vector cimport vector
from libc.stdio cimport printf
from libcpp.string cimport string

cdef class face:
    cdef int number_of_faces, i, count, distance
    cdef float KNOWN_DISTANCE, KNOWN_WIDTH, distracted
    cdef bint sleeping, boolean
    cdef string path
    cdef int text

    def __cinit__(self):   
        self.sleeping = False
        self.count=0
        self.text = 0
        self.boolean =False
        self.number_of_faces = 0
        self.i = 0
        self.distance = 0
        self.KNOWN_DISTANCE = 24.0
        self.KNOWN_WIDTH = 11.0
        self.distracted = False
    
    cpdef facedetect(self, frame):
        cdef float height, width
        cdef int count

        height, width, _ = frame.shape
        count = 0
        with mp.solutions.face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
            frame.flags.writeable = False
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)
            for detection in enumerate(results.detections):
                score = detection[1].score # percentage score of the model
                score = round(score[0]*100, 2) # round to two decimal places
                box = detection[1].location_data.relative_bounding_box
                x, y, w, h = int(box.xmin*width), int(box.ymin * height), int(box.width*width), int(box.height*height)
            if results != ():
                self.boolean = True
                
            count += 1  
        return self.boolean, count, score, x, w, y, h

    cpdef find_marker(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 35, 125)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key = cv2.contourArea)
        return cv2.minAreaRect(c)
    
    cpdef distance_to_camera(self, perWidth):
        perWidth = perWidth[1][0] 
        focalLength = (perWidth* self.KNOWN_DISTANCE) / self.KNOWN_WIDTH
        w = self.KNOWN_WIDTH * focalLength
        return round(w/perWidth, 2)