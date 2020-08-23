import os
import cv2


# Detect face (use leter in code to detect face)
detectFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Move to SketchDataBase folder
os.chdir("criminalDataBase")

# Maximum no of image to be taken
MAXIMG = 400

# Take 600 image using loop
while (MAXIMG > 0):
    # At starting enter name
    if(MAXIMG == 400):
        name = input("Enter name")
        file_no = input("File no")
        crime_commited = input("Crime Commit")
        criminal_act = input("Enter criminal act")
        enter_time = input("Enter time")
        predicted_exit_time = input("Predicted exit time")

        # Create a directory with above name
        try:
            os.mkdir(file_no)
        except:
            print("Person photo already present, add more")

        # Move to directory that is created
        os.chdir(file_no)

        # Open Camera
        webcam = cv2.VideoCapture(0)

    # Take Sketch or photo
    check, frame = webcam.read()

    # Convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect face
    faces = detectFace.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # (x,y,w,h) axis(x,y) and width and hight of face

        # crop and save face
        crop_face = frame[y:y+h, x:x+w]
        imgName = "{0}{1}.jpg".format(file_no, MAXIMG)  # name of image
        cv2.imwrite(imgName, crop_face)

        # create rectangle around face
        color = (255, 0, 0)  # color of recangle
        thickness = 2  # thickness of rectangle
        cv2.rectangle(gray, (x, y), (x+w, y+h), color, thickness)

        # display image
        # put no.(text) on image
        textOnImage = "Image left to take {0}".format(MAXIMG)
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (50, 50)  # position form ORiGin
        fontScale = 1  # size of text
        color = (0, 0, 255)  # optional
        thickness = 1  # optional
        cv2.putText(gray,
                    textOnImage,
                    org, font, fontScale, color, thickness)

        # Display current img
        cv2.imshow("image", gray)
        key = cv2.waitKey(2)  # wait, otherwise system hacks and stop.

        # Decrement by 1 on every one face taken
        MAXIMG = MAXIMG - 1
        print(MAXIMG)
