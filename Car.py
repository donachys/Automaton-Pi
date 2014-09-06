#!/usr/bin/python

from Adafruit.Adafruit_PWM_Servo_Driver import PWM
import time

class states:
    FORWARD = 0
    STOPPED = 1
    REVERSE = 2
    
class Car:

    STOPPEDTICK = 400
    minForward = 420
    maxForward = 550
    minReverse = 380
    maxReverse = 250
    state = states.STOPPED
    pwm = PWM(0x40, debug=True)
    pwm.setPWMFreq(60)
    motorchannel = 0

    def forward(self, spd):
        tick = ((spd/100) * (maxForward - minForward))+minForward
        if(not state == states.REVERSE):
            state = states.FORWARD
            self.pwm.setPWM(motorchannel, 0, tick)
        else
            neutral()
            print('tried to move forward while state was REVERSE')
            forward(spd)
        
    def reverse(self, spd):
        tick = ((spd/100) * (minReverse = maxReverse))-minReverse
        if(not state == states.FORWARD):
            state = states.REVERSE
            self.pwm.setPWM(motorchannel, 0, tick)
        else
            print('tried to move reverse while state was FORWARD')
            neutral()
            reverse(spd)
            
    def neutral(self):
        state = states.STOPPED
        self.pwm.setPWM(motorchannel, 0, STOPPEDTICK)

      
        
