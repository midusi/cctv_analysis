import os
from flask import Flask, jsonify, render_template, request, redirect
from werkzeug.utils import secure_filename
import uuid
import json
import sys
sys.path.insert(0, '../model/keras')
from yolo import YOLO, excecute


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
        kerasModel = YOLO()
        result = kerasModel.analyze_video(f'{filepath}')
        return result

if __name__ == '__main__':
    app.run(debug=True)

