import pygame
from pygame.locals import *

chao=[]
for i in range(5, 20, 1):
	chao.append((i*20, 280))
player=[]
player.append((240, 80))

skin=pygame.Surface((10, 10))
skin.fill((255, 255, 255))

skinc=pygame.Surface((20, 20))
skinc.fill((255, 255, 255))

from main import *
def draw():
	for p in player:
		tela.blit(skin, p)
	for c in chao:
		tela.blit(skinc, c)
def update():
	sla=9