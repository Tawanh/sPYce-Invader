import pygame
import sys

class Shield_Square:
    def __init__(self, Position, Sprite, taille, bord = False):
        self._index_haut = 0
        self._index_bas = 0
        self._splitted_sprite = Sprite.split(".")
        self._sprite = self._splitted_sprite[0] + str(self._index_haut) + str(self._index_bas) + "." + self._splitted_sprite[1]
        self._sprite = pygame.image.load(self._sprite)
        self._position = Position
        self._taille = taille
        self._sprite = pygame.transform.scale(self._sprite,taille)
        self._bord = bord

    def detruire(self, orientation):
        if self._index_bas + self._index_haut == 4 and not self._bord:
            return False
        elif self._index_bas + self._index_haut == 2:
            return False
        if orientation == "bas":
            self._index_bas += 1
        elif orientation == "haut":
            self._index_haut += 1

        self._sprite = self._splitted_sprite[0] + str(self._index_haut) + str(self._index_bas) + "." + self._splitted_sprite[1]
        self._sprite = pygame.image.load(self._sprite)
        self._sprite = pygame.transform.scale(self._sprite,self._taille)
        return True

    def afficher(self, ecran):
        ecran.blit(self._sprite,self._position)

    def getCoord(self):
        return self._position[0],self._position[1]

    def getScale(self):
        return self._taille


class Shield:
    def __init__(self, position, taille_square, sprite, spritegauche, spritedroit):
        self._position = position
        self._liste_shield_square = []
        for i1 in range(4):
            for i2 in range(2):
                if i1 == 0 and i2 == 0:
                    self._liste_shield_square.append(Shield_Square((i1*taille_square + position[0],i2*taille_square + position[1]),spritegauche,(taille_square,taille_square),True))
                elif i1 == 3 and i2 == 0:
                    self._liste_shield_square.append(Shield_Square((i1*taille_square + position[0],i2*taille_square + position[1]),spritedroit,(taille_square,taille_square),True))
                else:
                    self._liste_shield_square.append(Shield_Square((i1*taille_square + position[0],i2*taille_square + position[1]),sprite,(taille_square,taille_square)))

    def afficher(self, ecran):
        for i in self._liste_shield_square:
            if i is not None:
                i.afficher(ecran)

    def get_liste(self):
        return self._liste_shield_square

    def destroyShield(self,index):
        self._liste_shield_square[index] = None
