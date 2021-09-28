# we warp all the functions together to one video and display the output

# required imports
import cv2
from logging import error
import time
import numpy as np
import os

# file imports
from enviroment import enviroment


# global varibales
Enviroment = enviroment()


# main video class
class videoOutput:
    def __init__(self) -> None:
        # random variables i need
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.font_size = 0.6
        self.font_thickness = 1
        self.line_type = cv2.LINE_AA
        self.yellow = (0, 255, 255)
        self.path = '../resources/video1.mp4'

    def debug(self):
        # main video
        cap = cv2.VideoCapture(self.path)
        while cap.isOpened():
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            frame = cv2.resize(frame, (640, 480)) 

            # frame resolution text
            cv2.putText(frame, "Frame size: {}".format(frame.shape[:2]), (10, 30),self.font, self.font_size, self.yellow, self.font_thickness, self.line_type) 

            # frame brightness text
            cv2.putText(frame, "Exposure: {}".format(Enviroment.brightness_level(frame)), (10, 50),self.font, self.font_size, self.yellow, self.font_thickness, self.line_type)

            # frame saturation text
            cv2.putText(frame, "Saturation: {}".format(Enviroment.saturation_level(frame)), (10, 70),self.font, self.font_size, self.yellow, self.font_thickness, self.line_type)

            #frames per second test
            cv2.putText(frame, "Frames Per Sec: {}".format(Enviroment.frames_per_second()), (10, 90),self.font, self.font_size, self.yellow, self.font_thickness, self.line_type)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    run = videoOutput()
    run.debug()
