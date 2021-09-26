# we do advanced lane detection udacity project based on this (
# https://towardsdatascience.com/advanced-lane-detection-for-autonomous-vehicles-using-computer-vision-techniques
# -f229e4245e41) (https://github.com/uppala75/CarND-Advanced-Lane-Lines/blob/master/AdvancedLaneLines.md)


# improvements: 1. add timeit 2. add loading animation for corners found 3. write tests for the class 4.add progress bar


try:
    import numpy as np
    import cv2
    import pickle
    import glob
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import matplotlib.gridspec as gridspec
    from logging import error
    from cameracalibration import CameraCalibration
    from preprocessimages import PreprocessImage
    from tracker import tracker

except Exception as e:
    error(e)

class LaneDetect:

    def __init__(self):
        self.bot_width = .76 # percentage of bottom trapezoidal height
        self.mid_width = .08 # percentage of mid trapezoidal height
        self.height_pct = .62 # percentage of trapezoidal height
        self.bottom_trim= .935 # percentage from top to bottom avoiding the hood of the car

        self.images = glob.glob('../resources/test_images/*.jpg')

        if self.images == []:
            error("Cannot find test images")

    def lanedetection_pipeline(self, frames):
        
        """

        parameter
        ________
        None 

        Function
        _______


        return 
        _______
        None

        """
        pass



# we initialize the class
if __name__ == '__main__':

    preprocess = LaneDetect()
    cap = cv2.VideoCapture('../resources/video2.mp4')

    if (cap.isOpened()== False): 
        print("Error opening video  file")
        
    # Read until video is completed
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            frame = preprocess.lanedetection_pipeline(frame)
            cv2.imshow('Frame', frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey() & 0xFF == ord('q'):
            break
        # Break the loop
        else: 
            break 
    