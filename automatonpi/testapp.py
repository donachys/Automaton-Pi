import math
import random
import sys
import time
import pygame
from states import *
from pygame.locals import *

class TestApp:
	FPS = 30 # frames per second to update the screen
	#WINWIDTH = 640 # width of the program's window, in pixels
	#WINHEIGHT = 480 # height in pixels
	#HALF_WINWIDTH = int(WINWIDTH / 2)
	#HALF_WINHEIGHT = int(WINHEIGHT / 2)
	
	#DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	#pygame.display.set_caption('Automaton-Pi')
	#BASICFONT = pygame.font.Font('freesansbold.ttf', 32)
	def __init__(self):
		self.state = NeutralState(0, self)

	def run(self):
		pygame.init()
		pygame.joystick.init()
		joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
		print joysticks
		joystick = pygame.joystick.Joystick(0)
		joystick.init()
		pygame.event.set_allowed(None)
		pygame.event.set_allowed([pygame.QUIT, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP, pygame.JOYHATMOTION]) # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
		while True:
			for event in pygame.event.get(): # event handling loop
				self.state.handleInput(event)
				name = joystick.get_name()
				print name
				axes = joystick.get_numaxes()
				print "axes {}".format(axes)
				for i in range(axes):
					axis = joystick.get_axis(i)
					print "Axis: {} value: {}".format(i, axis)
				buttons = joystick.get_numbuttons()
				print "buttons {}".format(buttons)
				for i in range(buttons):
					button = joystick.get_button(i)
					print "Button: {} value: {}".format(i, button)
				hats = joystick.get_numhats()
				print "hats {}".format(hats)
				for i in range(hats):
					hat = joystick.get_hat(i)
					print "Hat: {} value: {}",format(i, hat)
			self.state.update()

def main():
	app = TestApp()
	app.run()
#if __name__ == "__main__":
	
