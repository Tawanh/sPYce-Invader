# Créé par Antoine.Herout

import pygame
from pygame.locals import *

from random import randint
from projectile import Projectile


class Ennemi:
    """
    Création d'un instance Ennemi:
        ennemie = Ennemie(Sprite(str),PV(int),Position([int,int]))

    attributs d'instance :
        _sprite,_pv,_position

    attributs de classe:
        Méthode :
            movement(vitesse,direction,ecran) fait bouger l'ennemi de "vitesse" pixel dans le sens "direction" ([x,y]) sur la surface ecran
            ajouterPv(ajout) ajoute le nombre "ajout" a la variable d'instance pv
            getPv() retourne la variable d'instance pv
            changeSprite(Sprite) change l'image de l'instance en fonction de "Sprite" et modifie sa grandeur avec "Hauteur" et "Largeur"
            testCollider(rect) test si l'instance est entré en collison avec un autre rect et renvoie la reponse sous forme de bool
    """
    def __init__(self,Sprite,PV,Hauteur,Largeur,Position = [0,0]):
        self._sprite = pygame.transform.scale(Sprite, (Hauteur,Largeur))
        self._pv = PV
        self._position = Position
        self.lenght = Largeur
    def movement(self,vitesse,direction,ecran):
        self._position[0] += vitesse * direction[0]
        self._position[1] += vitesse * direction[1]
        ecran.blit(self._sprite, self._position)

    def ajouterPv(self,ajout):
        self._pv += ajout

    def getPv(self):
        return self._pv

    def changeSprite(self,Sprite,Hauteur,Largeur):
        self.sprite = pygame.transform.scale(Sprite, (Hauteur,Largeur))

    def getRect(self):
        return self._sprite

    def getCoord(self, add_x = 0, add_y = 0):
        return (self._position[0] + add_x,self._position[1] + add_y)

class Liste_ennemi:
    def __init__(self, nombre_ennemi_horizontal, nombre_etage_ennemi, espacement_horizontal, espacement_vertical, sprite, hauteur_joueur, largeur_joueur, ecran, longueur_deplacement_horizontal):
        marge = (ecran[0] - (largeur_joueur * nombre_ennemi_horizontal) - (espacement_horizontal *(nombre_ennemi_horizontal))) / 2
        self._liste_ennemi = []
        splitted_image = sprite.split(".")
        for i1 in range(nombre_etage_ennemi):
            self._liste_ennemi.append([])
            image = splitted_image[0] + str(i1) + "." + splitted_image[1]
            image = pygame.image.load(image).convert_alpha()
            for i2 in range(nombre_ennemi_horizontal):
                self._liste_ennemi[-1].append(Ennemi(image, 1, hauteur_joueur, largeur_joueur,[marge + (espacement_horizontal + largeur_joueur) * i2 + (espacement_horizontal / 2) - (longueur_deplacement_horizontal / 2), 25 + espacement_vertical * i1]))

    def movement_all_ennemi(self,vitesse,direction,screen,proba,projectile):
        for i1,j1 in enumerate(self._liste_ennemi):
            for i2,j2 in enumerate(j1):
                if not j2 == None:
                    j2.movement(vitesse,direction,screen)
                    nombre_none = 0
                    for i3 in range(i1 + 1, len(self._liste_ennemi)):
                        if self._liste_ennemi[i3][i2] == None:
                            nombre_none += 1
                    if nombre_none == len(self._liste_ennemi) - 1 - i1:
                        if randint(0,proba) == 1:
                            projectile.append(Projectile(2 ,j2.getCoord(16),+1, screen))
    def getlistennemi(self):
        return self._liste_ennemi