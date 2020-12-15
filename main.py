import pygame
from pygame.locals import *
pygame.init()
tela=pygame.display.set_mode((500, 500))
while True:
	for event in pygame.event.get():
		if event.type==QUIT:
			break
pygame.quit()