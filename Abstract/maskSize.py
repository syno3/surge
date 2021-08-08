import matplotlib.pyplot as plt
import cv2 as cv


path = 'resources/video.mp4'
cap = cv.VideoCapture(path)

for i in range(1):
    ret, frame = cap.read()
    plt.imshow(frame)
    plt.show()
    #cv.imshow('frame', frame)
    if cv.waitKey(0) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
    