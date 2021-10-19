# we add 1.monocular depth, we detect faces with mediapipe + count faces
import os
import cv2
import imutils
import numpy as np

# face detection module
import mediapipe as mp # we will do face detection

# for sleep prediction
from keras.models import load_model

# main face class
# we need to use numpy to optimize the code, // learn opencv optimization
class face:
    def __init__(self) ->None:

        # cascade files
        self.front_face_harcascaade_path = cv2.CascadeClassifier("assets/front_face.xml")
        self.eye_cascade = cv2.CascadeClassifier("assets/eye.xml")
        self.left_eye = cv2.CascadeClassifier("assets/left_eye.xml")
        self.right_eye = cv2.CascadeClassifier("assets/right_eye.xml")
        
        
        self.model =  load_model("assets/models/eyeStateModel1.h5")
        self.sleeping = False
        self.count=0
        self.path = os.getcwd()
        
        # globals for face
        self.boolean =False
        
        # debugging global variables
        self.number_of_faces = 0 # number of faces in the video
        self.i = 0
        self.distance = 0 # distance of face from camera
        
        # mediapipe submodules
        self.mp_face_detection = mp.solutions.face_detection
        self.mp_drawing = mp.solutions.drawing_utils
        
        # global for depth
        self.KNOWN_DISTANCE = 24.0
        self.KNOWN_WIDTH = 11.0
    
    
    # we use media pipe for face detection and number of faces
    def facedetect(self, frame: np.ndarray):
        height, width, _ = frame.shape
        count = 0
        with self.mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
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

    @staticmethod
    def find_marker(frame: np.ndarray):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 35, 125)

        # find the contours in the edged image and keep the largest one;
        # we'll assume that this is our piece of paper in the image
        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key = cv2.contourArea)

        # compute the bounding box of the of the paper region and return it
        return cv2.minAreaRect(c)
    
    # we need to accurately compute focal lenght for this
    def distance_to_camera(self, perWidth):
        perWidth = perWidth[1][0] 
    	# compute and return the distance from the maker to the camera
        focalLength = (perWidth* self.KNOWN_DISTANCE) / self.KNOWN_WIDTH
        w = self.KNOWN_WIDTH * focalLength
        
        return round(w/perWidth, 2)
    
    # we need to fix speed
    def driver_attention(self, frame: np.ndarray) -> bool:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = self.eye_cascade.detectMultiScale(gray, 1.1, 4)
        
        for (x,y,w,h) in eyes:
            eyes=frame[y:y+h,x:x+w]
            self.count=+1
            eyes = cv2.resize(eyes, (32, 32))
            eyes = np.array(eyes)
            eyes = np.expand_dims(eyes, axis=0)
            ypred = self.model.predict(eyes)
            
            prediction = np.argmax(ypred[0], axis=0)
            
            if prediction == 1:
                self.sleeping = False
            else:
                self.sleeping = True
                
        return self.sleeping
    
    # we detect driver attention status
    def driver_distracted(self, frame:np.ndarray) ->bool:
        pass
        
                



        

if __name__ == "__main__":
    pass