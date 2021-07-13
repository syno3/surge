##########################################################
##                                                      ##
##     we use pretrained model for object detection     ##
##             YOLOV5                                   ##
##                                                      ##
##########################################################
### we import required modules
try:
  import torch ## to create NN and load model
  from matplotlib import pyplot as plt #to plot the images
  import numpy as np ## work with numoy arrays and other functions
  import cv2 as cv ## to load and process the video
  import logging ### to create logging
except Exception as e:
  logging.critical("{}".format(e)) ## print critical message

### instantiate some variables

path_video = '/content/Car - 2165.mp4'

## load the model ultralytics/yolov5
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

## Train model on video frames
cap = cv.VideoCapture(path_video)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2_imshow(np.squeeze(results.render()))
    
    if cv.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
