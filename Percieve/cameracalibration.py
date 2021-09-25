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

# CAMERA CALIBRATION CLASS
class CameraCalibration:
    def __init__(self, nx: int, ny: int) -> None:

        """ 
        parameter
        ________
        self.nx = 9 # size of the sqaure in chess box
        self.ny = 6

        self.paths # paths to different resources
        self.objp

        self.images # list of images in the calibration path

        Function
        _______

        we detect corners using cv2.findChessboardCorners and append the objp and corners in empty list. we then return the values.
        Use the objpoints and imgpoints to compute the camera calibration and distortion coefficients using the cv2.calibrateCamera() function. This distortion correction was applied to the test image using the cv2.undistort() function.
        we apply undistortion to test images using the cv2.undistort function and visualize using matplotlib

        return 
        _______
        None


        """
        # Calibrate the Camera
        # number of inside corners in x & y directions
        self.nx = nx
        self.ny = ny
        #../resources/test_images/test5.jpg
        # paths for the methods
        self.path = r'C:\Users\kirimi\Desktop\surge\resources\camera_cal\calibration*.jpg'
        self.path_calibration1 = r'C:\Users\kirimi\Desktop\surge\resources\camera_cal\calibration1.jpg'
        self.path_calibrationPickle = r'C:\Users\kirimi\Desktop\surge\resources\camera_cal\calibration_pickle.p'

        # prepare object points
        self.objp = np.zeros((6 * 9, 3), np.float32)
        self.objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

        # list the images
        self.images = glob.glob(self.path)

    @property
    def cornersfound(self):
        # Arrays to store object points and image points from all the images
        objpoints = []  # 3d points in real world space
        imgpoints = []  # 2d points in image plane

        for _, fname in enumerate(self.images):
            img = cv2.imread(fname)
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Find the chessboard corners
            ret, corners = cv2.findChessboardCorners(gray, (self.nx, self.ny), None)

            # If found, add to object points, image points
            if ret:
                objpoints.append(self.objp)
                imgpoints.append(corners)
                
        return objpoints, imgpoints

    def distortioncoefficients(self) -> None:
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
        # Take an image, object points, image points, and perform the camera calibration. Undistort the image after
        # camera calibration

        # load image for reference
        image = cv2.imread(self.path_calibration1)
        img_size = (image.shape[1], image.shape[0])

        # Perform camera calibration with the given object and image points
        objpoints, imgpoints = self.cornersfound

        _, mtx, dist, _, _ = cv2.calibrateCamera(objpoints, imgpoints, img_size, None, None)

        # Save the camera calibration results for later use
        dist_pickle = {"mtx": mtx, "dist": dist}
        pickle.dump(dist_pickle, open(self.path_calibrationPickle, "wb"))

        # Visualize the before/after distortion on chessboard images
        # undist = cv2.undistort(image, mtx, dist, None, mtx)
