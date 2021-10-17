# we add 1.monocular depth, we detect faces with mediapipe + count faces
import cv2
import imutils
import numpy as np

# face detection module
import mediapipe as mp # we will do face detection

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

    def driver_attention(self, frame: np.ndarray) -> str:
        pass

if __name__ == "__main__":
    pass