''' Adam Iskandar Bin Ahmad Faisal
    1181101747
    CE
    
    Muhammad Amir Asyraf Bin Fazli
    1191301877
    CE
    
    Nur Syakira Binti Suhaimi
    1181101225
    CE
    
    ECE3086 Assignment 1 - Q3   '''

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
import torch
from time import time

path_working = r'/home/fortyone/Desktop/MMU/MMTECH/Assignment/ECE3086-Assignment/Assignment-1/Q3'
os.chdir(path_working)

def encodeVideoAsMJPEG(videoFile, duration):
    # your code
    cap = cv2.VideoCapture(videoFile)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    vFrameRate = np.round( cap.get(cv2.CAP_PROP_FPS) )
    print('Frame width:', frame_width)
    print('Frame height:', frame_height)
    print("Framerate:", vFrameRate)

    name = "Compressed Video"
    destinationFolder = os.path.join(path_working, name, 'compressedVid.mjpeg')

    if not os.path.exists(name):
        os.makedirs(name)

    video = cv2.VideoWriter(destinationFolder, cv2.VideoWriter_fourcc(*'mjpg'), vFrameRate, (frame_width, frame_height))

    while True:
        has_frame, frame = cap.read()
        if not has_frame:
            print('Can\'t get frame')
            break
        
        video.write(frame)
        
        cv2.imshow('frame', frame)
        key = cv2.waitKey(3)
        if key == 27:
            print('Pressed Esc')
            break

    cap.release()
    video.release()
    cv2.destroyAllWindows()

    sizevideoFile = os.path.getsize(videoFile)
    sizecompressedFile = os.path.getsize(destinationFolder)

    compressionRatio = sizevideoFile / sizecompressedFile

    print("Size of original video = ", np.round(sizevideoFile/(1024*1024)) , "mb")
    print("Size of compresses video = ", np.round(sizecompressedFile/(1024*1024)) , "mb")


    return (destinationFolder, compressionRatio)

videoFile = '../myVideo.mp4'
folder, CR = encodeVideoAsMJPEG(videoFile, 10) #10 minutes

print("Compression ratio = ", CR)