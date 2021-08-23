#### we perform visual odometry in python
""" 
1. Acquire input images 
2. Image correction: apply image processing, (lens distortion removal)
3. Feature extraction: define interest operators, and match feature across frame and construc optical flow filed
- use correlation to establish correspondence of two images and long term feature tracking
- feature extraction and correlation
-construct optical flow field (lucas-kanade method)
4. check flow field vector for potential tracking errors and remove outliers
5. estimate the camera motion and the optical flow
- kalman filter for state estimate distribution maintenance
-find the geometric and 3d properties of he features tha minimize the cost function based on the re-porjection error between two adjecent images 
"""

try:
    import cv2 as cv
    import numpy as np
    import logging
except Exception as e:
    logging.critical('please fix the following errors {}').format(e)

### some random variables
path = 'resources/video1.mp4'
(major_ver, minor_ver, subminor_ver) = (cv.__version__).split('.')


class opticalFlow:
    def __init__(self):
        pass

    def gray(self, frame):
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        return gray

    def denseFlow(self, first_frame, gray):

        prev_gray = cv.cvtColor(first_frame, cv.COLOR_BGR2GRAY)
        # Creates an image filled with zero intensities with the same dimensions as the frame
        mask = np.zeros_like(first_frame)
        # Sets image saturation to maximum
        mask[..., 1] = 255
        # Calculates dense optical flow by Farneback method
        flow = cv.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        # Computes the magnitude and angle of the 2D vectors
        magnitude, angle = cv.cartToPolar(flow[..., 0], flow[..., 1])
        # Sets image hue according to the optical flow direction
        mask[..., 0] = angle * 180 / np.pi / 2
        # Sets image value according to the optical flow magnitude (normalized)
        mask[..., 2] = cv.normalize(magnitude, None, 0, 255, cv.NORM_MINMAX)
        # Converts HSV to RGB (BGR) color representation
        rgb = cv.cvtColor(mask, cv.COLOR_HSV2BGR)
        rgb = cv.resize(rgb, (540, 480), interpolation = cv.INTER_AREA)

        return rgb
    def cameraMotion(self):
        pass

OF = opticalFlow()

# The video feed is read in as a VideoCapture object
cap = cv.VideoCapture(path)
# ret = a boolean return value from getting the frame, first_frame = the first frame in the entire video sequence
ret, first_frame = cap.read()

while(cap.isOpened()):
    # ret = a boolean return value from getting the frame, frame = the current frame being projected in the video
    ret, frame = cap.read()
    # Opens a new window and displays the input frame
    #cv.imshow("input", frame)
    gray = OF.gray(frame)
    #cv.imshow('gray', gray)
    rgb = OF.denseFlow(first_frame, gray) 
    cv.imshow("dense optical flow", rgb)
    # Updates previous frame
    prev_gray = gray
    # Frames are read by intervals of 1 millisecond. The programs breaks out of the while loop when the user presses the 'q' key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# The following frees up resources and closes all windows
cap.release()
cv.destroyAllWindows()