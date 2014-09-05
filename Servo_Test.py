#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

#servoMin = 150  # Min pulse length out of 4096
#servoMax = 650  # Max pulse length out of 4096

servoMin = 385
servoMax = 515

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
val = servoMin+1
flop = False
while (True):
    print val
    if(val > servoMax):
        flop = True
    else:
        if(val < servoMin):
            flop = False
    if(flop):
        val=val-15
    else:
        val=val+15
    pwm.setPWM(0,0,val)
    time.sleep(0.25)
  # Change speed of continuous servo on channel O
  #pwm.setPWM(0, 0, servoMin)
  #time.sleep(1)
  #setServoPulse(0, 100)
  #time.sleep(1)
  #setServoPulse(0, 150)
  #pwm.setPWM(0, 0, servoMax)
  #time.sleep(1)
