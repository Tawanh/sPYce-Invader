# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7

#from joueur import Joueur
import pygame
from pygame.locals import *
from joueur import Joueur
from projectile import Projectile
from boss import Boss
import sys

pygame.init()
clock = pygame.time.Clock()
FPS = 60

longueur = 1080
largeur = 720
screen = pygame.display.set_mode((longueur, largeur))

projectiles = []
joueur = Joueur(screen)
boss = Boss(screen)

running = True

while running:
    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.QUIT:
                running = False
            if event.key == pygame.K_SPACE:
                projectiles.append(Projectile(2 ,(joueur.getCoords(16)),-1, screen)) #Louis-Léandre :
                                                                                                 #besoin methode : joueur.get_coord()
                                                                                                 #qui renvoie le x et le y du rect

    joueur.moov(longueur)

	#fixer le nombre de fps sur ma clock
    clock.tick(FPS)
    if projectiles != []:
        for e in projectiles:
            if e.is_collide():
                del e
            else:
                e.afficher()

    boss.movement(longueur)
    joueur.afficher()
    boss.afficher()
    pygame.display.update()

sys.exit()