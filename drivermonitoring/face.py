# we add 1.monocular depth, we detect faces with mediapipe + count faces
# we perform object detection
# we look for distarcted driving

import os
import cv2
import imutils
import numpy as np
import pandas as pd

# face detection module
import mediapipe as mp # we will do face detection

# for sleep prediction
from keras.models import load_model
import tensorflow as tf
import tensorflow_hub as hub
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
        
        # mediapipe pose submodules
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
        self.mpDraw = mp.solutions.drawing_utils
        
        # global for depth
        self.KNOWN_DISTANCE = 24.0
        self.KNOWN_WIDTH = 11.0
        
        # head pose detection
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.distracted = False
        self.text = None
        
        #object detection
        #self.detector = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")
        #self.labels = pd.read_csv('labels.csv',sep=';',index_col='ID')
        #self.labels = self.labels['OBJECT (2017 REL.)']
        
        
        
        
        
        
        
        
        
        
    
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
    
    # we need to fix speed // not working properly // we move to cnn 
    def driver_attention(self, frame: np.ndarray) -> bool:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        eyes = self.eye_cascade.detectMultiScale(gray, 1.1, 4) # look for faster option (slowing down code)
        
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
    
    
    # we perform object detection
    def objects(self, frame:np.ndarray) ->bool:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_tensor = tf.convert_to_tensor(frame, dtype=tf.uint8)
        rgb_tensor = tf.expand_dims(rgb_tensor , 0)
        boxes, scores, classes, _ = self.detector(rgb_tensor)
        pred_labels = classes.numpy().astype('int')[0]
        pred_labels = [self.labels[i] for i in pred_labels]
        pred_boxes = boxes.numpy()[0].astype('int')
        pred_scores = scores.numpy()[0]
        
        #loop throughout the detections and place a box around it  
        for score, (ymin,xmin,ymax,xmax), label in zip(pred_scores, pred_boxes, pred_labels):
            if score < 0.5:
                continue
            
            
            score = 100 * round(score,0)
            
            
        return score, ymin, xmin, ymax, xmax, pred_labels
    
    
    # we perform head pose detection
    def head_pose(self, frame:np.ndarray) -> str:
        frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
        frame.flags.writeable = False
        results = self.face_mesh.process(frame)
        frame.flags.writeable = True
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        img_h, img_w, img_c = frame.shape
        face_3d = []
        face_2d = []

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for idx, lm in enumerate(face_landmarks.landmark):
                    if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                        if idx == 1:
                            _ = (lm.x * img_w, lm.y * img_h)
                            _ = (lm.x * img_w, lm.y * img_h, lm.z * 8000)

                        x, y = int(lm.x * img_w), int(lm.y * img_h)

                        # Get the 2D Coordinates
                        face_2d.append([x, y])

                        # Get the 3D Coordinates
                        face_3d.append([x, y, lm.z])       

            # Convert it to the NumPy array
            face_2d = np.array(face_2d, dtype=np.float64)

            # Convert it to the NumPy array
            face_3d = np.array(face_3d, dtype=np.float64)
            # The camera matrix
            focal_length = 1 * img_w

            cam_matrix = np.array([ [focal_length, 0, img_h / 2],
                                    [0, focal_length, img_w / 2],
                                    [0, 0, 1]])

            # The Distance Matrix
            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            # Solve PnP
            _, rot_vec, _ = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

            # Get rotational matrix
            rmat, _ = cv2.Rodrigues(rot_vec)

            # Get angles
            angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)

            # Get the y rotation degree
            x = angles[0] * 360
            y = angles[1] * 360
            
            if y < -10:
                self.text = "Left"
                self.distracted = True
            elif y > 10:
                self.text = "Right"
                self.distracted = True
            elif x < -10:
                self.text = "Down"
                self.distracted = True
            else:
                self.text = "Forward"
                self.distracted = False

        return self.distracted, self.text
    
    # we detect for proper pose in driving (aka both hands at steering wheel)
    def body_pose(self, frame:np.ndarray):
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)
        if results.pose_landmarks:
            #self.mpDraw.draw_landmarks(frame, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
            for _, lm in enumerate(results.pose_landmarks.landmark):
                h, w,_ = frame.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                
        return cx, cy
    
    
    # we will add face 3d landmark tracking (aka face 3d control)
        























        

if __name__ == "__main__":
    pass