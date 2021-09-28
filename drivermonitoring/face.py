# we detect face, number of faces, eye glasses, drowsiness, distarcted, holding phone, smoking, yawning

# we import needed variables
import cv2
import numpy as np
import os


# global variables


# main face class

class face:
    def __init__(self) -> None:

        self.front_face_harcascaade_path = 'assets/front_face.xml'
        self.bool = False

    # we detect 
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
        pass

    def detected_eye_glasses(self, frame: np.ndarray) -> bool:
        pass
    