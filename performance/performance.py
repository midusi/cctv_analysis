import os

'''os.system(f'python ../model/yoloOpenCv/probando.py people3.mp4 yolov3-tiny.cfg yolov3-tiny.weights')
print("Termino Ejecucion yolov3-tiny\n\n")
os.system(f'python ../model/yoloOpenCv/probando.py people3.mp4 yolov3-320.cfg yolov3.weights')
print("Termino Ejecucion yolov3-320\n\n")
os.system(f'python ../model/yoloOpenCv/probando.py people3.mp4 yolov3-416.cfg yolov3.weights')
print("Termino Ejecucion yolov3-416\n\n")
os.system(f'python ../model/yoloOpenCv/probando.py people3.mp4 yolov3-608.cfg yolov3.weights')
print("Termino Ejecucion yolov3-608\n\n")'''
os.system(f'python ../model/keras/yolo_video.py --input people3.mp4')
print("Termino Ejecucion keras\n\n")