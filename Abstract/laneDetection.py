## laoding modules that we need

try:
    import cv2 as cv
    import numpy as np
    import matplotlib.pyplot as plt
    import cython
    import logging
except Exception as e:
    logging.error(e)


class imagePreporcessing:
    def __init__(self):
        self.videopath = 'resources/video.mp4'
        
    def videopath(self):
        return self.videopath
    
    def edges(self, frame):
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        blurred = cv.GaussianBlur(gray, (5,5), 0)
        edges = cv.Canny(blurred, 100, 300)
        
        return edges
    
    def mask(self, edges):
        height, width = edges.shape
        ploygon = np.array([[
            (0, height/2),
            (width, height/2),
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
    
    def make_points(frame, line):
            
        height, width = frame.shape
        slope, intercept = line
        y1 = height  # bottom of the frame
        y2 = int(y1 * 1 / 2)  # make points from middle of the frame down

        # bound the coordinates within the frame
        x1 = max(-width, min(2 * width, int((y1 - intercept) / slope)))
        x2 = max(-width, min(2 * width, int((y2 - intercept) / slope)))
        
        return [[x1, y1, x2, y2]] 
    
    def averageslope(self, linesegement, edges):
        """
    
    This function combines line segments into one or two lane lines
    If all line slopes are < 0: then we only have detected left lane
    If all line slopes are > 0: then we only have detected right lane
    
        """
        lane_lines = []
        if linesegement is None:
            logging.info('No line_segment segments detected')
            return lane_lines
    
        height, width= edges.shape
        left_fit = []
        right_fit = []
        
        image = imagePreporcessing()
        
        boundary = 1/3
        left_region_boundary = width * (1 - boundary)  # left lane line segment should be on left 2/3 of the screen
        right_region_boundary = width * boundary # right lane line segment should be on left 2/3 of the screen
        
        for line_segment in linesegement:
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
    
### putting it all together
def detect_lane(frame): 
    image = imagePreporcessing()
         
    edges = image.edges(frame)
    mask = image.mask(edges)
    lines = image.detectlanes(mask)
    lanelines = image.averageslope(frame, lines)
        
    return lanelines
    
### reading the video frame
image = imagePreporcessing()
video_path = str(image.videopath)
cap = cv.VideoCapture(video_path)

while(cap.isOpened()):
    ret, frame = cap.read()
    #cv.imshow('frame',frame))
    lanes = detect_lane(frame)
    #cv.imshow('edges', detected_edges)
    cv.imshow('lanes', lanes)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()