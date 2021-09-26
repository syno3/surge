
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
except Exception as e:
    error(e)

# WE PREPROCESS UNDISTORTED IMAGES

class PreprocessImage(CameraCalibration):
    """ 
    we do some basic image preprocessing from the undistorted image
    """

    def __init__(self):
        super().__init__(nx=9, ny=6)

    # Define a function that takes an image, gradient orientation,
    # and threshold min / max values.
    @property
    def load_pickle(self):
        # loading pickle file
        with open(self.path_calibrationPickle, "rb") as input_file:
            e = pickle.load(input_file)

        mtx = e.get('mtx')
        dist = e.get('dist')

        return mtx, dist

    def image_pipeline(self, images):
        pass

# we initialize the class
if __name__ == '__main__':

    preprocess = PreprocessImage()
    cap = cv2.VideoCapture('../resources/video2.mp4')

    if (cap.isOpened()== False): 
        print("Error opening video  file")
        
    # Read until video is completed
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            frame = preprocess.image_pipeline(frame)
            cv2.imshow('Frame', frame)
        # Press Q on keyboard to  exit
        if cv2.waitKey() & 0xFF == ord('q'):
            break
        # Break the loop
        else: 
            break 