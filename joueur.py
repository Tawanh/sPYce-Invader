# Créé par Nathan.zorroche, le 13/10/2022 en Python 3.7
import pygame
pygame.init()

from pygame.locals import *

class Joueur:

    def __init__(self):
        self.vaisseau = pygame.image.load('vaisseau.png')
        self.vaisseau = pygame.transform.scale(self.vaisseau, (64,64))
        self.rect = self.vaisseau.get_rect()
        self.rect.x = 1080//2
        self.rect.y = 720 - 100
        self.vie = 3
        self.type_tir = None

    def move_right(self):
        self.rect.x += 5

    def move_left(self):
        self.rect.x -= 5
