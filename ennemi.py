# Créé par Antoine.Herout

import pygame, sys
from pygame.locals import *
import time


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

        #affichage
        ecran.blit(self._sprite,self._position)

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
