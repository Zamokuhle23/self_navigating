from MotorModule import Motor
from LaneModule import getLaneCurve
import WebcamModule
import utlis

##################################################
motor = Motor(2,3,4,17,22,25)
##################################################

def main():
    utlis.initializeTrackbars()

    img = WebcamModule.getImg(False)
    curveVal= getLaneCurve(img,display=1)
    #print(curveVal)

    sen = 0.5  # SENSITIVITY
    maxVAl= 0.6 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    #if curveVal>0:
    #    sen =1
        #if curveVal<0.05: curveVal=0
    #else:
    #    if curveVal>-0.08: curveVal=0

    motor.move(0.6,curveVal*sen)

    print(curveVal*sen)
    #cv2.waitKey(1)


if __name__ == '__main__':
    while True:
        main()