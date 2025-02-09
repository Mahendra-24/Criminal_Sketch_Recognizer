# Match face, detect name and save attendence.
import cv2
import os
from time import sleep
import pickle

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {}

with open("labels.pickle", 'rb') as f:
    orig_labels = pickle.load(f)
    labels = {k: v for v, k in orig_labels.items()}  # reverse dic

# Take image
webcam = cv2.VideoCapture(0)  # start camera
while True:
    check, frame = webcam.read()  # start reading image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # roi->region of interest (faces in image)
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]

        try:
            id, conf = recognizer.predict(face_gray)
        except:
            print("Does not train yet,run tranner.py module,")
            input()  # wait
        # predict the face
        # conf conformation
        # 0 means 100% confirm

        if conf >= 45 and conf <= 85:
            print(labels[id])
        # Create rectangel
        color = (255, 0, 0)
        thickness = 2
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, thickness)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)
