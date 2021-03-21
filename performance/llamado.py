import os
import pathlib

#os.system(f'python ../model/yoloOpenCv/probando.py people3.mp4 yolov3-tiny.cfg yolov3-tiny.weights')

os.system(f'python ../model/keras/yolo_video.py --input people3.mp4')
