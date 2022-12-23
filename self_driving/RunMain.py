import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os
from time import sleep
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import WebcamModule as wM
import MotorModule as mM

#######################################
steeringSen = 1  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
motor = mM.Motor(2, 3, 4, 17, 22, 25) # Pin Numbers
model = load_model('/home/pi/Desktop/files/self_driving/model3.h5', compile=False)
from tensorflow.keras.optimizers import Adam

model.compile(Adam(learning_rate=0.0001),loss='mse')

######################################

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img

while True:

    img = wM.getImg(False)
    img = np.asarray(img)
    img = preProcess(img)
    img = np.array([img])
    steering = float(model.predict(img))
    final = round(-steering*steeringSen,3)
    if(final < 0):

        if(final > -0.02):
            final = 0
        #else:
        #    final-=0.02

        if(final < -1): final = -1
    elif(final > 0):
        #if(final < 0.02): final = 0
        if(final > 1): final = 1

    print(final)
    #sleep(0.1)
    motor.move(0.3,final)
    cv2.waitKey(1)