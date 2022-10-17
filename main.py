# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7

#from joueur import Joueur
import pygame
pygame.init()
from pygame import mixer
from pygame.locals import *

from projectile import Projectile

clock = pygame.time.Clock()
FPS = 60

longueur = 1080
largeur = 720
screen = pygame.display.set_mode((longueur, largeur))
vaisseau = pygame.image.load('vaisseau.png')
vaisseau = pygame.transform.scale(vaisseau, (64,64))
rect = vaisseau.get_rect()
rect.x = longueur//2
rect.y = largeur - 100


running = True

while running:
	screen.fill([0,0,0])
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
			if event.type == pygame.QUIT:
					pygame.quit()
			if event.key == pygame.K_RIGHT:
				rect.x += 5
			if event.key == pygame.K_LEFT:
				rect.x -= 5
			if event.key == pygame.K_SPACE:
				balle = Projectile(-1, 1, (rect.x ,rect.y -64), 1 , screen)
				balle.draw()


	#fixer le nombre de fps sur ma clock
	clock.tick(FPS)

	screen.blit(vaisseau, (rect.x, rect.y))
	pygame.display.update()

