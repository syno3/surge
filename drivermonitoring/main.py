# we warp all the functions together to one video and display the output
# convert to cython

# required imports
import os
import cv2
import numpy as np
from threading import Thread
from playsound import playsound # we play warning sound
from time import sleep

# importing required cython files
from enviroment import enviroment
from face import face
from cpu import cpu
from abstract import *


# we instantiate class in global variables
Enviroment = enviroment()
Face = face()
CPU = cpu()

# main video class
class videoOutput:
    def __init__(self) -> None:
        # random variables i need
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.font_size = 0.6
        self.font_thickness = 1
        self.line_type = cv2.LINE_AA

        # colors for opencv
        self.yellow = (0, 255, 255)
        self.red = (0, 0, 255)
        self.blue = (255, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.path = '../resources/video4.mp4'
        self.recording_path = 'assets/recordings'

        # debugging
        self.distracted = False
        self.drowsy = False
        self.i = 0
        self.cap = None

        self.play = False
        
        # paths for notifications sounds

    # we record evidence of inappropriate driving   
    def record_evidence(self, frame: np.ndarray) ->None:

        """
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        we write the frame to new location and increase index
        
        return
        _______

        None

        """

        location = os.path.join(self.recording_path, 'capture' + str(self.i) + '.jpg')
        cv2.imwrite(location, frame)
        self.i += 1

    # we pass frames to the enviroment pipeline
    def enviroment_pipeline(self, frame: np.ndarray) ->str:

        """
        parameters
        _________

        Frame : we take the frames as the input

        function
        ________

        we take frame and convert to HSV color space. We get the last V value and calculate the mean of the value.

        using the mean we determine the level of brightness and saturation levels
        
        return
        _______

        str : the output string of the levels of brightness and saturation level
        """
        brightness_output = Enviroment.brightness_level(frame)
        saturation_output = Enviroment.saturation_level(frame)
        return brightness_output, saturation_output

    # we pass frames to face pileline
    def face_pipeline(self, frame: np.ndarray) ->int:
        pass

    def debug(self):
        # main video
        self.cap = cv2.VideoCapture(self.path)
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            frame = cv2.resize(frame, (680, 480))  # reducing this increases speed

            # frame resolution text
            cv2.putText(frame, "Frame size: {}".format(frame.shape[:2]), (10, 30), self.font, self.font_size,
                        self.yellow, self.font_thickness, self.line_type)

            #enviroment pipeline (module to be threaded)
            brightness_output, saturation_output = self.enviroment_pipeline(frame)

            # frame brightness text
            cv2.putText(frame, "Exposure: {}".format(brightness_output), (10, 50), self.font,
                        self.font_size, self.yellow, self.font_thickness, self.line_type)

            # frame saturation text
            cv2.putText(frame, "Saturation: {}".format(saturation_output), (10, 70), self.font,
                        self.font_size, self.yellow, self.font_thickness, self.line_type)

            # frames per second test
            number = Enviroment.frames_per_second()
            if number < 15:
                cv2.putText(frame, "Frames Per Sec: {}".format(number), (10, 90), self.font, self.font_size, self.red,
                            self.font_thickness, self.line_type)
            else:
                cv2.putText(frame, "Frames Per Sec: {}".format(number), (10, 90), self.font, self.font_size, self.green,
                            self.font_thickness, self.line_type)

            # error for face not detected
            e1 = cv2.getTickCount()  # debugging speed
            detected, count, score, x, w, y, h = Face.facedetect(frame)
            
            if detected:
                # face detected
                cv2.putText(frame, "Face detected: {}".format(detected), (10, 130), self.font, self.font_size,
                            self.green, self.font_thickness, self.line_type)
                cv2.putText(frame, "Detection accuracy: {}%".format(score), (10, 150), self.font, self.font_size,
                            self.green, self.font_thickness, self.line_type)
                cv2.putText(frame, "Face position: {}, {}".format(x, y), (10, 170), self.font, self.font_size,
                            self.green, self.font_thickness, self.line_type)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.rectangle(frame, (x, y), (x+w, y-25), (0, 0, 255), -1)
                cv2.putText(frame, f'{score}', (x, y), 
cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                # number of faces detected
                cv2.putText(frame, "Number of Faces detected: {}".format(count), (10, 210), self.font,
                            self.font_size, self.green, self.font_thickness, self.line_type)
                # distance of camera from face
                marker = Face.find_marker(frame)
                dist = Face.distance_to_camera(marker)
                cv2.putText(frame, "Distance from camera: Appx {} inches".format(dist), (10, 230), self.font,
                            self.font_size, self.green, self.font_thickness, self.line_type)
                
                # driver attention aka (drowsiness, smartphone taking, wearing seatbelt) // keep proof ie. record part he was sleeping
                # distracted, warning = Face.driver_attention(frame)
                #self.drowsy, _, _ = Drowsy.detect_drowsiness(frame)
                if self.distracted:
                    # run the record part
                    self.record_evidence(frame)
                    # cv2.putText(frame, "Stay alert !!", (10, 190),self.font, self.font_size, self.red, self.font_thickness, self.line_type)
                #if self.drowsy:
                    #self.record_evidence(frame)
                    #cv2.putText(frame, "Please concetrate", (10, 190),self.font, self.font_size, self.red, self.font_thickness, self.line_type)
            else:
                # face not detected
                cv2.putText(frame, "Face not detected", (10, 130), self.font, self.font_size, self.red,
                            self.font_thickness, self.line_type)

            e2 = cv2.getTickCount()  # debugging speed
            time = (e2 - e1) / cv2.getTickFrequency()  # debugging speed
            if time < 0.01:
                cv2.putText(frame, "Clock speed: {}".format(time), (10, 190), self.font,
                            self.font_size, self.green, self.font_thickness, self.line_type)
            else:
                cv2.putText(frame, "Clock speed: {}".format(time), (10, 190), self.font,
                            self.font_size, self.red, self.font_thickness, self.line_type)
            print(f"clock cycles per second: {time}")  # debugging speed

            cv2.imshow('frame', frame)
            if cv2.waitKey(10) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    # we create separate generator function for stream
    def stream_buffer(self):
        self.cap = cv2.VideoCapture(self.path)
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            frame = cv2.resize(frame, (680//2, 480//2))
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'

    # we debug global variables for flask render
    def global_variables(self):
        self.cap = cv2.VideoCapture(self.path)
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            brightness_output, saturation_output = self.enviroment_pipeline(frame)
            number = Enviroment.frames_per_second()
            yield brightness_output, saturation_output, number



if __name__ == '__main__':
    run = videoOutput()
    run.debug() # we run the actual video when the file is called