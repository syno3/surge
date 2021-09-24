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


## ACTUAL LANE DETECTION CLASS
class Lanedetection:
    def __init__(self) -> None:
        pass

# we initialize the class
#cameracalibration = cameracalibration(9, 6)
#cameracalibration.distortionCoefficients()
