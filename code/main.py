import pygame, sys
import game as g

# Pygame setup
pygame.init()
clock = pygame.time.Clock()
game = g.Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	#screen.fill('grey')
	game.run()

	pygame.display.update()
	clock.tick(60)