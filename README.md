# CCTV analysis.

A cctv analysis server to asynchronously analyse videos for objects such as persons or cars in cctv camera feeds.
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction.

KERAS implementation of YOLOv3 (Tensorflow backend) inspired by [allanzelener/YAD2K](https://github.com/allanzelener/YAD2K).


---

## Initial setup for model.

1. Clone the repository on your computer.
2. Download YOLOV3 weights from: [YOLO website](http://pjreddie.com/darknet/yolo/). Or from this drive link https://drive.google.com/file/d/1NUYrGllK8diIkVZbmIjMqR6BiUhwLgCZ/view?usp=sharing , or use de wget instruction above
3. Convert the YOLO Darknet model to a KERAS model.
4. Run YOLO detection.


wget https://pjreddie.com/media/files/yolov3.weights 

at the model folder run:

python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5

the is model ready to run in the server.

### WEB server

To run the server localy:

python app.py  
server runs at http://127.0.0.1:5000/ localy,
use the "seleccionar archivo" button, then select video, once the video is selected click at the "enviar" button, after procesing the output can be found at the server folder as a .yml file called lista


