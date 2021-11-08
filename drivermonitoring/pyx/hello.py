import test
import enviroment
import face
import cv2

ex = test.test()
sy= test.say()
env = enviroment.enviroment()
fc = face.face()

print("TEST STARTING")

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("cant open frame")
        break
    #ex.hello(frame)
    #sy.smth()
    detected, count, score, x, w, y, h = fc.facedetect(frame)
    if detected:
    # face detected
        cv2.putText(frame, "Face detected: {}".format(detected), (10, 130), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(frame, "Detection accuracy: {}%".format(score), (10, 150), cv2.FONT_HERSHEY_COMPLEX, 0.6,(0, 255, 0), 1, cv2.LINE_AA)
        cv2.putText(frame, "Face position: {}, {}".format(x, y), (10, 170), cv2.FONT_HERSHEY_COMPLEX, 0.6,(0, 255, 0), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y), (x+w, y-25), (0, 0, 255), -1)
        cv2.putText(frame, f'{score}', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow("frame", frame)
    if cv2.waitKey(10) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    