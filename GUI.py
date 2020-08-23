import os
import tkinter

# Problem uploadImage.py can't able to open camera after open from this.
# interface


def uploadImage():
    os.system("python uploadImage.py")


def trainingDataBase():
    os.system("python trainingOnDataBase.py")


def detectCriminal():
    os.system("python detectCriminal.py")


def openSheet():
    os.system("hello.xlsx")


top = tkinter.Tk()
upload = tkinter.Button(top, text="1.upload", command=uploadImage)
trainer = tkinter.Button(top, text="2.trainer", command=trainingDataBase)
recognizer = tkinter.Button(top, text="3.recognizer", command=detectCriminal)
showRecord = tkinter.Button(top, text="4.openSheet", command=openSheet)

upload.pack()
trainer.pack()
recognizer.pack()
showRecord.pack()
top.mainloop()
