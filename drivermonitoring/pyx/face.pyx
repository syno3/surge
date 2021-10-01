# distutils: language = c
# cython: language_level = 3

# we require ubuntu !!!!!
import cv2
import numpy as np
import os
import cython
import threaded

# we optimize the code
import cython
from libcpp cimport bool

# global variables


# main face class
# we need to use numpy to optimize the code, // learn opencv optimization

cdef class face:
    # cython variables
    cdef int i
    cdef int number_of_faces
    cdef char* front_face_harcascaade_path
    cdef bool eye_glasses, distracted, seat_belt, drowsy, boolean

    def __init__(self) ->None:

        # random variables we need
        self.front_face_harcascaade_path ="assets/front_face.xml"
        self.boolean =False

        # booleans for the methods in class
        self.eye_glasses =False
        self.distracted =False
        self.seat_belt =False
        self.drowsy =False

        # try speed up code
        self.face_cascade = cv2.CascadeClassifier(self.front_face_harcascaade_path)

        self.number_of_faces = 0
        self.i = 0

    # we detect frontal face consider cvlibs
    
    cpdef int detect_face(self, list frame):

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        we use harcaascade to detect face and the count the number of detected faces

        we use dlib.get_frontal_face_detector() to determine the coordiantes of faces in frames and count the number of coordinates.
        
        return
        _______

        Bool : boolean of wether True incase face detected or false

        """
        # initilize variables
        cdef int scale_percent, width, height
        cdef tuple dim
        cdef list faces

        # we resize image to reduce lag
        scale_percent = 60 # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resized image
        resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

        # convert to gray
        frame = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(frame, 1.1, 4)

        if faces != []:
            self.boolean = True


        return 0
        
    cdef int driver_attention(self, list frame):

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        
        return
        _______

        int : number of detected faces in the image

        """
        return 0
