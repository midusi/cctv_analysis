# CCTV analysis.

A cctv analysis server to asynchronously analyse videos for objects such as persons or cars in cctv camera feeds.
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

## Introduction.

KERAS implementation of YOLOv3 (Tensorflow backend) inspired by [allanzelener/YAD2K](https://github.com/allanzelener/YAD2K).


---

## Initial setup for model.

1. Clone the repository on your computer.
2. Download YOLOV3 weights from: [YOLO website](http://pjreddie.com/darknet/yolo/). Or at this drive link https://drive.google.com/file/d/1NUYrGllK8diIkVZbmIjMqR6BiUhwLgCZ/view?usp=sharing
3. Convert the YOLO Darknet model to a KERAS model.
4. Run YOLO detection.


wget https://pjreddie.com/media/files/yolov3.weights 
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5

Once weights are converted, model can be used by the next instructions: 
python yolo_video.py [OPTIONS...] --image, for image detection mode, OR
python yolo_video.py [video_path] [output_path (optional)]
For Tiny YOLOv3, just do in a similar way, just specify model path and anchor path with --model model_file and --anchors anchor_file.

### WEB server

To run the app localy:

python app.py  
server runs at http://127.0.0.1:5000/ localy,
select video and after procesing the output can be found at the proyect folder as a .yml file called lista


### Usage of the model

usage: yolo_video.py [-h] [--model MODEL] [--anchors ANCHORS]
                     [--classes CLASSES] [--gpu_num GPU_NUM] [--image]
                     [--input] [--output]

positional arguments:
  --input        Video input path
  --output       Video output path

optional arguments:
  -h, --help         show this help message and exit
  --model MODEL      path to model weight file, default model_data/yolo.h5
  --anchors ANCHORS  path to anchor definitions, default
                     model_data/yolo_anchors.txt
  --classes CLASSES  path to class definitions, default
                     model_data/coco_classes.txt
  --gpu_num GPU_NUM  Number of GPU to use, default 1
  --image            Image detection mode, will ignore all positional arguments

