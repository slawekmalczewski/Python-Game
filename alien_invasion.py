import sys

import pygame

def run_game():
	#Game initialization and creation of a game window
	
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion by Slawomir Malczewski")
	
	#define BackGround color
	bg_color = (230,230,230)
	
	#Main game loop
	while True:
		#Waiting for an event - key stroke or mouse click
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit
		
		screen.fill(bg_color)
		
		#Display the most recently modified window
		pygame.display.flip()
		
run_game()
