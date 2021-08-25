""" 
1. Compute camera calibration matrix and distortion effects
2. Apply a distortion correction to raw images
3. Use color transformatio, gradient to create a threshold binary image
4. Apply a perspective transform to generate a 'bird's eye view'
5. Detect lane pixels and fit to find the lane boundary
6. Determine the curvature of the lane and the vehicle position with repect to another
7. wrap the detected lane boundaries back onto the original image and display numerical estimation of the lane curvature
8. Use the numerical estimate to calculate the steering angle

"""

##### we work on an advanced lane detection algorithim

try:
    import numpy as np
    import logging
    import cv2
    import time
    import glob
    from camera import *

except Exception as e:
    logging.error('please fix the following errors {}').format(e)

##### we create the lanedetection class
class LaneDetection:
    def __init__(self, path):
        self.path = str(path)

    @property  
    def __str__(self):
        return self.path



#### we initialize lanedetection class
LaneDetection = LaneDetection('resources/video1.mp4')

def main():
    #### we add random variables here
    video_path = LaneDetection.path
    cap = cv2.VideoCapture(video_path)

    prev_frame = 0
    new_frame = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    #### we use opencv to display video
    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame, (780, 520), interpolation=cv2.INTER_AREA)
        new_frame = time.time()

        fps = 1/(new_frame - prev_frame)
        prev_frame = new_frame

        fps = int(fps)
        cv2.putText(frame,
        'Frames Per Second : {}'.format(fps),
        (50, 50),
        font,1,
        (0,255,255),
        2, cv2.LINE_4)

        cv2.imshow('lane_detected',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    #main()