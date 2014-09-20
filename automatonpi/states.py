#!/usr/bin/env python2

from automatonpi.packages.adafruit.Adafruit_PWM_Servo_Driver import PWM
import time
import pygame
from pygame.locals import *
class CarState():
	"""docstring for CarState"""
	pwm = PWM(0x40, debug=False)
	pwm.setPWMFreq(60)
	MOTORCHANNEL = 9
	SERVOCHANNEL = 8
	SERVOMIN = 385
	SERVOMAX = 515
	SERVOCENTER = int((SERVOMAX-SERVOMIN)/2.0)+SERVOMIN

	def steer(self, amt):
		tick = 0
		if(amt < 0):
			tick = int((self.SERVOMAX - self.SERVOCENTER) * (abs(amt)/100.00) + self.SERVOCENTER)
			#print "<<<<<LEFT tick: %d" % tick
			
		elif(amt > 0):
			tick = int(self.SERVOCENTER -(self.SERVOCENTER - self.SERVOMIN) * (abs(amt)/100.00))
			#print ">>>>>RIGHT tick: %d" % tick
		else:
			tick = self.SERVOCENTER

		self.pwm.setPWM(self.SERVOCHANNEL, 0, tick)

class ForwardState(CarState):
	"""docstring for ForwardState"""
	MINFORWARD = 395
	MAXFORWARD = 250
	def __init__(self, f, s, myApp):
		self.force = f
		self.steer_val = s
		self.app = myApp
	def update(self):
		if(self.force > 100):
			self.force = 100
		elif(self.force < 0):
			self.force = 0
		tick = int(self.MINFORWARD-((abs(self.force)/100.00) * (self.MINFORWARD - self.MAXFORWARD)))
		self.pwm.setPWM(self.MOTORCHANNEL, 0, tick)
		#super(CarState,self).steer(self.steer_val)
		self.steer(self.steer_val)
	def handleInput(self, event):
		if event.type == KEYDOWN:
			if event.key in (K_UP, K_w):
				#increase speed
				self.force+=10
			elif event.key in (K_DOWN, K_s):
				#change state to neutral
				self.app.state = NeutralState(self.steer_val, self.app)
			elif event.key in (K_LEFT, K_a):
				self.steer_val = -70
			elif event.key in (K_RIGHT, K_d):
				self.steer_val = 70
		if event.type == JOYAXISMOTION and event.axis <= 3:
			if event.axis == 0:
				if event.value <= 0:
					self.app.state = NeutralState(self.steer_val, self.app)
				elif event.value >= 0:
					self.force = int(100 * event.value)
			if event.axis == 3:
				self.steer_val = int(100 * abs(event.value))

class ReverseState(CarState):
	"""docstring for ReverseState"""
	MINREVERSE = 415
	MAXREVERSE = 550
	def __init__(self, f, s, myApp):
		self.force = f
		self.steer_val = s
		self.app = myApp
	def update(self):
		if(self.force > 100):
			self.force = 100
		elif(self.force < 0):
			self.force = 0
		tick = int(((self.force/100.00) * (self.MAXREVERSE - self.MINREVERSE))+self.MINREVERSE)
		self.pwm.setPWM(self.MOTORCHANNEL, 0, tick)
		#super(CarState,self).steer(self.steer_val)
		self.steer(self.steer_val)
	def handleInput(self, event):
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
		if event.type == JOYAXISMOTION and event.axis <= 3:
			if event.axis == 0:
				if event.value < 0:
					self.force = int(100 * abs(event.value))
				elif event.value >= 0:
					self.app.state = NeutralState(self.steer_val, self.app)
			if event.axis == 3:
				self.steer_val = int(100 * abs(event.value))


class NeutralState(CarState):
	"""docstring for NeutralState"""
	STOPPEDTICK = 402
	def __init__(self, s, myApp):
		self.steer_val = s
		self.app = myApp
		self.time_in_state = pygame.time.get_ticks()
		self.sent_stop = False
	def update(self):
		if not self.sent_stop:
			self.pwm.setPWM(self.MOTORCHANNEL, 0, self.STOPPEDTICK)
		#super(CarState,self).steer(self.steer_val)
		self.steer(self.steer_val)
		#time.sleep(.5)
	def handleInput(self, event):
		if event.type == KEYDOWN:
			if event.key in (K_UP, K_w):
				#change state to forward
				#if (pygame.time.get_ticks() - self.time_in_state > 2500):
				#    self.app.state = ForwardState(10, self.steer_val, self.app)
				self.app.state = ForwardState(10, self.steer_val, self.app)
			elif event.key in (K_DOWN, K_s):
				#change state to reverse
				#if (pygame.time.get_ticks() - self.time_in_state > 2500):
				#    self.app.state = ReverseState(10,self.steer_val, self.app)
				self.app.state = ReverseState(10,self.steer_val, self.app)
			elif event.key in (K_LEFT, K_a):
				self.steer_val = -70
			elif event.key in (K_RIGHT, K_d):
				self.steer_val = 70
		if event.type == JOYAXISMOTION and event.axis <= 3:
			if event.axis == 0:
				if event.value < 0:
					self.app.state = ReverseState(int(100*abs(event.value)), self.steer_val, self.app)
				elif event.value >= 0:
					self.app.state = ForwardState(int(100*event.value), self.steer_val, self.app)
			if event.axis == 3:
				self.steer_val = int(100 * abs(event.value))
