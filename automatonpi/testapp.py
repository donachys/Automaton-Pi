import math
import random
import sys
import time
import pygame
from states import *
from pygame.locals import *

class TestApp:
	FPS = 30 # frames per second to update the screen
	WINWIDTH = 640 # width of the program's window, in pixels
	WINHEIGHT = 480 # height in pixels
	HALF_WINWIDTH = int(WINWIDTH / 2)
	HALF_WINHEIGHT = int(WINHEIGHT / 2)
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	pygame.display.set_caption('Automaton-Pi')
	BASICFONT = pygame.font.Font('freesansbold.ttf', 32)
	def __init__(self):
		self.state = NeutralState(0, self)

	def run(self):
		while True:
			for event in pygame.event.get(): # event handling loop
				self.state.handleInput(event)
			self.state.update()

def main():
	app = TestApp()
	app.run()
#if __name__ == "__main__":
	
