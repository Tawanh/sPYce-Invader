# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7
import pygame
pygame.init()
import sys
from pygame.locals import *

class Joueur:

    def __init__(self, ecran):
        self.vaisseau = pygame.image.load('images/vaisseau.png')
        self.vaisseau = pygame.transform.scale(self.vaisseau, (64,64))
        self.rect = self.vaisseau.get_rect()
        self.rect.x = 1080//2
        self.rect.y = 720 - 100
        self.vie = 3
        self.type_tir = None
        self.screen = ecran
        self._score = 0
        self.coeur_rempli = pygame.image.load('images/coeur_remplie.png')
        self.coeur_rempli = pygame.transform.scale(self.coeur_rempli, (64,50))
        self.coeur_vide = pygame.image.load('images/coeur_vide.png')
        self.coeur_vide = pygame.transform.scale(self.coeur_vide, (64,50))

    def move_right(self):
        self.rect.x += 5

    def move_left(self):
        self.rect.x -= 5

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
            sys.exit()
            
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
