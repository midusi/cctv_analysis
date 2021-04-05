import os
import sys
sys.path.insert(0, '..')
from model.keras.yolo import YOLO
from model.openCv.OpenCv import OpenCV
from timeit import default_timer as timer
import numpy as np
import json

def load(model_name):
    if model_name.startswith("keras"):
        return YOLO()
    elif model_name.startswith("opencv"):
        version = model_name.split('_',1)[1]
        return OpenCV(version)
    else:
        raise ValueError(f"Model {model_name} not found")

#json resultados
performance = {}
data = []

def ejecutarModelo(modelName):
    model = load(modelName)
    print("empezo ejecucion de modelo")
    start = timer()
    resultado = model.analyze_video('people3.mp4')
    end = timer()
    meanPersons = np.mean(resultado)
    tiempoTotal = end - start
    FPS_Promedio = ((len(resultado))/(end-start))
    dataJson = {
        'Modelo': modelName,
        'PersonasPromedio': meanPersons,
        'tiempo total': tiempoTotal,
        'FPS_Promedio': FPS_Promedio
    }
    data.append(dataJson)
    return dataJson

#OpenCV tiny
modelData = ejecutarModelo('opencv_tiny')
print(modelData)

#OpenCV 320
modelData = ejecutarModelo('opencv_320')
print(modelData)

#OpenCV 416
modelData = ejecutarModelo('opencv_416')
print(modelData)

#OpenCV 608
modelData = ejecutarModelo('opencv_608')
print(modelData)

#Keras
modelData = ejecutarModelo('keras_default')
print(modelData)


performance['resumen'] = data

jsonData = json.dumps(performance, indent = 1)

print(jsonData)




