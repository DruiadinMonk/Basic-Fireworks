# Fireworks simulation.

# MODULES
import pygame
import random
import sys
from firework import Firework



# INITIALIZE
pygame.init()
WIN_X, WIN_Y = 400, 600
window = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.display.set_caption("Fireworks Simulator")
clock = pygame.time.Clock()
run = True
FPS = 30 		# Speed of program
gravity = 1
timer = 15 		# After 'X' seconds, create another Firework



# COLORS
BACKGROUND 	= (  0,   0,   0)
SALMON_PINK = (255, 145, 164)
RED 		= (255,  38,  38)
CORAL 		= (255, 130,  77)
ORANGE 		= (255, 128,   0)
SUNGLOW 	= (255, 200,  71)
LEMON 		= (255, 247,   0)
INCHWORM 	= (160, 255,  77)
NEON_GREEN 	= ( 23, 255,  38)
AQUAMARINE 	= (127, 255, 212)
AQUA 		= ( 23, 232, 255)
AZURE 	 	= (  0, 128, 255)
BLUE_VIOLET = (131,  59, 255)
VIOLET     	= (133,  25, 255)
FUSCHSIA 	= (255,   0, 255)

WHITE  = (255, 255, 255)
L_GRAY = (170, 170, 170)
D_GRAY = ( 85,  85,  85)

# List of all colors, 14 total, except BACKGROUND and shades of gray.
colors = [SALMON_PINK, RED, CORAL, ORANGE, SUNGLOW, LEMON, INCHWORM, NEON_GREEN, AQUAMARINE, AQUA, AZURE, BLUE_VIOLET, VIOLET, FUSCHSIA ]



# Create an initial 15 fireworks
fireworks = []
for i in range(10):
	r_x = random.randint(50, 350) 		# Random 'x' axis.
	r_vel = random.randint(12, 35) 		# Random velocity / height.
	r_col = random.randint(0, 13)  		# Random color selector
	radius = 5 							# Radius of firework.

	f = Firework(window, colors[r_col], r_x, WIN_Y+radius, r_vel, radius) 	# Object

	fireworks.append(f) 				# Add firework to list.



# MAIN LOOP
while run:


	# INITIALIZE
	clock.tick(FPS) 	 		# Speed of loop.
	window.fill(BACKGROUND) 	# Background color.
	MOUSE_X, MOUSE_Y = pygame.mouse.get_pos()


	# EACH EVENT
	for event in pygame.event.get():
		# IF QUIT...
		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()


	# if timer == 0:

	for i in range(len(fireworks)):

		# Stop firework when...
		if fireworks[i].vel <= 0:
			fireworks[i].vel = 0

			# After object in 'fireworks[]' list stops, explode it.
			# Explode radically increases size then disappears after "Random max size" is hit.
			fireworks[i].radius += 3

		else: 	# Else, keep applying gravity.
			fireworks[i].vel -= gravity


		# Reset when firework is done exploding.
		if fireworks[i].radius >= 50:

			r_x = random.randint(50, 350) 		# Random 'x' axis.
			r_vel = random.randint(12, 35) 		# Random velocity / height.
			r_col = random.randint(0, 13)  	# Random color selector

			fireworks[i].y = WIN_Y+radius
			fireworks[i].x = r_x
			fireworks[i].color = colors[r_col]  	# Random color selector
			fireworks[i].vel = r_vel
			fireworks[i].radius = 5



		fireworks[i].draw()

	# timer -= 1


	# UPDATE
	pygame.display.update()
