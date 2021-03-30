import abc 
#import cv2  
  
class BaseModel(abc.ABC):
  
  @abc.abstractmethod
  def analyze_frame(self,frame):
    pass
  def analyze_video(self,video_path):
    pass

  
  import sys
  sys.path.insert(0, 'keras/')
  from keras.yolo import YOLO
  #from keras import YOLO
  
  def load(model_name):
    print("inicia modelo :",model_name)
    if model_name.startswith("yolo"):
      return YOLO(model_name)
    else:
      raise ValueError(f"Model {model_name} not found")
    '''elif model_name.startswith("opencv"):
      return OpenCVDetector(model_name)'''

