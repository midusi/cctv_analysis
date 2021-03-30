import sys
import cv2
import numpy as np
import yaml
import os
from timeit import default_timer as timer
import json

from ..base import BaseModel

class OpenCVDetector(BaseModel):
    def __init__(self,..,version):
        
        videoPath = '/../../server/videos/'+sys.argv[1]
        cfgPath = '/../cfg/'+sys.argv[2]
        weightsPath = '/../weights/'+version       
       


relative_path = os.path.dirname(os.path.relpath(__file__))

#Argunmentos ---> ArchivoVideo.mp4 archivo.cfg archivo.weights]

print(relative_path+videoPath)

cap = cv2.VideoCapture(relative_path+videoPath)
whT = 320
confThreshold = 0.5
nmsThreshold = 0.3
myList = []
accum_FPS = 0

classesFile = relative_path+'/../cfg/coco_names.txt'
classNames = []
with open(classesFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')


modelConfiguration = relative_path+cfgPath  
modelWeights = relative_path+weightsPath

net = cv2.dnn.readNetFromDarknet(modelConfiguration,modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

accum_time = 0
sumExec_time = 0
curr_fps = 0
fps = "FPS: ??"
prev_time = timer()

data = {}
data['list'] = []
def json_write(data):
    """guardo datos en un archivo json"""
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
        
def findObjets(outputs,img):
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
            if confidence > confThreshold:
                w,h = int (det[2]*wT) , int (det[3]*hT)
                x,y = int (det [0]*wT - w/2) , int ((det[1]*hT)-h/2)
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))

    indices = cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nmsThreshold)
    for i in indices:
        i = i[0]
        box = bbox[i]
        x,y,w,h = box[0],box[1],box[2],box[3]
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)  
        cv2.putText(img,f'{classNames[classIds[i]].upper()}{int(confs[i]*100)}%',
        (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
        #print(classNames[classIds[i]].upper())
        if classNames[classIds[i]].upper() == 'PERSON':
            p = p+1
    data['list'].append(p)
    p = 0

while True:
    success, img = cap.read()
    if not success:
            break
    blob = cv2.dnn.blobFromImage(img,1/255,(whT,whT),[0,0,0],1,crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    #print(layerNames)
    outputNames = [layerNames [i[0]-1] for i in net.getUnconnectedOutLayers() ]
    #print (outputNames)

    outputs = net.forward(outputNames)
    #print(outputs[0].shape)
    #print(outputs[1].shape)
    #print(outputs[2].shape)
    findObjets(outputs,img)
    curr_time = timer()
    exec_time = curr_time - prev_time
    prev_time = curr_time
    accum_time = accum_time + exec_time
    sumExec_time = sumExec_time + exec_time
    curr_fps = curr_fps + 1
    if accum_time > 1:
        accum_time = accum_time - 1
        fps = "FPS: " + str(curr_fps)
        accum_FPS = accum_FPS + curr_fps
        curr_fps = 0
        print(fps)
    #print(myList)
contador = 1    
for cantPersonasFrame in data['list']:
    #print('Frame :',contador,'cantidad de personas :',cantPersonasFrame)
    contador+=1
avg_FPS = accum_FPS / sumExec_time 
json_write(data)
meanPersons = np.mean(data['list'])
print('Rendimiento: ----------')
print('Personas encontradas en promedio por frame : ',meanPersons)
print('Tiempo total de ejecucion: ',sumExec_time)
print('FPS promedio de ejecucion: ',avg_FPS)  
print('-----------------------')
#cv2.imshow('Image',img)
cv2.waitKey(1)
