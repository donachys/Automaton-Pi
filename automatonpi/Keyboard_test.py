import math
import random
import sys
import time
import pygame
from Car import Car
from pygame.locals import *

myCar = Car()
forward = False
backward = False
moveLeft = False
moveRight = False
motorVal = 0

FPS = 30 # frames per second to update the screen
WINWIDTH = 640 # width of the program's window, in pixels
WINHEIGHT = 480 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption('Automaton-Pi')
BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

def terminate():
    myCar.straight()
    myCar.neutral()
    pygame.quit()
    sys.exit()

while (1):
    if(myCar.ready):
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()

            elif event.type == KEYDOWN:
                if event.key in (K_UP, K_w):
                    if(motorVal < 0):
                        motorVal = 0
                    else:
                        motorVal += 10
                elif event.key in (K_DOWN, K_s):
                    if(motorVal > 0):
                        motorVal = 0
                    else:
                        motorVal -= 10
                elif event.key in (K_LEFT, K_a):
                    moveLeft = True
                elif event.key in (K_RIGHT, K_d):
                    moveRight = True
                elif event.key == K_ESCAPE:
                    terminate()
        if(motorVal > 0):
            forward = True
            backward = False
            neutral = False
        elif(motorVal < 0):
            backward = True
            forward = False
            neutral = False
        elif(motorVal == 0):
            neutral = True
            backward = False
            forward = False

        if (forward):
            print "calling forward: %d" % motorVal
            myCar.forward(motorVal)
        elif (backward):
            print "calling reverse: %d" % motorVal
            myCar.reverse(motorVal)
        elif (neutral):
            "calling neutral"
            myCar.neutral()
        print "motorVal: %d" % motorVal

        if(moveRight and moveLeft):
            print "calling straight"
            myCar.straight()
            moveRight = False
            moveLeft = False
        elif(moveRight):
            moveLeft = False
            print "calling right"
            myCar.right(50)
        elif(moveLeft):
            moveRight = False
            print "calling left"
            myCar.left(50)
        else:
            print "calling straight"
            myCar.straight()
    else:
        print("myCar not READY")