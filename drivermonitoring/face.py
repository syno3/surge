# we detect face, number of faces, eye glasses, drowsiness, distarcted, holding phone, smoking, yawning

# we import needed variables
import cv2
import numpy as np
import os
import dlib
import thread


# global variables


# main face class

class face:
    def __init__(self) -> None:

        self.front_face_harcascaade_path = 'assets/front_face.xml'
        self.bool = False
        self.i = 0

    # we detect frontal face consider cvlibs
    def detect_face(self, frame: np.ndarray) -> bool:

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        we use harcaascade to detect face
        
        return
        _______

        Bool : boolean of wether True incase face detected or false

        """
        face_cascade = cv2.CascadeClassifier(self.front_face_harcascaade_path)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(frame, 1.1, 4)

        if faces != []:
            self.bool = True

        return self.bool

    def number_detected_faces(self, frame: np.ndarray) -> int:

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        we use dlib.get_frontal_face_detector() to determine the coordiantes of faces in frames and count the number of coordinates.
        
        return
        _______

        int : number of detected faces in the image

        """
        detector = dlib.get_frontal_face_detector()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        for _ in faces:
            i = i+1

        return i

    def detected_eye_glasses(self, frame: np.ndarray) -> bool:

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        we use dlib.get_frontal_face_detector() to determine the coordiantes of faces in frames and count the number of coordinates.
        
        return
        _______

        int : number of detected faces in the image

        """
        pass

    def driver_attention(self, frame: np.ndarray) ->str:
        pass

    def wearing_seatbelt(self, frame: np.ndarray) ->str:
        pass

    def illegal_substances(self, frame: np.ndarray) ->str:
        pass