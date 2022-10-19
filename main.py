# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7

#from joueur import Joueur
import pygame
pygame.init()
from pygame.locals import *
from joueur import Joueur
from projectile import Projectile

clock = pygame.time.Clock()
FPS = 60

longueur = 1080
largeur = 720
screen = pygame.display.set_mode((longueur, largeur))

joueur = Joueur(screen)

running = True

while running:
	screen.fill([0,0,0])
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
			if event.type == pygame.QUIT:
				pygame.quit()

	keys = pygame.key.get_pressed()	
			
	if keys[pygame.K_RIGHT] and joueur.rect.x <= longueur - 64:
			joueur.move_right()
	if keys[pygame.K_LEFT] and joueur.rect.x >= 0:
			joueur.move_left()


	#fixer le nombre de fps sur ma clock
	clock.tick(FPS)

	joueur.afficher()
	pygame.display.update()

