#!/usr/bin/python

from Adafruit.Adafruit_PWM_Servo_Driver import PWM
import time

class states:
    FORWARD = 0
    STOPPED = 1
    REVERSE = 2
    
class Car:

    STOPPEDTICK = 402
    minForward = 420
    maxForward = 550
    minReverse = 380
    maxReverse = 250
    servoMin = 385
    servoMax = 515
    servoCenter = int((servoMax-servoMin)/2.0)+servoMin
    state = states.STOPPED
    pwm = PWM(0x40, debug=True)
    pwm.setPWMFreq(60)
    motorchannel = 9
    servochannel = 8
    ready = True #is the motor/esc ready?

#########################################
# spd = a number from 1-100 representing
# percentage of forward speed
#########################################
    def forward(self, spd):
        tick = int(((spd/100.00) * (self.maxForward - self.minForward))+self.minForward)
        print("FORWARD >> %d ticks" % tick)
        if(not self.state == states.REVERSE):
            state = states.FORWARD
            self.pwm.setPWM(self.motorchannel, 0, tick)
        else:
            neutral()
            print('tried to move forward while state was REVERSE')
            forward(spd)
#########################################
# spd = a number from 1-100 representing
# percentage of reverse speed
#########################################        
    def reverse(self, spd):
        print(abs(spd))
        tick = int(self.minReverse-((abs(spd)/100.00) * (self.minReverse - self.maxReverse)))
        print("REVERSE >> %d ticks" % tick)
        if(not self.state == states.FORWARD):
            state = states.REVERSE
            self.pwm.setPWM(self.motorchannel, 0, tick)
        else:
            print('tried to move reverse while state was FORWARD')
            neutral()
            reverse(spd)
#######################
# Should stop the car
#######################
    def neutral(self):
        self.ready = False
        state = states.STOPPED
        self.pwm.setPWM(self.motorchannel, 0, self.STOPPEDTICK)
        #print(">>>START SLEEP 1")
        #time.sleep(10)
        #print("<<<END SLEEP 1")
        self.ready = True

#########################
# steer the car
#########################
    def left(self, amt):
        tick = int((self.servoMax - self.servoCenter) * (amt/100.00) + self.servoCenter)
        print "<<<<<LEFT tick: %d" % tick
        self.pwm.setPWM(self.servochannel, 0, tick)

    def right(self, amt):
        tick = int(self.servoCenter -(self.servoCenter - self.servoMin) * (amt/100.00))
        print ">>>>>RIGHT tick: %d" % tick
        self.pwm.setPWM(self.servochannel, 0, tick)

    def straight(self):
        self.pwm.setPWM(self.servochannel, 0, self.servoCenter)
