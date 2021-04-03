import os
from flask import Flask, jsonify, render_template, request, redirect
from werkzeug.utils import secure_filename
import uuid
import json
import sys
from model.keras.yolo import YOLO
from model.openCv.OpenCv import OpenCV


with open('user_cfg.json') as file:
    user_cfg = json.load(file)


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = user_cfg['videopath']

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
        kerasModel = YOLO()
        result = kerasModel.analyze_video(f'{filepath}')

        return render_template('video_procesing.html')

#sube video a la ruta especificada en user_cfg.json y le asigna un ID unico
#luego procesa el video y retorna el json generado con la informacion
#Los videos y resultados van a parar a la carpeta definida en user_cfg.json (por defecto carpeta files)

@app.route("/model_request", methods=['POST'])
def model_request():
    if request.method == "POST":
        f = request.files['file']
        filename = str(uuid.uuid4())
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(filepath)
        model = load('opencv_320')
        result = model.analyze_video(f'{filepath}')
        return {
            'peoplePerFrame': result
        }




def load(model_name):

    if model_name.startswith("yolo"):
        return YOLO()
    elif model_name.startswith("opencv"):
        version = model_name.split('_',1)[1]
        return OpenCV(version)
    else:
        raise ValueError(f"Model {model_name} not found")
