import os
import sys
sys.path.insert(0, '../model/keras')
from yolo import YOLO, excecute
from timeit import default_timer as timer
import numpy as np

'''os.system(f'python ../model/yoloOpenCv/probando.py people3.mp4 yolov3-tiny.cfg yolov3-tiny.weights')
print("Termino Ejecucion yolov3-tiny\n\n")
os.system(f'python ../model/yoloOpenCv/probando.py people3.mp4 yolov3-320.cfg yolov3.weights')
print("Termino Ejecucion yolov3-320\n\n")
os.system(f'python ../model/yoloOpenCv/probando.py people3.mp4 yolov3-416.cfg yolov3.weights')
print("Termino Ejecucion yolov3-416\n\n")
os.system(f'python ../model/yoloOpenCv/probando.py people3.mp4 yolov3-608.cfg yolov3.weights')
print("Termino Ejecucion yolov3-608\n\n")'''

#Keras model
kerasModel = YOLO()
print("empezo ejecucion de modelo")
start = timer()
resultado = excecute(kerasModel,'people3.mp4',"")
end = timer()
meanPersons = np.mean(resultado['list'])
print('Rendimiento ----------')
print('Personas encontradas en promedio por frame : ',meanPersons) 
print("tiempo total : ",end-start)
print("FPS promedio : ",((len(resultado['list']))/(end-start)))
print('-----------------------')
print("Termino Ejecucion keras\n\n")