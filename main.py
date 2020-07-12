import os
import datetime as dt

folder = str(dt.datetime.now()).replace(':', '_')[:10]

os.makedirs(folder)
current_path = os.path.abspath(os.getcwd())
video_file = input('Enter file path/name: ')
file = str(dt.datetime.now()).replace(':', '.')[:19]
save_file = os.path.join(current_path, folder, f'Cleaned_{file}.avi')

os.chdir('keras-deeplab-v3-plus')

from matplotlib import pyplot as plt
import cv2
import numpy as np
from model import Deeplabv3
from imutils.video import WebcamVideoStream

deeplab_model = Deeplabv3()

vid = cv2.VideoCapture(video_file)
try:
  blur_value = int(input('Enter odd blur integer value for kernel: '))
  blurValue = (blur_value, blur_value)
except:
  print('The provided blur value is not acceptable. Using default value of 35x35.')
  blurValue = (35,35)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter(save_file, codec, 15, (width, height))

while True:
    _, frame = vid.read()
    if not(_):
        break
    w, h, _ = frame.shape
    ratio = 512. / np.max([w,h])
       
    resized = cv2.resize(frame,(int(ratio*h),int(ratio*w)))
    resized = resized / 127.5 - 1.
    pad_x = int(512 - resized.shape[0])
    resized2 = np.pad(resized,((0,pad_x),(0,0),(0,0)),mode='constant')    
    res = deeplab_model.predict(np.expand_dims(resized2,0))
    labels = np.argmax(res.squeeze(),-1)    
    
    labels = labels[:-pad_x-25]
    mask = labels == 0    
    resizedFrame = cv2.resize(frame, (labels.shape[1],labels.shape[0]))
    blur = cv2.GaussianBlur(resizedFrame,blurValue,0)    
    resizedFrame[mask] = blur[mask]
    final_image = cv2.resize(resizedFrame, (width, height))
    writer.write(final_image)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
writer.release()
cv2.destroyAllWindows()