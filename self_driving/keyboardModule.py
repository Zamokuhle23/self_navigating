import pygame
import MotorModule as M
value = 0
def init():
    pygame.init()
    win = pygame.display.set_mode((100,100))
intr = 0
notPressed = True
def getKey():
    init()
    global intr
    global value
    global notPressed
    ans = False
    for eve in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()

    if keyInput[pygame.K_LEFT]:
        value += 0.004
    elif keyInput[pygame.K_RIGHT]:
        value -= 0.004
    elif keyInput[pygame.K_r]:
        notPressed = True
        intr=1
    elif keyInput[pygame.K_s]:
        if notPressed:
            intr=2
            notPressed = False
        else:
            intr=0
    elif keyInput[pygame.K_SPACE]:
        intr=3
    elif keyInput[pygame.K_m]:
        intr=0
    else:
        value = 0



    pygame.display.update()
    if(value > 1):
        value = 1
    elif(value < -1):
        value = -1
    dict = {"value":round(value, 3),"share":intr}

    return dict

def main():
    motor= M.Motor(2,3,4,17,22,25)
    while(True):
        value= getKey()["value"]
        if(getKey()["share"] == 3):
          motor.stop()
        else:
            motor.move(0.3,round(value, 3))
            print("moving: ",round(value, 3))

if __name__ == '__main__':
    init()
    while True:
        main()