#!/usr/bin/python

from Adafruit.Adafruit_PWM_Servo_Driver import PWM
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
pwm.setPWMFreq(60)

for x in range(389,589,5):
    pwm.setPWM(0,0,x)
    print(x)
    time.sleep(0.25)
time.sleep(1)
pwm.setPWM(0,0,0)
#pwm.softwareReset()
time.sleep(1)
for x in range(388, 220, -5):
    pwm.setPWM(0,0,x)
    print(x)
    time.sleep(0.25)  
pwm.setPWM(0,0,0)
