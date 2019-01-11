import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('cascades/haarcascade_frontalface_default.xml') # face classifier
eye_cascade = cv.CascadeClassifier('cascades/haarcascade_eye.xml') # eye classifier

cap = cv.VideoCapture(0) # start video recording

while (True):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # convert RGB frame to grayscale
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) # detect face in the grayscale frame

    for (x, y, w, h) in faces:
        print(x,y,w,h)
        roi_color = frame[y:y+h, x:x+w]
        roi_gray = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray) # detect eye in the faces

        for (ex, ey, ew, eh) in eyes:
            eye_frame_color = (0,255,0) # BGR
            eye_stroke = 2
            cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), eye_frame_color) # cv.distroyAllWindows(), eye_stroke)
            print(ex, ey)

        # Uncomment the below code if you want to save an image.
        # img_item = "my-image.png"
        # cv.imwrite(img_item, roi_color)

        face_frame_color = (0,0,255) #BGR
        face_stroke = 2
        cv.rectangle(frame, (x,y), (x+w, y+h), face_frame_color, face_stroke)

    cv.imshow('frame', frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()