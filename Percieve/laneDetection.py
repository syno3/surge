## laoding modules that we need

from numpy.lib.type_check import imag


try:
    import cv2 as cv
    import numpy as np
    import matplotlib.pyplot as plt
    import cython
    import logging
    import math
except Exception as e:
    logging.error(e)


class Imagepreporcessing:
    """ 
    ImagePreprocessing : class
    
    parameters
    __________
    
    videopath = 'test video path'
    
    functions
    _________
    
    edges - canny edge detector
    mask - overlay edges on mask
    detected lanes - 
    average - 
    height - returns height of the frame
    make_points - 
    display_lines - draw lines 
    detected_lanes - wrapper function for all the other functions in the class
    
    """
    def __init__(self):
        self.videopath = 'resources/video.mp4'
        
    def videopath(self):
        """ 
        
        return 
        ______
        
        
        return the videopath variable as a string
        
        """
        return str(self.videopath)
    
    def edges(self, frame):
        """ 
        parameters
        _________
        
        frame - frame of the opencv video object
        
        converts the frame to grayscale
        blurs using gaussian blur
        detects edges using canny function
        
        return
        ______
        
        detected edges : return edgdes
        
        """
        
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(gray, (5,5), 0)
        edges = cv.Canny(blurred, 100, 300)
        
        return edges
    
    def mask(self, edges):
        """ 
        parameters
        __________
        
        edges - use the detected edges from egdes method
        
        obtains the height and width from calling shape function numpy
        creates polygon 
        creates blank mask using numpy zeros_like
        fills the mask with the polygon using fillpoly
        combines the filled mask with the detected edges using bitwise_and
        returns the final output
        
        return
        ______
        
        return mask
        
        
        """
        height, width = edges.shape
        ploygon = np.array([[
            (0, height/3),
            (width, height),
            (width, height),
            (0, height),
        ]], np.int32)
        
        mask = np.zeros_like(edges)
        
        mask = cv.fillPoly(mask, ploygon, 255)
        mask = cv.bitwise_and(edges, mask)
        return mask
    
    def detectlanes(self, mask):
        rho = 1
        angle = np.pi / 180 #angular precision in radian
        min_threshold = 10
        linesegement = cv.HoughLinesP(mask, rho, angle, min_threshold, np.array([]), minLineLength=8, maxLineGap=4)
        
        return linesegement 
    
    def average(self, frame, line_segments):
        """
        This function combines line segments into one or two lane lines
        If all line slopes are < 0: then we only have detected left lane
        If all line slopes are > 0: then we only have detected right lane
        """
        lane_lines = []
        if line_segments is None:
            logging.info('No line_segment segments detected')
            return lane_lines

        height, width, _ = frame.shape
        left_fit = []
        right_fit = []

        boundary = 1/3
        left_region_boundary = width * (1 - boundary)  # left lane line segment should be on left 2/3 of the screen
        right_region_boundary = width * boundary # right lane line segment should be on left 2/3 of the screen

        for line_segment in line_segments:
            for x1, y1, x2, y2 in line_segment:
                if x1 == x2:
                    logging.info('skipping vertical line segment (slope=inf): %s' % line_segment)
                    continue
                fit = np.polyfit((x1, x2), (y1, y2), 1)
                slope = fit[0]
                intercept = fit[1]
                if slope < 0:
                    if x1 < left_region_boundary and x2 < left_region_boundary:
                        left_fit.append((slope, intercept))
                else:
                    if x1 > right_region_boundary and x2 > right_region_boundary:
                        right_fit.append((slope, intercept))

        left_fit_average = np.average(left_fit, axis=0)
        if len(left_fit) > 0:
            lane_lines.append(image.make_points(frame, left_fit_average))

        right_fit_average = np.average(right_fit, axis=0)
        if len(right_fit) > 0:
            lane_lines.append(image.make_points(frame, right_fit_average))

        logging.debug('lane lines: %s' % lane_lines)  # [[[316, 720, 484, 432]], [[1009, 720, 718, 432]]]

        return lane_lines
    
    def height(self, image):
        height = image.shape[0]
        return height
    
    def make_points(self, frame, line):
        height, width, _ = frame.shape
        slope, intercept = line
        y1 = height  # bottom of the frame
        y2 = int(y1 * 1 / 2)  # make points from middle of the frame down

        # bound the coordinates within the frame
        x1 = max(-width, min(2 * width, int((y1 - intercept) / slope)))
        x2 = max(-width, min(2 * width, int((y2 - intercept) / slope)))
        
        return np.array([x1, y1, x2, y2])
    
    def display_lines(self, image, lines):
        
        lines_image = np.zeros_like(image)
        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line
                cv.line(lines_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
                
        return lines_image
    
    ### putting it all together
    def detect_lane(self, frame):
        
        edges = image.edges(frame)
        cropped_edges = image.mask(edges)
        line_segments = image.detectlanes(cropped_edges)
        lane_lines = image.average(frame, line_segments)
        
        return lane_lines


###### compute the steering directions between the two lanes detected ######

class motionPlanning(Imagepreporcessing):
    def __init__(self):
        super().__init__()
    pass

    def laneLines(self, frame):
        
        lane_lines = image.detect_lane(frame)
        return lane_lines[0][0], lane_lines[1][0]
    
    def heightAndWidth(self, qframe):
        
        height, width, _ = frame.shape
        return height, width
    
    def steering(self, frame):
        
        height, width = motion.heightAndWidth(frame)
        left_x2= lane_lines[0][0]
        right_x2= lane_lines[1][0]
        mid = int(width / 2)
        
        x_offset = (left_x2 + right_x2) / 2 - mid
        y_offset = int(height / 2)
        angle_to_mid_radian = math.atan(x_offset / y_offset)  # angle (in radian) to center vertical line
        angle_to_mid_deg = int(angle_to_mid_radian * 180.0 / math.pi)  # angle (in degrees) to center vertical line
        steering_angle = angle_to_mid_deg + 90  # this is the steering angle needed by picar front wheel
        
        return steering_angle

    
    def display_heading_line(self, frame, steering_angle, line_color=(0, 0, 255), line_width=10 ):
        heading_image = np.zeros_like(frame)
        height, width, _ = frame.shape

        # figure out the heading line from steering angle
        # heading line (x1,y1) is always center bottom of the screen
        # (x2, y2) requires a bit of trigonometry

        # Note: the steering angle of:
        # 0-89 degree: turn left
        # 90 degree: going straight
        # 91-180 degree: turn right 
        steering_angle_radian = steering_angle / 180.0 * math.pi
        x1 = int(width / 2)
        y1 = height
        x2 = int(x1 - height / 2 / math.tan(steering_angle_radian))
        y2 = int(height / 2)

        cv.line(heading_image, (x1, y1), (x2, y2), line_color, line_width)
        heading_image = cv.addWeighted(frame, 0.8, heading_image, 1, 1)

        return heading_image


### reading the video frame
image = Imagepreporcessing()
motion = motionPlanning()
video_path = image.videopath
cap = cv.VideoCapture(video_path)




while(cap.isOpened()):
    ret, frame = cap.read()
    lane_lines = image.detect_lane(frame)
    lane_detected = image.display_lines(frame, lane_lines)
    lanes = motion.laneLines(frame)
    steering = motion.steering(frame)
    heading = motion.display_heading_line(frame, steering)

    
    lanes = cv.addWeighted(heading, 0.8, lane_detected, 1, 1)
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(lanes, 
                'STEERING ANGLE :{}'.format(steering), 
                (50, 50), 
                font, 1, 
                (0, 255, 255), 
                2, 
                cv.LINE_4)
    
    cv.imshow('lane_detected',lanes)
    #cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()