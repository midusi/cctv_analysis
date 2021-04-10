import os
from flask import Flask, jsonify, render_template, request, redirect
from werkzeug.utils import secure_filename
import uuid
import json
import requests
from model.keras.yolo import YOLO
from model.openCv.OpenCv import OpenCV
import threading


with open('app_cfg.json') as file:
    app_cfg = json.load(file)


app = Flask(__name__)

#configuracion inicial

app.config['UPLOAD_FOLDER'] = app_cfg['videos_path']
model_cfg = app_cfg['default_model'] # por defecto opencv_320
#para cambiar modelo ----> remplazar x con un numero del 1 al 5
# 1 = opencv_320  2 = opencv_416  3 = opencv_608  4 = opencv_tiny  5 = keras
#model_cfg = app_cfg['models']['5']


#homepage
@app.route("/")
def upload_file():
    return render_template('formulario.html')

#sube video a la ruta especificada en app_cfg.json y le asigna un ID unico
#luego procesa el video y genera un json con la informacion
@app.route("/uploader", methods=['POST'])
def uploader():
    if request.method == "POST":
        f = request.files['archivo']
        filename = str(uuid.uuid4())
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(filepath)
        model = load(model_cfg)
        result = {
            'peoplePerFrame': model.analyze_video(f'{filepath}')
        } 
        with open('{}.json'.format(f'{filepath}'), 'w') as file:
            json.dump(result, file, indent=4)
        return render_template('video_procesing.html')

#sube video a la ruta especificada en user_cfg.json y le asigna un ID unico
#luego procesa el video y retorna el json generado con la informacion
#Los videos y resultados van a parar a la carpeta definida en app_cfg.json (por defecto carpeta files)

def model_video_processing(filepath):
    print("entre a model_video_processing")
    model = load(model_cfg)
    result = {
        'peoplePerFrame': model.analyze_video(f'{filepath}')
    } 
    #with open('{}.json'.format(f'{filepath}'), 'w') as file:
        #json.dump(result, file, indent=4)
    print("voy a enviar request")
    url = 'http://127.0.0.1:5001/client_response'
    respuesta = requests.post(url, json=result)
    print(respuesta.text)

@app.route("/model_request", methods=['POST'])
def model_request():
    if request.method == "POST":
        print("entre a model_request")
        f = request.files['file']
        filename = str(uuid.uuid4())
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(filepath)
        #ejecutar thread en segundo plano (model_request)
        thread = threading.Thread(target=model_video_processing, args=(filepath, ))
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution
        return filename





def load(model_name):

    if model_name.startswith("keras"):
        return YOLO()
    elif model_name.startswith("opencv"):
        version = model_name.split('_',1)[1]
        return OpenCV(version)
    else:
        raise ValueError(f"Model {model_name} not found")
