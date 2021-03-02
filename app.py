import os
from flask import Flask, jsonify, render_template, request, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./videos"

@app.route("/")
def upload_file():
    return render_template('formulario.html')

@app.route("/uploader", methods=['POST'])
def uploader():
    if request.method == "POST":
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return render_template('video_procesing.html')




if __name__ == '__main__':
    app.run(debug=True)


'''
    @app.route('/ping')
def ping():
    return jsonify({"message":"pong!"})

@app.route('/products')
def getProducts():
    return jsonify(products)

@app.route('/products/<string:product_name>')    
def getProduct(product_name):
    print(product_name)
    return 'recived'
    '''