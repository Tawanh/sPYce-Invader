# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7

#from joueur import Joueur
import pygame
from pygame.locals import *
from joueur import Joueur
from projectile import Projectile
from boss import Boss
import sys
from ennemi import Liste_ennemi
from shield import Shield, Shield_Square

pygame.init()
clock = pygame.time.Clock()
FPS = 60

longueur = 1080
largeur = 800
screen = pygame.display.set_mode((longueur, largeur))
font = pygame.font.Font("font/CosmicAlien-V4Ax.ttf", 50)

#variable ennemi
paterne_ennemi_horizontal = True
direction = [1,0]
vitesse = 0.3
longueur_deplacement_vertical = 20
longueur_deplacement_horizontal = 100
liste_ennemi = Liste_ennemi(15,4,20,40,"images/invader.png",11*4,8*4,(longueur,largeur),longueur_deplacement_horizontal)
compteur = 0

#variable bouclier
liste_tout_shield = []
for i in range(4):
    liste_tout_shield.append(Shield((100 + i * 250,500) , 30, "images/bouclier.png","images/boucliergauche.png","images/bouclierdroit.png"))
print(liste_tout_shield)

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
    if projectiles_joueur != []:
        for i , e in enumerate(projectiles_joueur):
            if e.is_collide(largeur):
                del e
            elif not  boss_kill and e.rect.colliderect(boss.getRect()):
                projectiles_joueur.pop(i)
                boss._pv -= 1
                if boss._pv ==0:
                    boss.kill()
                    boss_kill = True
            elif e.is_collide(largeur, liste_ennemi.getlistennemi()):
                print("Ennemi mort")
		joueur.ajout_score()
                projectiles_joueur.pop(i)
            elif e.is_collide(largeur, liste_tout_shield, True, "haut"):
                projectiles_joueur.pop(i)
            else:
                e.afficher()
    if projectiles_ennemis != []:
        for i, e in enumerate(projectiles_ennemis):
            if e.is_collide(largeur, joueur):
                projectiles_ennemis.pop(i)
            elif e.is_collide(largeur, liste_tout_shield, True, "bas"):
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
    
    joueur.afficher()
    

    #bouclier
    for i in liste_tout_shield:
        i.afficher(screen)

    #score
    score_texte = font.render(f"Score : {joueur._score}", 1, (255,255,255))
    screen.blit(score_texte, (380, 700))

    #vie
    joueur.affiche_vie()

    #Apparition du boss
    if joueur._score == 200:
        liste_ennemi._liste_ennemi = []
        if not boss_kill:
            boss.afficher()
            boss.movement(longueur, projectiles_ennemis)
		
    pygame.display.update()

sys.exit()
