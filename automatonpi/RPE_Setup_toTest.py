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

