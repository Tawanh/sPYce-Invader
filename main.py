# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7

#from joueur import Joueur
import pygame
from pygame.locals import *
from joueur import Joueur
from projectile import Projectile
from boss import Boss
import sys
from ennemi import Ennemi,Liste_ennemi
from random import randint

pygame.init()
clock = pygame.time.Clock()
FPS = 60

longueur = 1080
largeur = 720
screen = pygame.display.set_mode((longueur, largeur))

#variable ennemi
paterne_ennemi_horizontal = True
direction = [1,0]
vitesse = 0.3
longueur_deplacement_vertical = 20
longueur_deplacement_horizontal = 100
liste_ennemi = Liste_ennemi(15,4,20,40,"invader.png",11*4,8*4,(longueur,largeur),longueur_deplacement_horizontal)
compteur = 0


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
                projectiles.append(Projectile(2 ,(joueur.getCoords(16)),-1, screen))

    joueur.moov(longueur)

	#fixer le nombre de fps sur ma clock
    clock.tick(FPS)
    if projectiles != []:
        for e in projectiles:
            if e.is_collide(largeur, objet = None):
                del e
            else:
                e.afficher()
    #movement ennemis
    compteur +=1
    if paterne_ennemi_horizontal:
        liste_ennemi.movement_all_ennemi(vitesse,direction,screen,500,projectiles)
        if compteur == longueur_deplacement_horizontal//vitesse:
            paterne_ennemi_horizontal = False
            compteur = 0
    else:
        liste_ennemi.movement_all_ennemi(vitesse,[0,1],screen,500,projectiles)
        if compteur == longueur_deplacement_vertical//vitesse:
            paterne_ennemi_horizontal = True
            direction[0] *= -1
            compteur = 0

    boss.movement(longueur)
    joueur.afficher()
    boss.afficher()
    pygame.display.update()

sys.exit()