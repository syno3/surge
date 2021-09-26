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

        self.gidx = 0

        self.window_width = 50
        self.window_height = 80

    def warp_perspective(self):
        """

        parameter
        ________
        None 

        Function
        _______

        we read images in the list and pass them through the pipeline we created. We then warp perspective by selecting a region of interest within the image, and create a bird's eye view.

        return 
        _______
        None

        """

        preprocess = PreprocessImage()
        mtx, dist = preprocess.load_pickle

        for _,fname in enumerate(self.images):
            img = cv2.imread(fname)
            img = cv2.undistort(img,mtx,dist,None,mtx)

            preprocessImage = preprocess.image_pipeline(img)
            
            img_size = (img.shape[1],img.shape[0])

            src = np.float32([[img.shape[1]*(0.5-self.mid_width/2), img.shape[0]*self.height_pct],[img.shape[1]*(0.5+self.mid_width/2),img.shape[0]*self.height_pct],[img.shape[1]*(0.5+self.bot_width/2), img.shape[0]*self.bottom_trim],[img.shape[1]*(0.5-self.bot_width/2), img.shape[0]*self.bottom_trim]])

            offset = img_size[0]*0.25
    
            dst = np.float32([[offset,0],[img_size[0]-offset,0],[img_size[0]-offset,img_size[1]],[offset,img_size[1]]])
            
            #perform the warp perspective transform
            M = cv2.getPerspectiveTransform(src, dst)
            Minv = cv2.getPerspectiveTransform(dst, src)
            warped = cv2.warpPerspective(preprocessImage, M, img_size, flags=cv2.INTER_LINEAR)

    def apply_convolution(self):

        """

        parameter
        ________
        None 

        Function
        _______

        Apply convolution which will maximize the number of "hot" pixels in each window. This convolution is the summation of the product of two separate signals: the window template and the vertical slice of the pixel image. The window template is slid across the image from left to right and any overlapping values are summed together, creating the convolved signal. The peak of the convolved signal is where the highest overlap of pixels occured and is the position for the lane marker.

        return 
        _______
        None

        """

        preprocess = PreprocessImage()
        mtx, dist = preprocess.load_pickle

        for _,fname in enumerate(self.images):
            #read in image
            img = cv2.imread(fname)
            #undistort the image
            img = cv2.undistort(img,mtx,dist,None,mtx)
            
            #pass image thru the pipeline
            preprocessImage = preprocess.image_pipeline(img)

            img_size = (img.shape[1],img.shape[0])
            
            src = np.float32([[img.shape[1]*(0.5-self.mid_width/2), img.shape[0]*self.height_pct],[img.shape[1]*(0.5+self.mid_width/2),img.shape[0]*self.height_pct],[img.shape[1]*(0.5+self.bot_width/2), img.shape[0]*self.bottom_trim],[img.shape[1]*(0.5-self.bot_width/2), img.shape[0]*self.bottom_trim]])

            offset = img_size[0]*0.25

            dst = np.float32([[offset,0],[img_size[0]-offset,0],[img_size[0]-offset,img_size[1]],[offset,img_size[1]]])
        
            #perform the warp perspective transform
            M = cv2.getPerspectiveTransform(src,dst)
            Minv = cv2.getPerspectiveTransform(dst,src)
            warped = cv2.warpPerspective(preprocessImage, M, img_size, flags=cv2.INTER_LINEAR)

            #set up the overall class to do the lane line tracking
            curve_centers = tracker(Mywindow_width=self.window_width, Mywindow_height=self.window_height, Mymargin = 25, My_ym = 10/720, My_xm = 4/384, Mysmooth_factor=15)
            
            window_centroids = curve_centers.find_window_centroids(warped)
            
            # Points used to draw all the left and right windows
            l_points = np.zeros_like(warped)
            r_points = np.zeros_like(warped)
                
            # points used to find the right & left lanes
            rightx = []
            leftx = []

            # Go through each level and draw the windows 
            for level in range(0,len(window_centroids)):
                # Window_mask is a function to draw window areas
                # Add center value found in frame to the list of lane points per left, right
                leftx.append(window_centroids[level][0])
                rightx.append(window_centroids[level][1])

                l_mask = preprocess.window_mask(self.window_width, self.window_height,warped,window_centroids[level][0],level)
                r_mask = preprocess.window_mask(self.window_width, self.window_height,warped,window_centroids[level][1],level)

                # Add graphic points from window mask here to total pixels found 
                l_points[(l_points == 255) | ((l_mask == 1) ) ] = 255
                r_points[(r_points == 255) | ((r_mask == 1) ) ] = 255

            # Draw the results
            template = np.array(r_points+l_points,np.uint8) # add both left and right window pixels together
            zero_channel = np.zeros_like(template) # create a zero color channel
            template = np.array(cv2.merge((zero_channel,template,zero_channel)),np.uint8) # make window pixels green
            warpage = np.array(cv2.merge((warped,warped,warped)),np.uint8) # making the original road pixels 3 color channels
            result = cv2.addWeighted(warpage, 1, template, 0.5, 0.0) # overlay the original road image with window results

        return result

    def ploynomial_fit(self):

        """

        parameter
        ________
        None 

        Function
        _______

        Fit a polynomial to the identified lane lines on the left and the right. Visualize the results by overlapping the lane lines on to the original undistorted image

        return 
        _______
        None

        """
        preprocess = PreprocessImage()
        mtx, dist = preprocess.load_pickle

        for _,fname in enumerate(self.images):
            #read in image
            img = cv2.imread(fname)
            #undistort the image
            img = cv2.undistort(img,mtx,dist,None,mtx)
            
            #pass image thru the pipeline

            preprocessImage = preprocess.image_pipeline(img)

            img_size = (img.shape[1],img.shape[0])
            
            src = np.float32([[img.shape[1]*(0.5-self.mid_width/2), img.shape[0]*self.height_pct],[img.shape[1]*(0.5+self.mid_width/2),img.shape[0]*self.height_pct],[img.shape[1]*(0.5+self.bot_width/2), img.shape[0]*self.bottom_trim],[img.shape[1]*(0.5-self.bot_width/2), img.shape[0]*self.bottom_trim]])

            offset = img_size[0]*0.25
            dst = np.float32([[offset,0],[img_size[0]-offset,0],[img_size[0]-offset,img_size[1]],[offset,img_size[1]]])   
            
            #src = np.float32([(532, 496), (756, 496), (288, 664), (1016, 664)])
            #dst = np.float32([(src[2][0], src[2][1] - 200),(src[3][0], src[3][1] - 200),(src[2][0], src[2][1]),(src[3][0], src[3][1])])

            #perform the warp perspective transform
            M = cv2.getPerspectiveTransform(src,dst)
            Minv = cv2.getPerspectiveTransform(dst,src)
            warped = cv2.warpPerspective(preprocessImage, M, img_size, flags=cv2.INTER_LINEAR)

            #set up the overall class to do the lane line tracking
            curve_centers = tracker(Mywindow_width=self.window_width, Mywindow_height=self.window_height, Mymargin = 25, My_ym = 10/720, My_xm = 4/384, Mysmooth_factor=15)
            
            window_centroids = curve_centers.find_window_centroids(warped)
            
            # Points used to draw all the left and right windows
            l_points = np.zeros_like(warped)
            r_points = np.zeros_like(warped)
                
            # points used to find the right & left lanes
            rightx = []
            leftx = []

            # Go through each level and draw the windows 
            for level in range(0,len(window_centroids)):
                # Window_mask is a function to draw window areas
                # Add center value found in frame to the list of lane points per left, right
                leftx.append(window_centroids[level][0])
                rightx.append(window_centroids[level][1])

                l_mask = preprocess.window_mask(self.window_width,self.window_height,warped,window_centroids[level][0],level)
                r_mask = preprocess.window_mask(self.window_width,self.window_height,warped,window_centroids[level][1],level)
                # Add graphic points from window mask here to total pixels found 
                l_points[(l_points == 255) | ((l_mask == 1) ) ] = 255
                r_points[(r_points == 255) | ((r_mask == 1) ) ] = 255

            # Draw the results
            template = np.array(r_points+l_points,np.uint8) # add both left and right window pixels together
            zero_channel = np.zeros_like(template) # create a zero color channel
            template = np.array(cv2.merge((zero_channel,template,zero_channel)),np.uint8) # make window pixels green
            warpage = np.array(cv2.merge((warped,warped,warped)),np.uint8) # making the original road pixels 3 color channels
            result = cv2.addWeighted(warpage, 1, template, 0.5, 0.0) # overlay the original road image with window results
            
            #fit the lane boundaries to the left, right center positions found
            yvals = range(0,warped.shape[0])
            
            res_yvals = np.arange(warped.shape[0]-(self.window_height/2),0,-self.window_height)
            
            left_fit = np.polyfit(res_yvals, leftx, 2)
            left_fitx = left_fit[0]*yvals*yvals + left_fit[1]*yvals + left_fit[2]
            left_fitx = np.array(left_fitx,np.int32)
            
            right_fit = np.polyfit(res_yvals, rightx, 2)
            right_fitx = right_fit[0]*yvals*yvals + right_fit[1]*yvals + right_fit[2]
            right_fitx = np.array(right_fitx,np.int32)
            
            left_lane = np.array(list(zip(np.concatenate((left_fitx-self.window_width/2, left_fitx[::-1]+self.window_width/2),axis=0),np.concatenate((yvals,yvals[::-1]),axis=0))),np.int32)
            right_lane = np.array(list(zip(np.concatenate((right_fitx-self.window_width/2, right_fitx[::-1]+self.window_width/2),axis=0),np.concatenate((yvals,yvals[::-1]),axis=0))),np.int32)

            road = np.zeros_like(img)
            road_bkg = np.zeros_like(img)
            cv2.fillPoly(road,[left_lane],color=[255,0,0])
            cv2.fillPoly(road,[right_lane],color=[0,0,255])
            cv2.fillPoly(road_bkg,[left_lane],color=[255,255,255])
            cv2.fillPoly(road_bkg,[right_lane],color=[255,255,255])

            road_warped = cv2.warpPerspective(road,Minv,img_size,flags=cv2.INTER_LINEAR)
            road_warped_bkg= cv2.warpPerspective(road_bkg,Minv,img_size,flags=cv2.INTER_LINEAR)
            
            base = cv2.addWeighted(img,1.0,road_warped, -1.0, 0.0)
            result = cv2.addWeighted(base,1.0,road_warped, 1.0, 0.0)

            
        return result


# we initialize the class
if __name__ == '__main__':
    lane = LaneDetect()
    lane.ploynomial_fit()




""" 
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
    
"""