import abc 
import cv2  
  
class BaseModel:
  
  @abc.abstractmethod
  def analyze_frame(self,frame):
    pass
  def analyze_video(self,video_path):
    vid = cv2.VideoCapture(video_path)
    if not vid.isOpened():
        raise IOError(f"Couldn't open video {video_path}")
    video_FourCC     = cv2.VideoWriter_fourcc(*'XVID')
    video_fps       = vid.get(cv2.CAP_PROP_FPS)
    video_size      = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    results=[]
    while True:
        return_value, frame = vid.read()
        if not return_value:
            break
        image = Image.fromarray(frame)
        results.append(self.analyze_image(image))
    return results
