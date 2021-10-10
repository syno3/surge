# we warp all the functions together to one video and display the output
# convert to cython

# required imports
import cv2
import numpy as np
import os
from threading import Thread

# importing required cython files
from enviroment import enviroment
from face import face
from cpu import cpu
from abstract import *

# we instantiate class in global variables
Enviroment = enviroment()
Face = face()
CPU = cpu()


# Drowsy = drowsines()


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

    # we record evidence of inappropriate driving   
    def record_evidence(self, frame: np.ndarray):
        location = os.path.join(self.recording_path, 'capture' + str(self.i) + '.jpg')
        cv2.imwrite(location, frame)
        self.i += 1

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

            # frame brightness text
            cv2.putText(frame, "Exposure: {}".format(Enviroment.brightness_level(frame)), (10, 50), self.font,
                        self.font_size, self.yellow, self.font_thickness, self.line_type)

            # frame saturation text
            cv2.putText(frame, "Saturation: {}".format(Enviroment.saturation_level(frame)), (10, 70), self.font,
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
            detected, num_of_faces, _ = Face.detect_face(frame)  # will use rect later

            if detected:
                # face detected
                cv2.putText(frame, "Face detected: {}".format(detected), (10, 130), self.font, self.font_size,
                            self.green, self.font_thickness, self.line_type)

                # number of faces detected
                cv2.putText(frame, "Number of Faces detected: {}".format(num_of_faces), (10, 150), self.font,
                            self.font_size, self.green, self.font_thickness, self.line_type)
                # driver attention aka (drowsiness, smartphone taking, wearing seatbelt) // keep proof ie. record part he was sleeping
                # distracted, warning = Face.driver_attention(frame)
                # drowsy, _, _ = Drowsy.detect_drowsiness(frame)
                if self.distracted:
                    # run the record part
                    self.record_evidence(frame)
                    # cv2.putText(frame, "Stay alert !!", (10, 190),self.font, self.font_size, self.red, self.font_thickness, self.line_type)
                if self.drowsy:
                    self.record_evidence(frame)
                    # cv2.putText(frame, f"{warning}", (10, 190),self.font, self.font_size, self.red, self.font_thickness, self.line_type)
            else:
                # face not detected
                cv2.putText(frame, "Face not detected", (10, 130), self.font, self.font_size, self.red,
                            self.font_thickness, self.line_type)

            e2 = cv2.getTickCount()  # debugging speed
            time = (e2 - e1) / cv2.getTickFrequency()  # debugging speed
            print(f"clock cycles per second: {time}")  # debugging speed

            cv2.imshow('frame', frame)
            if cv2.waitKey(10) == ord('q'):
                break

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'  # concat frame one by one and show result

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    run = videoOutput()
    run.debug()  # actual video output

    # CPU.run()  we get cpu debug information
