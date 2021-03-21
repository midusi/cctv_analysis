import os
from flask import Flask, jsonify, render_template, request, redirect
from werkzeug.utils import secure_filename
import uuid
import json

with open('app_cfg.json') as file:
    data = json.load(file)

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = data['videopath']

@app.route("/")
def upload_file():
    return render_template('formulario.html')

@app.route("/uploader", methods=['POST'])
def uploader():
    if request.method == "POST":
        f = request.files['archivo']
        filename = str(uuid.uuid4())
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(filepath)
        os.system('python '+data['defaultModel']+f' --input {filepath}')
        return render_template('video_procesing.html')




if __name__ == '__main__':
    app.run(debug=True)

