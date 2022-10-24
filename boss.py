import pygame
pygame.init()

from pygame.locals import *

class Boss:

    def __init__(self, ecran):
        self.image_boss = pygame.image.load('images/invader2.png')
        self.image_boss = pygame.transform.scale(self.image_boss, (128,128))
        self.rect = self.image_boss.get_rect()
        self.rect.x = 1080//2
        self.rect.y = 100
        self.screen = ecran
        self._pv = 20
        self.vitesse = 1

    def ajouterPv(self,ajout):
        self._pv += ajout

    def getPv(self):
        return self._pv

    def afficher(self):
        self.screen.blit(self.image_boss, (self.rect.x, self.rect.y))

    def movement(self, longueur):
        self.rect.x += self.vitesse
        self.descente(longueur)
    def getRect(self):
        return self.rect
        
    def descente(self, longueur):
        if self.rect.x >= longueur - 150:
            self.vitesse *= -1
            self.rect.y += 20
        if self.rect.x <= 150:
            self.vitesse *= -1
            self.rect.y += 20
    def kill(self):
        self.image_boss = pygame.image.load('images/death2.png')
        self.image_boss = pygame.transform.scale(self.image_boss, (128,128))
        self.afficher()
            
    
            
    

