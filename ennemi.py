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
            getRect() renvoie le rect de l'ennemi
            getCoord() renvoie les coordonnées de l'ennemi sous forme de deux float
            getScale() renvoie la taille de l'ennemi sous forme de deux float
            kill() tue l'ennemie
    """
    def __init__(self,Sprite,PV,Hauteur,Largeur,Position = [0,0]):
        self._sprite = pygame.transform.scale(Sprite, (Hauteur,Largeur))
        self._pv = PV
        self._position = Position
        self._lenght = Largeur
        self._height = Hauteur

    def movement(self,vitesse,direction,ecran):
        self.screen = ecran
        self._position[0] += vitesse * direction[0]
        self._position[1] += vitesse * direction[1]
        ecran.blit(self._sprite, self._position)

    def ajouterPv(self,ajout):
        self._pv += ajout

    def getPv(self):
        return self._pv

    def changeSprite(self,Sprite,Hauteur,Largeur):
        self._sprite = pygame.transform.scale(Sprite, (Hauteur,Largeur))

    def getRect(self):
        return self._sprite

    def getCoord(self, add_x = 0, add_y = 0):
        return self._position[0] + add_x,self._position[1] + add_y

    def getScale(self):
        return self._lenght, self._height

    def kill(self, type, tuple_index):
        if type == 0:
            self.image = pygame.image.load('images/death0.png').convert_alpha()
            self.changeSprite(self.image, self._height, self._lenght)
        if type == 1:
            self.image = pygame.image.load('images/death1.png').convert_alpha()
            self.changeSprite(self.image, self._height, self._lenght)
        if type == 2:
            self.image = pygame.image.load('images/death2.png').convert_alpha()
            self.changeSprite(self.image, self._height, self._lenght)
        if type == 3:
            self.image = pygame.image.load('images/death3.png').convert_alpha()
            self.changeSprite(self.image, self._height, self._lenght)
        self.screen.blit(self._sprite, self._position)
        tuple_index[1][tuple_index[0]] = None



class Liste_ennemi:
    """
    Création d'un instance Liste_ennemi:
        liste_ennemie = Liste_ennemie(nombre_ennemi_horizontal(int), nombre_etage_ennemi(int), espacement_horizontal(float), espacement_vertical(float), sprite(str), hauteur_joueur(float), largeur_joueur(float), ecran(pygame surface), longueur_deplacement_horizontal(float))

    attributs d'instance :
        _liste_ennemi

    attributs de classe:
        Méthode :
            movement_all_ennemi(vitesse,direction,screen,proba,projectile) fait bouger (vitesse,direction,screen) et tiré (proba,projectile) tout les ennemis
            getlistennemi() renvoie la liste d'ennemi
    """
    def __init__(self, nombre_ennemi_horizontal, nombre_etage_ennemi, espacement_horizontal, espacement_vertical, sprite, hauteur_joueur, largeur_joueur, ecran, longueur_deplacement_horizontal):
        marge = (ecran[0] - (largeur_joueur * nombre_ennemi_horizontal) - (espacement_horizontal *nombre_ennemi_horizontal)) / 2
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
                if j2 is not None:
                    j2.movement(vitesse,direction,screen)
                    nombre_none = 0
                    for i3 in range(i1 + 1, len(self._liste_ennemi)):
                        if self._liste_ennemi[i3][i2] is None:
                            nombre_none += 1
                    if nombre_none == len(self._liste_ennemi) - 1 - i1:
                        if randint(0,proba) == 1:
                            projectile.append(Projectile(2 ,j2.getCoord(0,j2.getScale()[1]),+1, screen))
    def getlistennemi(self):
        return self._liste_ennemi
