import random, sys, time, math, pygame
from pygame.locals import *
def terminate():
    pygame.quit()
    sys.exit()

for event in pygame.event.get(): # event handling loop
    if event.type == QUIT:
        terminate()

    elif event.type == KEYDOWN:
        if event.key in (K_UP, K_w):
            moveDown = False
            moveUp = True
        elif event.key in (K_DOWN, K_s):
            moveUp = False
            moveDown = True
        elif event.key in (K_LEFT, K_a):
            moveRight = False
            moveLeft = True
        elif event.key in (K_RIGHT, K_d):
        
        elif winMode and event.key == K_r:
                    return

        elif event.type == KEYUP:
        # stop moving the player's squirrel
        if event.key in (K_LEFT, K_a):
            moveLeft = False
        elif event.key in (K_RIGHT, K_d):
            moveRight = False
        elif event.key in (K_UP, K_w):
            moveUp = False
        elif event.key in (K_DOWN, K_s):
            moveDown = False

        elif event.key == K_ESCAPE:
            terminate()
