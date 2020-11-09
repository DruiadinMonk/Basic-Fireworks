# Firework class to make the firework object with an explosion function.

# MODULES
import pygame



# CLASS FIREWORK
class Firework:

	# INITIALIZE
	def __init__(self, window, color, x, y, vel, radius, ):
		self.window = window
		self.color = color
		self.x = x
		self.y = y
		self.vel = vel
		self.radius = radius


	# DRAW FIREWORK: A line for the firework. (Once it hit's Mouse (x, y), then draw explosion....do this in 'MAIN.py'.)
	# I can make 'color' the color that will explode, including the firework itself.
	def draw(self):
		pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
		self.y -= self.vel
