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


projectiles_joueur = []
projectiles_ennemis = []
joueur = Joueur(screen)
boss = Boss(screen)
boss_kill = False
compt = 0
running = True
delai_tir_joueur = 0
while running:
    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.QUIT:
                running = False
            if event.key == pygame.K_SPACE and delai_tir_joueur <= 0:
                projectiles_joueur.append(Projectile(2 ,(joueur.getCoords(16)),-1, screen))
                delai_tir_joueur = 60

    joueur.moov(longueur)

    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)
    
    #Detecte les collisons des balles
    if projectiles_joueur:
        for i , e in enumerate(projectiles_joueur):
            if e.is_collide(largeur):
                del e
                projectiles_joueur.pop(i)
            elif not  boss_kill and e.rect.colliderect(boss.getRect()):
                boss_kill = True
                del e
                projectiles_joueur.pop(i)
            elif e.is_collide(largeur, liste_ennemi.getlistennemi()): 
                print("Ennemi mort")
                del e
                projectiles_joueur.pop(i)
            else:
                e.afficher()
    if projectiles_ennemis:
        for i, e in enumerate(projectiles_ennemis):
            if e.is_collide(largeur, joueur):
                projectiles_ennemis.pop(i)
            else:
                e.afficher()
                
    #movement ennemis
    compteur +=1
    if paterne_ennemi_horizontal:
        liste_ennemi.movement_all_ennemi(vitesse,direction,screen,500,projectiles_ennemis)
        if compteur == longueur_deplacement_horizontal//vitesse:
            paterne_ennemi_horizontal = False
            compteur = 0
    else:
        liste_ennemi.movement_all_ennemi(vitesse,[0,1],screen,500,projectiles_ennemis)
        if compteur == longueur_deplacement_vertical//vitesse:  
            paterne_ennemi_horizontal = True
            direction[0] *= -1
            compteur = 0
    delai_tir_joueur -=1  
    boss.movement(longueur)
    joueur.afficher()
    if not boss_kill:
        boss.afficher()
    pygame.display.update()

sys.exit()    