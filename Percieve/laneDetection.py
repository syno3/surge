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

    # we add this lines for debugging purpose
    cap = cv2.VideoCapture('../resources/video1.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()