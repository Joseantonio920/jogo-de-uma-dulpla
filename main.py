import pygame
from pygame.locals import *
pygame.init()
tela=pygame.display.set_mode((500, 500), pygame.SCALED | pygame.FULLSCREEN)
time=pygame.time.Clock()

import init
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			break
	tela.fill((25, 25, 25))
	init.draw()
	init.update()
	pygame.display.flip()
pygame.quit()