#import func
from face import face
import cv2

#pose module
fc = face()

print("TEST STARTING")

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("cant open frame")
        break
    #module to be tested
    #head_pose, text  = fc.head_pose(frame)
    head_pose, text  = fc.head_pose(frame)
    print(text)
    cv2.imshow("frame", frame)
    if cv2.waitKey(10) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
   
   
''' these work with cython file ''' 
#distance to frame (cython)
#face detection (cython)
#distance to camera (cython)
#enviroment file (c++)
#camera calibration (c++)

''' these dont work please fix bugs '''
#object detection (more test neeeded)
#driver attention (java, c++, javascript)(aka sleep detection)
#head pose (python)
#body pose (pyhton)
#driver distracted (java, c++, javascript)(aka other distarctions)

''' mediapipe codebase  '''
#headpose
#bodypose

''' slow code '''
#driver attention
#driver distracted

''' completed c++ code '''
# full enviroment file code (c++)
# can complete camera calibration (c++)

#distance to frame (cython)
#face detection (cython)
#distance to camera (cython)

#head pose (python)
#body pose (pyhton)