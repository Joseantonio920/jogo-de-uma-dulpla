import pygame
from pygame.locals import *

skin=pygame.Surface((10, 10))
skin.fill((255, 255, 255))
x=0

from main import *
def draw():
	tela.blit(skin, (x, 0))
def update():
	time.tick(20)
	global x
	x=x+10