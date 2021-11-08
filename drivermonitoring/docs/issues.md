## bugs

1. referenced before assignmet in body_pose detection

Traceback (most recent call last):
  File "C:\Users\Harry Muge\Desktop\surge\drivermonitoring\main.py", line 289, in <module>
    run.debug() # we run the actual video when the file is called
  File "C:\Users\Harry Muge\Desktop\surge\drivermonitoring\main.py", line 209, in debug
    cx, cy = Face.body_pose(frame)
  File "C:\Users\Harry Muge\Desktop\surge\drivermonitoring\face.py", line 254, in body_pose
    return cx, cy
UnboundLocalError: local variable 'cx' referenced before assignment
[ WARN:0] global C:\Users\runneradmin\AppData\Local\Temp\pip-req-build-1i5nllza\opencv\modules\videoio\src\cap_msmf.cpp (438) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback

2. pygame sound play

- plays in an increasing infinite loop

3. error in face detection

Traceback (most recent call last):
  File "C:\Users\Harry Muge\Desktop\surge\drivermonitoring\main.py", line 289, in <module>
    run.debug() # we run the actual video when the file is called
  File "C:\Users\Harry Muge\Desktop\surge\drivermonitoring\main.py", line 157, in debug
    detected, count, score, x, w, y, h = Face.facedetect(frame)
  File "C:\Users\Harry Muge\Desktop\surge\drivermonitoring\face.py", line 88, in facedetect
    for detection in enumerate(results.detections):
TypeError: 'NoneType' object is not iterable
[ WARN:0] global C:\Users\runneradmin\AppData\Local\Temp\pip-req-build-1i5nllza\opencv\modules\videoio\src\cap_msmf.cpp (438) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback

4. WSL pygame error

Traceback (most recent call last):
  File "main.py", line 276, in <module>
    run = videoOutput()
  File "main.py", line 63, in __init__
    mixer.init()
pygame.error

5. extreemly slow face detection c++

6. cython attribute error
Traceback (most recent call last):
  File "main.py", line 32, in <module>
    Face = face.face()
  File "face.pyx", line 56, in face.face.__cinit__
AttributeError: 'face.face' object has no attribute 'mp_face_detection'

7. Cant access webcam in wsl
[ WARN:0] global /tmp/pip-req-build-h45n7_hz/opencv/modules/videoio/src/cap_v4l.cpp (890) open VIDEOIO(V4L2:/dev/video0): can't open camera by index

8. main cant access cython methods
Traceback (most recent call last):
  File "E:\surge\drivermonitoring\main.py", line 279, in <module>
    run.debug() # we run the actual video when the file is called
  File "E:\surge\drivermonitoring\main.py", line 132, in debug
    brightness_output, saturation_output, brightness_value, _ = self.enviroment_pipeline(frame)
  File "E:\surge\drivermonitoring\main.py", line 84, in enviroment_pipeline
    brightness_output, brightness_value = Enviroment.brightness_level(frame)
AttributeError: 'enviroment.enviroment' object has no attribute 'brightness_level'
[ WARN:0] global C:\Users\runneradmin\AppData\Local\Temp\pip-req-build-1i5nllza\opencv\modules\videoio\src\cap_msmf.cpp (438) `anonymous-namespace'::SourceReaderCB::~SourceReaderCB terminating async callback