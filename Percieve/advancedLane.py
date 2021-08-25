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

from cv2 import calibrateCamera


try:
    import numpy as np
    import logging
    import cv2
    import time
    import glob
except Exception as e:
    logging.error('please fix the following errors {}').format(e)

#### we create the camera calibration class

class CameraCalibration:
    def __init__(self):
        # array to store objects points and image points from all the images.
        self.objpoints = [] #3d points in real world
        self.imgpoints = [] #2d points to image plane
        self.images = glob.glob('*.jpg') # images ending with jpg

    @property
    def __len__(self):
        return len(self.images)

    @property
    def points(self):
        return self.objpoints, self.imgpoints

    def critertia(self):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        return criteria
    
    def objectPoints(self):
        objp = np.zeros((6*7, 3), np.float32)
        objp[:, :2] = np.mgrid[0:7, 0:6].T.reshape(-1, 2)
        return objp

    @property
    def calculation(self):
        for fname in self.images:
            img = cv2.imread(fname)
            gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            objp = self.objectPoints
            criteria = self.critertia
            
            ## find the chess board corners
            ret, corners = cv2.findChessboardCorners(gray, (7, 6), None)

            ### if found add object points, image points
            if ret == True:
                self.objpoints.append(objp)

                corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                self.imgpoints.append(corners)

        return gray

    def calibration(self):
        gray = self.calculation
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(self.objpoints, self.imgpoints, gray.shape[::-1], None, None)

        return ret, mtx, dist, rvecs, tvecs
        
    def undistort(self, frame):
        h, w = frame.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
        dst = cv2.undistort(frame, mtx, dist, None, newcameramtx)

        ###crop image
        x, y, w, h = roi
        dst = dst[y:y+h, x:x+w]
        return dist


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
    camera = CameraCalibration()
    ret, mtx, dist, rvecs, tvecs = camera.calibration
    print(ret, mtx)