import cv2
import numpy as np

#drowsiness
from scipy.spatial import distance as dist
from imutils import face_utils
from imutils.video import VideoStream
from threading import Thread
import time
import dlib

# main face class
# we need to use numpy to optimize the code, // learn opencv optimization
class face:
    def __init__(self) ->None:

        # random variables we need
        self.front_face_harcascaade_path ="assets/front_face.xml"
        self.boolean =False

        # booleans for the methods in class
        self.eye_glasses =False
        self.distracted =False
        self.seat_belt =False
        self.drowsy =False
        self.boolean = False

        # try speed up code
        self.face_cascade = cv2.CascadeClassifier(self.front_face_harcascaade_path)

        self.number_of_faces = 0
        self.i = 0
    
    def detect_face(self, frame: np.ndarray) ->bool:

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
        # we resize image to reduce lag
        scale_percent = 60 # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resized image
        resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

        # convert to gray
        frame = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(frame, scaleFactor = 1.2, minNeighbors = 5)

        # number of faces in frame
        self.number_of_faces = len(faces)
        if self.number_of_faces < 1:
            self.boolean = False
        else:
            self.boolean = True

        return self.boolean, self.number_of_faces, faces
        
    def driver_attention(self, frame: np.ndarray) -> str:

        """ 
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        
        return
        _______

        str : 

        """
        pass

# driver drowsiness class
class drowsines:
    def __init__(self) -> None:

        self.EYE_AR_THRESH = 0.3 # threshold for eye aspect ratio
        self.EYE_AR_CONSEC_FRAMES = 48 # consecutive frames with eyes closed
        self.COUNTER = 0 # count number of frames
        self.DROWSY = False # boolean indicator

        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor() # add value

        # facial landmarks
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"] # landmarks for left eye
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"] # landmarks for right eye

        self.lStart = lStart
        self.lEnd = lEnd
        self.rStart = rStart
        self.rEnd = rEnd

    @staticmethod
    def eye_aspect_ratio(eye):
        # Vertical eye landmarks
        A = dist.euclidean(eye[1], eye[5])
        B = dist.euclidean(eye[2], eye[4])
        # Horizontal eye landmarks 
        C = dist.euclidean(eye[0], eye[3])

        # The EAR Equation 
        EAR = (A + B) / (2.0 * C)
        return EAR

    @staticmethod
    def mouth_aspect_ratio(mouth):

        A = dist.euclidean(mouth[13], mouth[19])
        B = dist.euclidean(mouth[14], mouth[18])
        C = dist.euclidean(mouth[15], mouth[17])

        MAR = (A + B + C) / 3.0
        return MAR

    def detect_drowsiness(self, frames:np.ndarray):

        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        rects = self.detector(gray, 0)

        for rect in rects:
            shape = self.predictor(gray, rect)
            shape = face_utils.shape_to_np(shape)

            leftEye = shape[self.lStart:self.lEnd]
            rightEye = shape[self.rStart:self.rEnd]
            leftEAR = self.eye_aspect_ratio(leftEye)
            rightEAR = self.eye_aspect_ratio(rightEye)

            ear = (leftEAR + rightEAR) / 2.0

            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)

            if ear < self.EYE_AR_THRESH:
                self.COUNTER += 1
                if self.COUNTER >= self.EYE_AR_CONSEC_FRAMES:
                    self.DROWSY = True

        return self.DROWSY, leftEyeHull, rightEyeHull
