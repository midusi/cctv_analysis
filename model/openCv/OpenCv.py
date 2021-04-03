import sys
import cv2
import numpy as np
import yaml
import os
from timeit import default_timer as timer
import json
from ..base import BaseModel

'''class OpenCVDetector(BaseModel):
    def __init__(self,..,version):
        
        videoPath = '/../../server/videos/'+sys.argv[1]
        cfgPath = '/../cfg/'+sys.argv[2]
        weightsPath = '/../weights/'+version  ''' #codigo ejemplo facu     
       


class OpenCV(BaseModel):
    relative_path = os.path.dirname(os.path.relpath(__file__))
    whT = 320
    confThreshold = 0.5
    nmsThreshold = 0.3
    data = []
    accum_FPS = 0

    def __init__ (self, version):
        
        if version == '320':
            cfgPath = '/../cfg/yolov3-320.cfg'
            weightsPath = '/../weights/yolov3.weights'
            classesFile = self.relative_path+'/../cfg/coco_names.txt'
            self.classNames = []
            with open(classesFile,'rt') as f:
                self.classNames = f.read().rstrip('\n').split('\n')

            modelConfiguration = self.relative_path+cfgPath  
            modelWeights = self.relative_path+weightsPath

            self.net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
            self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
            print('se cargo modelo : ',version)
        
        if version == 'tiny':
            cfgPath = '/../cfg/yolov3-tiny'
            weightsPath = '/../weights/yolov3-tiny.weights'
            classesFile = self.relative_path+'/../cfg/coco_names.txt'
            self.classNames = []
            with open(classesFile,'rt') as f:
                self.classNames = f.read().rstrip('\n').split('\n')
            modelConfiguration = self.relative_path+cfgPath  
            modelWeights = self.relative_path+weightsPath

            self.net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
            self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
            print('se cargo modelo : ',version)

        if version == '416':
            cfgPath = '/../cfg/yolov3-416'
            weightsPath = '/../weights/yolov3-tiny.weights'
            classesFile = self.relative_path+'/../cfg/coco_names.txt'
            self.classNames = []
            with open(classesFile,'rt') as f:
                self.classNames = f.read().rstrip('\n').split('\n')
            modelConfiguration = self.relative_path+cfgPath  
            modelWeights = self.relative_path+weightsPath

            self.net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
            self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
            print('se cargo modelo : ',version)
    
        if version == '608':
            cfgPath = '/../cfg/yolov3-608'
            weightsPath = '/../weights/yolov3-tiny.weights'
            classesFile = self.relative_path+'/../cfg/coco_names.txt'
            self.classNames = []
            with open(classesFile,'rt') as f:
                self.classNames = f.read().rstrip('\n').split('\n')
            modelConfiguration = self.relative_path+cfgPath  
            modelWeights = self.relative_path+weightsPath

            self.net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
            self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
            self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
            print('se cargo modelo : ',version)


    def analyze_frame(self,outputs,img):
        hT, wT, cT =img.shape 
        p = 0
        bbox = []
        classIds = []
        confs = []
        for output in outputs:
            for det in output:
                scores = det [5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > self.confThreshold:
                    w,h = int (det[2]*wT) , int (det[3]*hT)
                    x,y = int (det [0]*wT - w/2) , int ((det[1]*hT)-h/2)
                    bbox.append([x,y,w,h])
                    classIds.append(classId)
                    confs.append(float(confidence))
        indices = cv2.dnn.NMSBoxes(bbox,confs,self.confThreshold,self.nmsThreshold)
        for i in indices:
            i = i[0]
            box = bbox[i]
            x,y,w,h = box[0],box[1],box[2],box[3]
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)  
            cv2.putText(img,f'{self.classNames[classIds[i]].upper()}{int(confs[i]*100)}%',
            (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
            #print(classNames[classIds[i]].upper())
            if self.classNames[classIds[i]].upper() == 'PERSON':
                p = p+1
        self.data.append(p)
        print('.')
        p = 0     


    def analyze_video(self, videoPath):
        cap = cv2.VideoCapture(videoPath)
        while True:
            success, img = cap.read()
            if not success:
                break
            blob = cv2.dnn.blobFromImage(img,1/255,(self.whT,self.whT),[0,0,0],1,crop=False)
            self.net.setInput(blob)
            layerNames = self.net.getLayerNames()
            outputNames = [layerNames [i[0]-1] for i in self.net.getUnconnectedOutLayers() ]
            outputs = self.net.forward(outputNames)
            self.analyze_frame(outputs,img)
        cv2.waitKey(1)
        print(self.data)
        return(self.data)

