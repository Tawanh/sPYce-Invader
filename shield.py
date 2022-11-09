import pygame
import sys

class Shield_Square:
    """
    Création d'un instance Shield_Square:
        liste_square = Liste_Square(Position([float,float]), Sprite(str), taille([float,float]), bord(bool))

    attributs d'instance :
        _index_haut,_index_bas,_splitted_sprite,_sprite,_position,_taille,_bord

    attributs de classe:
        Méthode :
            detruire(orientation) change le sprite du bouclier et renvoie True si le bouclier doit encore exister
            afficher(ecran) affiche le bouclier sur ecran
            getCoord() renvoie la position du bouclier
            getScale() renvoie la taille du bouclier
    """
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
    """
    Création d'un instance Shield:
        square = Square(position([int,int]), taille_square([int,int]), sprite(str), spritegauche(str), spritedroit(str))

    attributs d'instance :
        _liste_shield_square,_position

    attributs de classe:
        Méthode :
            afficher(ecran) afficher tout les boucliers de la liste sur ecran
            get_liste() renvoie la liste de bouclier
            destroyShield(index) detrui le bouclier a l'index "index" (le transforme en None)
    """
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
