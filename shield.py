import pygame
import sys

class Shield_Square:
    def __init__(self, Position, Sprite, taille):
        self._index_haut = 0
        self._index_bas = 0
        self._splitted_sprite = Sprite.split(".")
        self._sprite = self._splitted_sprite[0] + str(self._index_haut) + str(self._index_bas) + "." + self._splitted_sprite[1]
        self._sprite = pygame.image.load(self._sprite)
        self._position = Position
        self._taille = taille
        self._sprite = pygame.transform.scale(self._sprite,taille)

    def detruire(self, orientation):
        if orientation == "bas":
            self._index_bas += 1
        elif orientation == "haut":
            self._index_haut += 1

        if self._index_bas + self._index_haut == 4:
            return False

        self._sprite = self._splitted_sprite[0] + str(self._index_haut) + str(self._index_bas) + "." + self._splitted_sprite[1]
        self._sprite = pygame.image.load(self._sprite)
        return True
    
    def afficher(self, ecran):
        ecran.blit(self._sprite,self._position)
        

class Shield:
    def __init__(self, position, taille_square, sprite):
        self._position = position
        self._liste_shield_square = []
        for i1 in range(2):
            for i2 in range(3):
                self._liste_shield_square.append(Shield_Square((i1*taille_square + position[0],i2*taille_square + position[1]),sprite,(taille_square,taille_square)))

    def afficher(self, ecran):
        for i in self._liste_shield_square:
            i.afficher(ecran)

    def get_liste(self):
        return self._liste_shield_square
