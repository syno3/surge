# we warp all the functions together to one video and display the output
# convert to cython

# required imports
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' # we remove tensorflow messages
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # we remove pygame message
os.environ['SDL_AUDIODRIVER'] = 'dsp' #audio driver

import cv2
import numpy as np
from threading import Thread # we will use later

#python modules
from python import cpu, pose

#cython modules
from cython import func, enviroment, sleepNN

#cpp functions
#from cpp import *

# for image adjustment
from PIL import ImageEnhance

# we instantiate class in global variables
ENVIROMENT = enviroment.enviroment()
FACE = func.face()
CPU = cpu.cpu()
SLEEP = sleepNN.sleep()
POSE = pose.pose()

# main video class
class videoOutput:
    def __init__(self) -> None:
        # random variables i need
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.font_size = 0.6
        self.fon_size_big = 1.0
        self.font_thickness = 1
        self.font_thickness_big = 2
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
        self.warning_path = 'assets/warning.mp3'

        # debugging
        self.distracted = False
        self.drowsy = False
        self.i = 0
        self.cap = None
        
        # we play warning sound 
        #mixer.init()
        #self.sound = mixer.Sound(self.warning_path)
        
        # paths for notifications sounds


    # we record evidence of inappropriate driving   
    def record_evidence(self, frame: np.ndarray) ->None:
        # we collect frames of distraction and store in file
        
        location = os.path.join(self.recording_path, 'capture' + str(self.i) + '.jpg')
        cv2.imwrite(location, frame)
        self.i += 1


    # we pass frames to the enviroment pipeline
    def enviroment_pipeline(self, frame: np.ndarray) ->str:
        # we reduce function loops by using pipeline
        
        brightness_output, brightness_value = ENVIROMENT.brightness_level(frame)
        saturation_output, saturation_value = ENVIROMENT.saturation_level(frame)
        return brightness_output, saturation_output, brightness_value, saturation_value


    # we pass frames to face pileline
    def face_pipeline(self, frame: np.ndarray) ->int:
        pass

    
    # we enhance the frames
    def enhanced(self, frame:np.ndarray) ->np.ndarray:
        frame = ImageEnhance.Brightness(frame)
        factor = 1.5 # brigtens the image
        frame = frame.enhance(factor)
        
        return frame
    
    
    # we darken the frames
    def darken(self, frame:np.ndarray) ->np.ndarray:
        frame = ImageEnhance.Brightness(frame)
        factor = 0.5 #darkens the image
        frame = frame.enhance(factor)
        
        return frame
            
    
    def debug(self):
        # main video
        #self.cap = cv2.VideoCapture(self.path)
        self.cap = cv2.VideoCapture(0)
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            frame = cv2.resize(frame, (680, 480))  # reducing this increases speed
            height,width = frame.shape[:2] #we get frame height
            
            cv2.rectangle(frame, (0,height-50) , (200,height) , (0,0,0) , thickness=cv2.FILLED )
            # frame resolution text
            cv2.putText(frame, "Frame size: {}".format(frame.shape[:2]), (10, 30), self.font, self.font_size,
                        self.yellow, self.font_thickness, self.line_type)

            #enviroment pipeline (module to be threaded)
            brightness_output, saturation_output, brightness_value, _ = self.enviroment_pipeline(frame)

            # frame brightness text
            cv2.putText(frame, "Exposure: {}".format(brightness_output), (10, 50), self.font,
                        self.font_size, self.yellow, self.font_thickness, self.line_type)

            # frame saturation text
            cv2.putText(frame, "Saturation: {}".format(saturation_output), (10, 70), self.font,
                        self.font_size, self.yellow, self.font_thickness, self.line_type)            
            # frames per second test
            number = ENVIROMENT.frames_per_second()
            if number < 15:
                cv2.putText(frame, "Frames Per Sec: {}".format(number), (10, 90), self.font, self.font_size, self.red,
                            self.font_thickness, self.line_type)
            else:
                cv2.putText(frame, "Frames Per Sec: {}".format(number), (10, 90), self.font, self.font_size, self.green,
                            self.font_thickness, self.line_type)

            # error for face not detected
            e1 = cv2.getTickCount()  # debugging speed
            try:
                detected, count, score, x, w, y, h = FACE.facedetect(frame)
            except TypeError:
                detected = False     
            
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
                # distance of camera from face // we create threads
                marker = FACE.find_marker(frame)
                dist = FACE.distance_to_camera(marker)
                cv2.putText(frame, "Distance from camera: Appx {} inches".format(dist), (10, 230), self.font,
                            self.font_size, self.green, self.font_thickness, self.line_type)
                
                # driver attention aka (drowsiness, smartphone taking, wearing seatbelt) // keep proof ie. record part he was sleeping
                sleepy = SLEEP.detect_sleep(frame)
                #self.distarcted, _, _ = Drowsy.driver_distracted(frame)
                if sleepy:
                    # run the record part
                    #self.record_evidence(frame)
                    cv2.putText(frame, "Driver Not Attentive : {}".format(sleepy), (10, 250),self.font, self.font_size, self.red, self.font_thickness, self.line_type)
                else:
                    cv2.putText(frame, "Driver Attentive", (10, 250),self.font, self.font_size, self.green, self.font_thickness, self.line_type)                    
                # we get head pose direction      
                head_pose, text  = POSE.head_pose(frame) # we get head direction
                if head_pose:
                    # run the record part
                    #self.record_evidence(frame)
                    cv2.putText(frame, "Driver is Facing : {}".format(text), (10, 270),self.font, self.font_size, self.red, self.font_thickness, self.line_type)     
                else:
                    cv2.putText(frame, "Driver is Facing : {}".format(text), (10, 270),self.font, self.font_size, self.green, self.font_thickness, self.line_type)   

                # we detect driver pose
                results = POSE.body_pose(frame)
                if results != None:
                    cx, cy = results
                else:
                    cx, cy = 0, 0
                cv2.putText(frame, "Driver pose : {}, {}".format(cx, cy), (10, 290),self.font, self.font_size, self.green, self.font_thickness, self.line_type)            
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
            if cv2.waitKey(1) == ord('q'):
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
            frame = cv2.resize(frame, (680, 480))
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'

if __name__ == '__main__':
    try:
        import cProfile, pstats
        profiler = cProfile.Profile()
        profiler.enable() 

        run = videoOutput()
        run.debug() # we run the actual video when the file is called
        
        profiler.disable()
        stats = pstats.Stats(profiler)
        stats.dump_stats(filename='../assets/stats/stats.prof') # we dump the debug file
    except TypeError:
        run = videoOutput()
        run.debug()
