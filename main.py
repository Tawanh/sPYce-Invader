# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7

#from joueur import Joueur
import pygame
from pygame.locals import *
from joueur import Joueur
from projectile import Projectile
from boss import Boss
import sys
from ennemi import Ennemi
from random import randint

#créer une liste d'ennemi
def listeEnnemi(nb_ennemi,nb_colonne,espacement1,espacement2,sprite,hauteur,largeur,ecran,longueur_deplacement_horizontal):
    marge = (ecran[0]-(largeur*nb_ennemi)-(espacement1*(nb_ennemi-1)))/ 2
    liste_ennemi = []
    splitted_image = sprite.split(".")
    for i1 in range(nb_colonne):
        liste_ennemi.append([])
        image = splitted_image[0] + str(i1) + "." + splitted_image[1]
        image = pygame.image.load(image).convert_alpha()
        for i2 in range(nb_ennemi):
            liste_ennemi[-1].append(Ennemi(image,1,hauteur, largeur,[marge + (espacement1 + largeur) * i2 + (espacement1/2) - (longueur_deplacement_horizontal/2), 25 + espacement2*i1]))
    return liste_ennemi


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
liste_ennemi = listeEnnemi(15,4,20,40,"invader.png",11*4,8*4,(longueur,largeur),longueur_deplacement_horizontal)
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
                projectiles.append(Projectile(2 ,(joueur.getCoords(16)),-1, screen)) #Louis-Léandre :
                                                                                                 #besoin methode : joueur.get_coord()
                                                                                                 #qui renvoie le x et le y du rect

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
        for i1,j1 in enumerate(liste_ennemi):
            for i2,j2 in enumerate(j1):
                if not j2 == None:
                    j2.movement(vitesse,direction, screen)
                    nombre_none = 0
                    for i3 in range(i1 + 1, len(liste_ennemi)):
                        if liste_ennemi[i3][i2] == None:
                            nombre_none +=1
                    if nombre_none == len(liste_ennemi) - 1 - i1:
                        if randint(0,500) == 1:
                            projectiles.append(Projectile(2 ,j2.getCoord(),+1, screen))
        if compteur == longueur_deplacement_horizontal//vitesse:
            paterne_ennemi_horizontal = False
            compteur = 0
    else:
        for i1,j1 in enumerate(liste_ennemi):
            for i2,j2 in enumerate(j1):
                if not j2 == None:
                    j2.movement(vitesse,[0,1],screen)
                    nombre_none = 0
                    for i3 in range(i1 + 1, len(liste_ennemi)):
                        if liste_ennemi[i3][i2] == None:
                            nombre_none +=1
                    if nombre_none == len(liste_ennemi) - 1 - i1:
                        if randint(0,500) == 1:
                            projectiles.append(Projectile(2 ,j2.getCoord(),+1, screen))

        if compteur == longueur_deplacement_vertical//vitesse:
            paterne_ennemi_horizontal = True
            direction[0] *= -1
            compteur = 0

    boss.movement(longueur)
    joueur.afficher()
    boss.afficher()
    pygame.display.update()

sys.exit()