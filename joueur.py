# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7
import pygame
pygame.init()
import sys
from pygame.locals import *

class Joueur:
    """
    Création d'un instance Joueur:
        joueur = Joueur(screen)

    attributs d'instance :
        vaisseau = l'image du joueur
        rect.x = position x du joueur
        rect.y = position y du joueur
        vie = vie du joueur
        _score = score du joueur
        coeur_remplie = image de la vie restante du joueur
        coeur_vide = image de la vie perdu du joueur

    attributs de classe:
        Méthode :
            move_right() fait bouger le joueur de "vitesse" pixel dans le sens "x" (self.rect.x)
            move_left() fait bouger le joueur de "vitesse" pixel dans le sens "y" (self.rect.y)
            afficher() fait afficher le joueur sur l'écran
            moov(longueur) prend dans une variable "keys" les touches appuyer par le joueur, si le joueur appuie sur la fleche de gauche
            cela appele la méthode move_left(). si le joueur appuie sur la fleche de droite cela appele la méthode move_right()
            getCoords(add_x = 0, add_y = 0) renvoie les coordonnées du joueur en ajoutant quelque pixel selon la demande pour trouver
            le centre de l'image
            kill() arrete le jeux si le joueur a 0 de vie
            affiche_vie() affiche sur l'ecran les coeurs du joueur selon sa vie 
    """
    def __init__(self, ecran):
        self.vaisseau = pygame.image.load('images/vaisseau.png')
        self.vaisseau = pygame.transform.scale(self.vaisseau, (60,40))
        self.rect = self.vaisseau.get_rect()
        self.rect.x = 1080//2
        self.rect.y = 720 - 100
        self.vie = 3
        self.screen = ecran
        self._score = 0
        self.vitesse = 5
        self.coeur_rempli = pygame.image.load('images/coeur_remplie.png')
        self.coeur_rempli = pygame.transform.scale(self.coeur_rempli, (64,50))
        self.coeur_vide = pygame.image.load('images/coeur_vide.png')
        self.coeur_vide = pygame.transform.scale(self.coeur_vide, (64,50))
        self.etat = "alive"
    def move_right(self):
        self.rect.x += self.vitesse

    def move_left(self):
        self.rect.x -= self.vitesse

    def afficher(self):
        self.screen.blit(self.vaisseau, (self.rect.x, self.rect.y))

    def moov(self, longueur):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.rect.x <= longueur - 64:
            self.move_right()
        if keys[pygame.K_LEFT] and self.rect.x >= 0:
            self.move_left()

    def getCoords(self, add_x = 0, add_y = 0):
        return self.rect.x + add_x,self.rect.y + add_y
    
    def kill(self):
        self.vie -= 1
        if self.vie == 0:
            self.etat = "dead"
    def ajout_score(self):
        self._score += 10

    def affiche_vie(self):
        #vie
        self.screen.blit(self.coeur_rempli, (70, 700))
        self.screen.blit(self.coeur_rempli, (120, 700))
        self.screen.blit(self.coeur_rempli, (170, 700))
        if self.vie == 2:
            self.screen.blit(self.coeur_vide, (170,700))
        if self.vie == 1:
            self.screen.blit(self.coeur_vide, (170,700))
            self.screen.blit(self.coeur_vide, (120,700))
