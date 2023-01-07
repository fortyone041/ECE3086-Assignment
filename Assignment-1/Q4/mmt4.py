''' Adam Iskandar Bin Ahmad Faisal
    1181101747
    CE
    
    Muhammad Amir Asyraf Bin Fazli
    1191301877
    CE
    
    Nur Syakira Binti Suhaimi
    1181101225
    CE
    
    ECE3086 Assignment 1 - Q4   '''

import cv2
from tkinter import Label
from tkinter import *
from tkinter import filedialog
import numpy as np
import tkinter as tk

import os
# change the path according to your pc
work_path= r'/home/fortyone/Desktop/MMU/MMTECH/Assignment/ECE3086-Assignment/Assignment-1/Q4'
os.chdir(work_path)

i=0
ctr=0
#root = tk.Tk()
#var=tk.IntVar()
#root = tk.Tk()
#%% Call back function

def init():
    print('Init() called when window start')

def addCount():
    global ctr
    global i
    ctr = i+10

def reduceCount():
    global ctr
    global i
    ctr = i-10   

def runDemo():
    filename = filedialog.askopenfilename()
    print("Selected video file = {} ".format (filename) )
    status = showVideo(filename)

def showVideo(filename):
    global ctr
    global i
    i = 0
    cap = cv2.VideoCapture(filename)
    frameNum = []
    vFrameRate = np.round( cap.get(cv2.CAP_PROP_FPS) )
    totalFrame = np.round(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    name, ext = os.path.splitext(filename)
    destinationFolder = os.path.join(work_path, name, 'vid.mjpeg')

    if not os.path.exists(name):
        os.makedirs(name)

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video = cv2.VideoWriter(destinationFolder, cv2.VideoWriter_fourcc(*'mjpg'), vFrameRate, (frame_width, frame_height))

    for x in range(int(totalFrame)):
        ret, frame = cap.read()
        frameNum.append(frame)
        video.write(frame)

    video.release()

    while i <= int(totalFrame):
        cap.isOpened()
        if button2['relief'] != "raised":
            addCount()
            i = ctr
            print(" Video counter ctr incremented = ", ctr)

        if  button3['relief'] != "raised":
            reduceCount()
            i = ctr
            print(" Video counter ctr reduced = ", i)

        if button4['relief'] != "raised":
            print('Video Paused')
            button5.wait_variable(var)
            print('Video Resumed')

        if ret == False :
            break

        currFrame = frameNum[i]
        cv2.imshow('frame',currFrame)
        print("Display frame {}".format(i) )
        
        if cv2.waitKey(40) & 0xFF == ord('q'):  # "Press q to clear video "
            break
        
        window.update()
        i = i + 1
        
    cap.release()
    return 1

#%%

window = Tk()
var=tk.IntVar()
window.geometry("300x300")
window.title(" My Simple Video Player ")

label1 = Label(window, text=" My Video Player ", 
                fg='blue', bg='yellow',
                relief = "solid",
                font=("arial",16,'bold')).place(x=10,y=10)

button1 = tk.Button(window, text = "Get video file", relief = RAISED, command= runDemo)
button1.place(x=10,y=110)

button2 = Button(window, text = "Increase Count", relief = RAISED, command=addCount)
button2.place(x=10,y=150)

button3 = Button(window, text = "Decrement Count", relief = RAISED, command=reduceCount)
button3.place(x=10,y=190)

button4 = Button(window, text = "Pause", relief = RAISED)
button4.place(x=10,y=270)

button5 = Button(window, text = "Play", relief = RAISED, command = lambda: var.set(1))
button5.place(x=10,y=230)

window.after_idle(init)
window.mainloop()

































