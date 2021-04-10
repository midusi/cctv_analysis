import gdown
from pathlib import Path
import os

relative_path = os.path.dirname(os.path.relpath(__file__))
pathYoloH5file = relative_path + '/cfg/yolo.h5'
pathYoloWeightFile = relative_path + '/weights/yolov3.weights'
pathYoloTinyWeightFile = relative_path + '/weights/yolov3-tiny.weights'

yoloH5file = Path(pathYoloH5file)
yoloWeightFile = Path(pathYoloWeightFile)
yoloTinyWeightFile = Path(pathYoloTinyWeightFile)


if not (yoloH5file.is_file()):
    gdown.download("https://drive.google.com/uc?id=1Wr8leP54mo_BzZF7hbKH5_n-wOt0QVDQ&export=download",pathYoloH5file)
if not (yoloWeightFile.is_file()):
    gdown.download("https://drive.google.com/uc?id=1e6mMCvbFGynFZg1oJVN3IV8MoR8cUGrK&export=download",pathYoloWeightFile)
if not (yoloTinyWeightFile.is_file()):
    gdown.download("https://drive.google.com/uc?id=1iW8SRBCjGrhY3gwiDbTzQCoYVMXiP7tB&export=download",pathYoloTinyWeightFile)
