import pygame
pygame.init()

from pygame.locals import *

class Boss:

    def __init__(self, ecran):
        self.image_boss = pygame.image.load('invader2.png')
        self.image_boss = pygame.transform.scale(self.image_boss, (64,64))
        self.rect = self.image_boss.get_rect()
        self.rect.x = 1080//2
        self.rect.y = 720 //2
        self.screen = ecran
        self._pv = 20
        self.vitesse = 2

    def ajouterPv(self,ajout):
        self._pv += ajout

    def getPv(self):
        return self._pv

    def afficher(self):
        self.screen.blit(self.image_boss, (self.rect.x, self.rect.y))

    def movement(self, longueur):
        self.rect.x += self.vitesse
        if self.rect.x >= longueur - 150:
            self.vitesse *= -1
            self.rect.y += 100
        if self.rect.x <= 150:
            self.vitesse *= -1
            self.rect.y += 100

