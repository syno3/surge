from numpy import matrix


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

    def abs_sobel_thresh(self, img, orient='x', thresh_min=25, thresh_max=255):
        # Convert to grayscale
        # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS).astype(np.float64)
        l_channel = hls[:, :, 1]
        s_channel = hls[:, :, 2]
        # Apply x or y gradient with the OpenCV Sobel() function
        # and take the absolute value
        if orient == 'x':
            abs_sobel = np.absolute(cv2.Sobel(l_channel, cv2.CV_64F, 1, 0))
        if orient == 'y':
            abs_sobel = np.absolute(cv2.Sobel(l_channel, cv2.CV_64F, 0, 1))
        # Rescale back to 8 bit integer
        scaled_sobel = np.uint8(255 * abs_sobel / np.max(abs_sobel))
        # Create a copy and apply the threshold
        binary_output = np.zeros_like(scaled_sobel)
        # Here I'm using inclusive (>=, <=) thresholds, but exclusive is ok too
        binary_output[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1

        # Return the result
        return binary_output

    def color_threshold(self, image, sthresh=(0, 255), vthresh=(0, 255)):
        hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
        s_channel = hls[:, :, 2]
        s_binary = np.zeros_like(s_channel)
        s_binary[(s_channel > sthresh[0]) & (s_channel <= sthresh[1])] = 1

        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        v_channel = hsv[:, :, 2]
        v_binary = np.zeros_like(v_channel)
        v_binary[(v_channel > vthresh[0]) & (v_channel <= vthresh[1])] = 1

        output = np.zeros_like(s_channel)
        output[(s_binary == 1) & (v_binary) == 1] = 1

        # Return the combined s_channel & v_channel binary image
        return output

    def window_mask(self, width, height, img_ref, center, level):
        output = np.zeros_like(img_ref)
        output[int(img_ref.shape[0] - (level + 1) * height):int(img_ref.shape[0] - level * height),
        max(0, int(center - width)):min(int(center + width), img_ref.shape[1])] = 1
        return output

    @property
    def load_pickle(self):
        # loading pickle file
        with open(self.path_calibrationPickle, "rb") as input_file:
            e = pickle.load(input_file)

        mtx = e.get('mtx')
        dist = e.get('dist')

        return mtx, dist

    def image_pipeline(self, images: matrix):

        mtx, dist = self.load_pickle

        undistTest = cv2.undistort(images, mtx, dist, None, mtx)
        #Apply Sobel operator in X-direction to experiment with gradient thresholds
        gradx = self.abs_sobel_thresh(undistTest, orient='x', thresh_min=20, thresh_max=100)

        #Apply Sobel operator in Y-direction to experiment with gradient thresholds
        grady = self.abs_sobel_thresh(undistTest, orient='y', thresh_min=20, thresh_max=100)

        #Experiment with HLS & HSV color spaces along with thresholds
        c_binary = self.color_threshold(undistTest, sthresh=(100,255), vthresh=(50,255))

        #Combine the binary images using the Sobel thresholds in X/Y directions along with the color threshold to form the final image pipeline
        preprocessImage = np.zeros_like(undistTest[:,:,0])
        preprocessImage[((gradx == 1) & (grady ==1) | (c_binary == 1))] = 255

        return preprocessImage
