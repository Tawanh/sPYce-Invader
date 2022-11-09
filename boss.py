import pygame
pygame.init()
from random import randint
from pygame.locals import *
from projectile import Projectile
class Boss:
    """
    Création d'un instance Boss:
        boss = Boss(ecran)

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
            
            afficher() fait afficher le boss sur l'écran
            movement(longueur, projectile) fait se déplacer le boss selon sa vitesse sur l'axe des x puis choisi un nombre aleatoire entre 0 et
            30, si celui ci tombe sur 4 le boss envoie un projectile
            descente(longueur) si le boss s'approche du bord de la fenetre il descend de 10 pixel puis change son déplacement dans l'axe des x pour
            que celui ci se deplace dans le sens opposer
            kill() affiche une image de mort des que le boss meurt
    """
    def __init__(self, ecran):
        self.image_boss = pygame.image.load('images/invader2.png')
        self.image_boss = pygame.transform.scale(self.image_boss, (128,128))
        self.rect = self.image_boss.get_rect()
        self.rect.x = 500
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

    def movement(self, longueur, projectile):
        self.rect.x += self.vitesse
        self.descente(longueur)
        x = randint(0,30)
        if x == 4:
            projectile.append(Projectile(2 ,(self.rect.x, self.rect.y ),+1, self.screen))
            
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
            
    
            
    

