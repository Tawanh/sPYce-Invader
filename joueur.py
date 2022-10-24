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
        self.point = 0

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
    #Provisoire, simule la mort
    def kill(self):
        print('Mort')
        sys.exit()# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7