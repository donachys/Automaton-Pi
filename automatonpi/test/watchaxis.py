#!/usr/bin/env python2

from __future__ import print_function
import pygame
import time
from pygame.locals import *

pygame.init()


def get_ps3_joystick():
    if pygame.joystick.get_count() != 0:
        return pygame.joystick.Joystick(0)
    else:
        return None


def run_event_loop(joystick):
    joystick.init()
    pygame.event.set_allowed([JOYAXISMOTION, JOYBALLMOTION,
                              JOYBUTTONDOWN, JOYBUTTONUP,
                              JOYHATMOTION])
    watched_axes = {16: None, 17: None, 18: None, 19: None}

    while True:
        for event in pygame.event.get():
            if event.type == JOYAXISMOTION and event.dict['axis'] in watched_axes.keys():
                if watched_axes[event.dict['axis']] != event.dict['value']:
                    watched_axes[event.dict['axis']] = event.dict['value']
                    print(event)
        time.sleep(0.01)


def main():
    joystick = get_ps3_joystick()
    if joystick is None:
        return -1
    run_event_loop(joystick)


if __name__ == '__main__':
    main()
