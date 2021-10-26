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