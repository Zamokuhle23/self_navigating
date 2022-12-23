import WebcamModule as wM
import DataCollectionModule as dcM
import keyboardModule as rm
import MotorModule as mM
import cv2
from time import sleep




maxThrottle = 0.3
motor = mM.Motor(2, 3, 4, 17, 22, 25)

record = 0
sens = 1
while True:
    joyVal = rm.getKey()
    #print(joyVal)
    steering = round(joyVal['value']*sens, 3)
    throttle = abs(joyVal["value"]*maxThrottle)
    if joyVal['share'] == 1:
        print('Recording Started ...')
        img = wM.getImg(False,size=[240,120])
        dcM.saveData(img,steering)
        #sleep(0.001)

    if joyVal['share'] == 2:
        dcM.saveLog()
    if joyVal['share'] == 3:
        motor.stop(0.02)
    #elif record == 2:
     #   dcM.saveLog()
     #   record = 0
    if joyVal['share'] != 3:
        print(steering)
        #motor.move(maxThrottle,steering)
    cv2.waitKey(1)