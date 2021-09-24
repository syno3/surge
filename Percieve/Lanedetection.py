# we do advanced lane detection udacity project
# based on this (https://towardsdatascience.com/advanced-lane-detection-for-autonomous-vehicles-using-computer-vision-techniques-f229e4245e41)
# (https://github.com/uppala75/CarND-Advanced-Lane-Lines/blob/master/AdvancedLaneLines.md)


## improvements: 1. add timeit 2. add loading animation for corners found 3. write tests for the class 4.


try:
    import numpy as np
    import cv2
    import pickle
    import glob
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import matplotlib.gridspec as gridspec
    from logging import error
except Exception as e:
    error(e)


#### SOME GLOBAL VARIABLES


## CAMERA CALIBRATION CLASS
class cameracalibration:
    def __init__(self, nx: int, ny: int) -> None:
        # Calibrate the Camera
        # number of inside corners in x & y directions
        self.nx = nx
        self.ny = ny

        #paths for the methods
        self.path = r'C:\Users\kirimi\Desktop\surge\resources\camera_cal\calibration*.jpg'
        self.path_calibration1 = r'C:\Users\kirimi\Desktop\surge\resources\camera_cal\calibration1.jpg'
        self.path_calibrationPickle = r'C:\Users\kirimi\Desktop\surge\resources\camera_cal\calibration_pickle.p'

        # prepare object points
        self.objp = np.zeros((6*9,3), np.float32)
        self.objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1,2)

        # list the images
        self.images = glob.glob(self.path)

    @property
    def cornersfound(self):
        # Arrays to store object points and image points from all the images
        objpoints = []# 3d points in real world space
        imgpoints = []# 2d points in image plane

        for _, fname in enumerate(self.images):
            img = cv2.imread(fname)
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Find the chessboard corners
            ret, corners = cv2.findChessboardCorners(gray, (self.nx, self.ny), None)

            # If found, add to object points, image points
            if ret == True:
                objpoints.append(self.objp)
                imgpoints.append(corners)

        return objpoints, imgpoints

    def distortionCoefficients(self) ->None:
        """
        parameter
        ________
        None 

        Function
        _______
        Use the objpoints and imgpoints to compute the camera calibration and distortion coefficients using the cv2.calibrateCamera() function. This distortion correction was applied to the test image using the cv2.undistort() function.

        return 
        _______
        None

        """
        # Take an image, object points, image points, and perform the camera calibration. Undistort the image after camera calibration
        
        #load image for reference
        image = cv2.imread(self.path_calibration1)
        img_size = (image.shape[1], image.shape[0])

        # Perform camera calibration with the given object and image points
        objpoints, imgpoints = self.cornersfound

        _, mtx, dist, _, _ = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)

        # Save the camera calibration results for later use
        dist_pickle = {}
        dist_pickle["mtx"] = mtx
        dist_pickle["dist"] = dist
        pickle.dump(dist_pickle, open(self.path_calibrationPickle, "wb"))

        #Visualize the before/after distortion on chessboard images
        #undist = cv2.undistort(image, mtx, dist, None, mtx)

    def applyUndistort(self) ->None:

        """ 
        parameter
        ________
        None

        Function
        _______
        we apply undistortion to test images using the cv2.undistort function and visualize using matplotlib

        return 
        _______
        None

        """

        # Choose from the test images to demonstrate the before/after applying undistortion 
        testImg = cv2.imread('.resources/test_images/test5.jpg')
        testImg = cv2.cvtColor(testImg, cv2.COLOR_BGR2RGB)

        undistTest = cv2.undistort(testImg, mtx, dist, None, mtx)

        #Visualize the before/after distortion on test images
        plt.figure(figsize = (18,12))
        grid = gridspec.GridSpec(1,2)
        # set the spacing between axes.
        grid.update(wspace=0.1, hspace=0.1)  

        img_plt = plt.subplot(grid[0])
        plt.imshow(testImg)
        plt.title('Original test Image')

        img_plt = plt.subplot(grid[1])
        plt.imshow(undistTest)
        plt.title('Undistorted test Image')


        plt.show()


## WE PREPROCESS UNDISTORTED IMAGES
class PreprocessImage:
    """ 
    we do some basic image preprocessing from the undistorted image
    """
    def __init__(self) -> None:
        pass
    # Define a function that takes an image, gradient orientation,
    # and threshold min / max values.

    def abs_sobel_thresh(self, img, orient='x', thresh_min=25, thresh_max=255):
        # Convert to grayscale
        # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS).astype(np.float)
        l_channel = hls[:,:,1]
        s_channel = hls[:,:,2]
        # Apply x or y gradient with the OpenCV Sobel() function
        # and take the absolute value
        if orient == 'x':
            abs_sobel = np.absolute(cv2.Sobel(l_channel, cv2.CV_64F, 1, 0))
        if orient == 'y':
            abs_sobel = np.absolute(cv2.Sobel(l_channel, cv2.CV_64F, 0, 1))
        # Rescale back to 8 bit integer
        scaled_sobel = np.uint8(255*abs_sobel/np.max(abs_sobel))
        # Create a copy and apply the threshold
        binary_output = np.zeros_like(scaled_sobel)
        # Here I'm using inclusive (>=, <=) thresholds, but exclusive is ok too
        binary_output[(scaled_sobel >= thresh_min) & (scaled_sobel <= thresh_max)] = 1

        # Return the result
        return binary_output

    # Define a function to return the magnitude of the gradient for a given sobel kernel size and threshold values
    def mag_thresh(self, img, sobel_kernel=3, mag_thresh=(0, 255)):
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # Take both Sobel x and y gradients
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
        # Calculate the gradient magnitude
        gradmag = np.sqrt(sobelx**2 + sobely**2)
        # Rescale to 8 bit
        scale_factor = np.max(gradmag)/255 
        gradmag = (gradmag/scale_factor).astype(np.uint8) 
        # Create a binary image of ones where threshold is met, zeros otherwise
        binary_output = np.zeros_like(gradmag)
        binary_output[(gradmag >= mag_thresh[0]) & (gradmag <= mag_thresh[1])] = 1

        # Return the binary image
        return binary_output

    # Define a function to threshold an image for a given range and Sobel kernel
    def dir_threshold(self, img, sobel_kernel=3, thresh=(0, np.pi/2)):
        # Grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # Calculate the x and y gradients
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=sobel_kernel)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=sobel_kernel)
        # Take the absolute value of the gradient direction, 
        # apply a threshold, and create a binary image result
        absgraddir = np.arctan2(np.absolute(sobely), np.absolute(sobelx))
        binary_output =  np.zeros_like(absgraddir)
        binary_output[(absgraddir >= thresh[0]) & (absgraddir <= thresh[1])] = 1

        # Return the binary image
        return binary_output

    def color_threshold(self, image, sthresh=(0,255), vthresh=(0,255)):
        hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
        s_channel = hls[:,:,2]
        s_binary = np.zeros_like(s_channel)
        s_binary[(s_channel > sthresh[0]) & (s_channel <= sthresh[1])] = 1

        hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
        v_channel = hsv[:,:,2]
        v_binary = np.zeros_like(v_channel)
        v_binary[(v_channel > vthresh[0]) & (v_channel <= vthresh[1])] = 1

        output = np.zeros_like(s_channel)
        output[(s_binary == 1) & (v_binary) == 1] = 1

        # Return the combined s_channel & v_channel binary image
        return output

    def s_channel_threshold(self, image, sthresh=(0,255)):
        hls = cv2.cvtColor(image, cv2.COLOR_RGB2HLS)
        s_channel = hls[:, :, 2]  # use S channel

        # create a copy and apply the threshold
        binary_output = np.zeros_like(s_channel)
        binary_output[(s_channel >= sthresh[0]) & (s_channel <= sthresh[1])] = 1
        return binary_output

    def window_mask(self, width, height, img_ref, center, level):
        output = np.zeros_like(img_ref)
        output[int(img_ref.shape[0]-(level+1)*height):int(img_ref.shape[0]-level*height), max(0,int(center-width)):min(int(center+width),img_ref.shape[1])] = 1
        return output



class Lanedetection:
    def __init__(self):
        pass

# we initialize the class
#cameracalibration = cameracalibration(9, 6)
#cameracalibration.distortionCoefficients()
