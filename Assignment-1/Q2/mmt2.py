''' Adam Iskandar Bin Ahmad Faisal
    1181101747
    CE
    
    Muhammad Amir Asyraf Bin Fazli
    1191301877
    CE
    
    Nur Syakira Binti Suhaimi
    1181101225
    CE
    
    ECE3086 Assignment 1 - Q2   '''

import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
import matplotlib
import torch
from time import time

path_working = r'/home/fortyone/Desktop/MMU/MMTECH/Assignment/ECE3086-Assignment/Assignment-1/Q2'
os.chdir(path_working)

videoFile = '../myVideo.mp4'
delay = 100

name = "Frames"
foldername = os.path.join(path_working, name)

if not os.path.exists(name):
    os.makedirs(name)

class ObjectDetection:
    """
    Class implements Yolo5 model to make inferences on a youtube video using OpenCV.
    """
    
    def __init__(self):
        """
        Initializes the class with youtube url and output file.
        :param url: Has to be as youtube URL,on which prediction is made.
        :param out_file: A valid output file name.
        """

        #self._URL = url
        self.model = self.load_model()
        self.classes = self.model.names
        #self.out_file = 'thor.mp4'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("\n\nDevice Used:",self.device)

    def load_model(self):
        """
        Loads Yolo5 model from pytorch hub.
        :return: Trained Pytorch model.
        """
        model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)
        return model

    def score_frame(self, frame):
        """
        Takes a single frame as input, and scores the frame using yolo5 model.
        :param frame: input frame in numpy/list/tuple format.
        :return: Labels and Coordinates of objects detected by model in the frame.
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
     
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def class_to_label(self, x):
        """
        For a given label value, return corresponding string label.
        :param x: numeric label
        :return: corresponding string label
        """
        return self.classes[int(x)]

    def get_class_list(self):
        return self.classes


    def plot_boxes(self, results, frame):
        """
        Takes a frame and its results as input, and plots the bounding boxes and label on to the frame.
        :param results: contains labels and coordinates predicted by model on the given frame.
        :param frame: Frame which has been scored.
        :return: Frame with bounding boxes and labels ploted on it.
        """
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.2:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame

    def runDetection(self, frame):
      results = self.score_frame(frame)
      frame = self.plot_boxes(results, frame)
      return frame, results

def summarizeVideo(videoFile, duration):
    # your code
    # return list of Jpeg .jpg files with human in the scene

    cap = cv2.VideoCapture(videoFile)
    vFrameRate = np.round( cap.get(cv2.CAP_PROP_FPS) )
    #frame at 10 minutes
    limit = int(vFrameRate*(duration*60))
    #limit = int(vFrameRate*(5))
    print(limit)
    frameList = []

    #declare yolov5 model
    obj = ObjectDetection()
    currPerson = 0

    for i in range(limit):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()

        #yolov5
        img_out, results_out = obj.runDetection(frame)

        labels, cord = results_out
        n = len(labels)
        detectedPerson = 0

        for x in range(n):
            if obj.class_to_label(labels[x]) == 'person': #find 'person' in frames
                detectedPerson = detectedPerson + 1

        #if number of person changes, save frame
        if currPerson != detectedPerson:
            currPerson = detectedPerson
            print( currPerson , ' detected')
            imfile = os.path.join(foldername,str(i)+'.jpg')
            cv2.imwrite(imfile, frame)
            frameList.append(str(i) + '.jpg')

    return frameList

framesList = summarizeVideo(videoFile, 10)
matplotlib.use('TkAgg')
fig = plt.figure()

for i, imf in enumerate(framesList[:20]):
    c = i + 1
    fig.add_subplot(4, 5, c).set_title(imf)
    im = cv2.imread(foldername + '/' + imf)
    plt.imshow(im)
    plt.axis('off')

plt.show()