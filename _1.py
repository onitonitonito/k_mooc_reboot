""" Face Recognition by OpenCV-Python """
import urllib
import matplotlib.pyplot as plt
import cv2
import numpy as np


# File "D:\My Documents\GitHub\k_mooc_reboot\_1.py", line 11, in <module>
# f.write(xmldata) - TypeError: write() argument must be str, not bytes
# ---------------------
# xmldata = urllib.request.urlopen(
#     'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml'
#     ).read()
# f = open('haarcascade_frontalface.xml','w')
# f.write(xmldata)
# f.close()


def findfaces(full_url_to_image):
    f = urllib.request.urlopen(full_url_to_image)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')
    image = np.asarray(bytearray(f.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print("------> Found {0} faces! <------ ").format(len(faces))

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 5)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image, extent=[300, 500, 0, 1], aspect='auto')
    plt.grid(False)
    plt.axis('off')
    plt.show()

IMG_URL="http://i.telegraph.co.uk/multimedia/archive/03385/putin-berlusconi-s_3385218k.jpg"
findfaces(IMG_URL)
