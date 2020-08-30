"""
# GOOGLE-NET Image CLASSIFICATION :
"""
print(__doc__)

import sys
import cv2
import numpy as np

from _path import get_cut_dir, stop_if_none

dir_src = get_cut_dir('openCV_TAcademy') + 'src\\'
dir_dnn = get_cut_dir('classify') + 'src_dnn\\'
dir_img = get_cut_dir('classify') + 'src_img\\'

filename = dir_img + 'space_shuttle.jpg' # 99.99 %
filename = dir_img + 'scooter.jpg'       # 59.21 %
filename = dir_img + 'pineapple.jpg'     # pineapple, ananas = 99.99 %
filename = dir_img + 'cup.jpg'           # espresso = 99.72 %
filename = dir_img + 'dog_retreiver.jpg' # gonden retreiver = 99.34 %
filename = dir_img + 'dog_beagle.jpg'    # 78.35 %

# filename = dir_src + 'namecard3.jpg'     # rubber eraser, pencil.. 18.35 %
# filename = dir_src + 'coin.png'          # PNG.FILE = ERROR - NULL OBJECT!

model = dir_dnn + 'bvlc_googlenet.caffemodel'
config = dir_dnn + 'deploy.prototxt'
classes = dir_dnn + 'classification_classes_ILSVRC2012.txt'

img = cv2.imread(filename, )
img = stop_if_none(img, message="Null Object!")

# cv2.imshow('img', img)
# cv2.waitKey()

# LOAD CLASS NAMES -> if net.empty():
net = cv2.dnn.readNet(model, config)
net = stop_if_none(net, message='Network load failed!')


# Load class names
classNames = None
with open(classes, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Inference
inputBlob = cv2.dnn.blobFromImage(img, 1, (224, 224), (104, 117, 123))
net.setInput(inputBlob, 'data')
prob = net.forward()
out = prob.flatten()


# Check results & Display
classId = np.argmax(out)
confidence = out[classId]

text = f"ID: {classNames[classId]:} ({confidence * 100:5.2f} %)"
print(text)

cv2.putText(img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
