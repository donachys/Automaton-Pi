#!/usr/bin/env python2

from automatonpi.packages.adafruit.Adafruit_PWM_Servo_Driver import PWM
import time

class CarState():
    """docsring for CarState"""
    pwm = PWM(0x40, debug=False)
    pwm.setPWMFreq(60)
    MOTORCHANNEL = 9
    SERVOCHANNEL = 8
    SERVOMIN = 385
    SERVOMAX = 515
    SERVOCENTER = int((SERVOMAX-SERVOMIN)/2.0)+SERVOMIN

    def steer(self, amt):
        tick = 0
        if(amt > 0):
            tick = int((self.SERVOMAX - self.SERVOCENTER) * (amt/100.00) + self.SERVOCENTER)
            print "<<<<<LEFT tick: %d" % tick
            
        elif(amt < 0):
            tick = int(self.SERVOCENTER -(self.SERVOCENTER - self.SERVOMIN) * (amt/100.00))
            print ">>>>>RIGHT tick: %d" % tick
        else:
            tick = self.SERVOCENTER

        self.pwm.setPWM(self.SERVOCHANNEL, 0, tick)

class ForwardState(CarState):
    """docstring for ForwardState"""
    MINFORWARD = 420
    MAXFORWARD = 550
    def __init__(self, f, s, myApp):
        self.force = f
        self.steer_val = s
        self.app = myApp
    def update(self):
        if(self.force > 100):
            self.force = 100
        elif(self.force < 0):
            self.force = 0
        tick = int(((spd/100.00) * (self.MAXFORWARD - self.MINFORWARD))+self.MINFORWARD)
        self.pwm.setPWM(self.MOTORCHANNEL, 0, tick)
        super(CarState,self).steer(self.steer_val)
    def handleInput(self, evt):
        if event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                #increase speed
                self.force+=10
            elif event.key in (K_DOWN, K_s):
                #change state to neutral
                self.car.state = NeutralState(self.steer_val, self.app)
            elif event.key in (K_LEFT, K_a):
                self.steer_val = -70
            elif event.key in (K_RIGHT, K_d):
                self.steer_val = 70

class ReverseState(CarState):
    """docstring for ReverseState"""
    MINREVERSE = 380
    MAXREVERSE = 250
    def __init__(self, f, s, myApp):
        self.force = f
        self.steer_val = s
        self.app = myApp
    def update(self):
        if(self.force > 100):
            self.force = 100
        elif(self.force < 0):
            self.force = 0
        tick = int(self.MINREVERSE-((abs(spd)/100.00) * (self.MINREVERSE - self.MAXREVERSE)))
        self.pwm.setPWM(self.MOTORCHANNEL, 0, tick)
        super(CarState,self).steer(self.steer_val)
    def handleInput(self, evt):
        if event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                #change state to neutral
                self.app.state = NeutralState(self.steer_val, self.app)
            elif event.key in (K_DOWN, K_s):
                #increase speed
                self.force+=10
            elif event.key in (K_LEFT, K_a):
                self.steer_val = -70
            elif event.key in (K_RIGHT, K_d):
                self.steer_val = 70

class NeutralState(CarState):
    """docstring for NeutralState"""
    STOPPEDTICK = 402
    def __init__(self, s, myApp):
        self.steer_val = s
        self.app = myApp
    def update(self):
        self.pwm.setPWM(self.MOTORCHANNEL, 0, self.STOPPEDTICK)
        super(CarState,self).steer(self.steer_val)
    def handleInput(self, evt):
        if event.type == KEYDOWN:
            if event.key in (K_UP, K_w):
                #change state to forward
                self.app.state = ForwardState(10, self.steer_val, self.app)
            elif event.key in (K_DOWN, K_s):
                #change state to reverse
                self.app.state = ReverseState(10,self.steer_val, self.app)
            elif event.key in (K_LEFT, K_a):
                self.steer_val = -70
            elif event.key in (K_RIGHT, K_d):
                self.steer_val = 70
