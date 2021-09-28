
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