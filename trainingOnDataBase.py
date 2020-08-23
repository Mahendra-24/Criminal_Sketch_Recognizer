import os
import cv2
import numpy as np

# Inialize recognizer
detectFace = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


recognizer = cv2.face.LBPHFaceRecognizer_create()

os.chdir("criminalDataBase")


initial_id = 0
labels_ids = {}  # {'name', id}
ids = []  # id of person
faces = []  # contain image to be train

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".png") or file.endswith(".jpg"):
        	folderName = os.path.join(root, file)
			label = os.path.basename(root).replace(" ", "-").lower()

            # Create labels_ids dictionary
            if not foloderName in labels_ids:
                labels_ids[label] = initial_id
                initial_id = initial_id + 1
            
            # Load image, L for grayscale
            img = Image.open(path).convert("L")

            # Convert img to numpy array
            img_np = np.array("img", "uint8")

            # Extract face form image
            face = detector.detectMultiScale(img_array, scaleFactor = 1.1, minNeighbors=5)
			cv2.waitKey(1)
			for (x,y,w,h) in face:
				roi = img_array[y:y+h, x:x+w] # roi = region of interest (face of person in img)
				
				faces.append(roi)#it contain all image face
				ids.append(labels_ids[label])#it contain labels corresponding to faces in train[]

# label will use in recognizer.py modules,so save in file
os.chdir('..')
labelsFile = open("labels.pickle",'wb')
pickle.dump(labels_ids,labelsFile)


try:#if no image is present in exception arise.

	recognizer.train(faces,np.array(ids))
	# recognizer needs train[] and name(labels[]) of ther person to train

	recognizer.save('trainer.yml')
	print("trained")
	
except:
	print("no image to recognize, please upload image")
	print("untrained")
