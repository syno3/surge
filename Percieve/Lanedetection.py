# we do advanced lane detection udacity project
# based on this (https://towardsdatascience.com/advanced-lane-detection-for-autonomous-vehicles-using-computer-vision-techniques-f229e4245e41)
# (https://github.com/uppala75/CarND-Advanced-Lane-Lines/blob/master/AdvancedLaneLines.md)


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


## CAMERA CALIBRATION
class cameracalibration:
    def __init__(self, nx: int, ny: int, path: str) -> None:
        # Calibrate the Camera
        # number of inside corners in x & y directions
        self.nx = nx
        self.ny = ny
        self.path = path

        # prepare object points
        self.objp = np.zeros((6*9,3), np.float32)
        self.objp[:,:2] = np.mgrid[0:9, 0:6].T.reshape(-1,2)

        # Arrays to store object points and image points from all the images
        self.objpoints = [] # 3d points in real world space
        self.imgpoints = [] # 2d points in image plane

        # list the images
        self.images = glob.glob(path)

    def cornersfound(self):

        plt.figure(figsize = (18,12))
        grid = gridspec.GridSpec(5,4)

        # set the spacing between axes.
        grid.update(wspace=0.05, hspace=0.15)  

        for idx, fname in enumerate(self.images):
            img = cv2.imread(fname)
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Find the chessboard corners
            ret, corners = cv2.findChessboardCorners(gray, (self.nx, self.ny), None)

            # If found, add to object points, image points
            if ret == True:
                self.objpoints.append(self.objp)
                self.imgpoints.append(corners)

                # Draw and display the corners
                img = cv2.drawChessboardCorners(img, (self.nx, self.ny), corners, ret)
                write_name = 'corners_found'+str(idx)+'.jpg'
                #cv2.imwrite(write_name,img)
                img_plt = plt.subplot(grid[idx])
                plt.axis('on')
                img_plt.set_xticklabels([])
                img_plt.set_yticklabels([])
                #img_plt.set_aspect('equal')
                plt.imshow(img)
                plt.title(write_name)
                plt.axis('off')
        plt.show()
        #plt.axis('off')

    def distortionCoefficients(self):
        """ 
        Use the objpoints and imgpoints to compute the camera calibration and distortion coefficients using the cv2.calibrateCamera() function. This distortion correction was applied to the test image using the cv2.undistort() function.

        """
        pass


# we initialize the class
cameracalibration = cameracalibration(9, 6, 'resources/calibration*.jpg')
