''' Adam Iskandar Bin Ahmad Faisal
    1181101747
    CE
    
    Muhammad Amir Asyraf Bin Fazli
    1191301877
    CE
    
    Nur Syakira Binti Suhaimi
    1181101225
    CE
    
    ECE3086 Assignment 1 - Q1   '''

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
import matplotlib

path_working = r'/home/fortyone/Desktop/MMU/MMTECH/Assignment/ECE3086-Assignment/Assignment-1/Q2'
os.chdir(path_working)

def getVideoProperty(videoFile):
    # your code

    #vFramerate
    cap = cv2.VideoCapture(videoFile)
    vFrameRate = np.round( cap.get(cv2.CAP_PROP_FPS) )

    #resolution
    width  = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH)  )
    height = int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT) )
    resolution = str(width) + " x " + str(height)

    #videoSize
    filestats = os.stat(videoFile)
    videoSize = filestats.st_size / (1024 * 1024)

    return(vFrameRate, resolution, videoSize)

videoFile = '../myVideo.mp4'
vFrameRate, resolution, videoSize = getVideoProperty(videoFile)

print("Frame rate of video is = " + str(vFrameRate))
print("Resolution of video is = " + str(resolution))
print("Size of video is = " + str(videoSize) + " mb")