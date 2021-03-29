import os
import pathlib
import sys
sys.path.insert(0, '../model/keras')
from yolo import YOLO, excecute
from timeit import default_timer as timer
import numpy as np
#archivo para pruebas

#os.system(f'python ../model/keras/yolo.py people3.mp4')
#os.system(f'python ../model/openCv/OpenCv.py people3.mp4 yolov3-320.cfg yolov3.weights')

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
