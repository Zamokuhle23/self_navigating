
import requests
import cv2
import numpy as np
import imutils

#cap = cv2.VideoCapture(0)
#vid = cv2.VideoCapture("http://192.168.43.179:8080/shot.jpg")
url = "http://192.168.43.251:8080/shot.jpg"
def getImg(display= False,size=[480,240]):
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=size[0], height=size[1])
    #if not cap.isOpened():
    #    print("Cannot open camera")
    #    exit()


    #_, img = cap.read()

    #img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
    return img

if __name__ == '__main__':
    while True:
        getImg(True)