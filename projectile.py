import pygame
class Projectile:
    """
    Création d'un instance Projectile:
        balle = Projectile(degat: = 1, coords:tuple = (0,0),sens:int = 0, ecran = 0)

    attributs d'instance :
        _damage; _sens; screen; projectile; rect

    attributs de classe:
        Méthode :
            afficher() : permet l'affichage de la balle et la deplace a chaque fois que la fonction est appellée -> None
            is_collide() : detecte si la balle touche un ennemi ou un bord de l'ecran, et retourne True ou false -> Bool
            mutateurs et acceseur permetant le changement et l'affichage de : damage, rect.x , rect.y
    """
    def __init__(self,degat:int = 1, coords:tuple = (0,0),sens:int = 0, ecran = 0) -> None:
        self._damage = degat
        self._sens = sens
        self.screen = ecran

    #   Affichage ball
        if sens == -1:
            self.projectile = pygame.image.load('images/balle.png')
        elif sens == +1:
            self.projectile = pygame.image.load('images/balle2.png')
        self.projectile = pygame.transform.scale(self.projectile, (25,25))
        self.rect = self.projectile.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]

    def afficher(self):
            self.add_coords(y = self._sens*5)
            self.screen.blit(self.projectile, (self.rect.x, self.rect.y))

    def is_collide(self, largeur,objet = None, bouclier = False, direction = False):
        if bouclier:
            for i in objet:
                for k, l in enumerate(i.get_liste()):
                    if l is not None:
                        lposx, lposy = l.getCoord()
                        if lposy - l.getScale()[1]/2 <= self.rect.y <= lposy + l.getScale()[1]/2 and lposx - l.getScale()[0]/2 <= self.rect.x <= lposx + l.getScale()[0]/2:
                            a = l.detruire(direction)
                            if not a:
                                i.destroyShield(k)
                            return True
            return False
        elif isinstance(objet, list):
            for k ,l in enumerate(objet):
                for i, e in enumerate(l):
                    if e is not None:
                        eposx, eposy = e.getCoord(8, 11)
                        if self.rect.y <= eposy and eposx + 32 >= self.rect.x >= eposx - e.getScale()[0]:
                            l[i].kill(k, (i,l))
                            return True
            return False
        elif objet is not  None and self.rect.colliderect(objet.rect):
            objet.kill()
            return True
        elif largeur-150>=self.rect.y >=  0:
            del self
            return False
        return True

    def get_coords(self):
        return self.rect.x, self.rect.y
    def add_coords(self, x:int = 0, y:int = 0):
        self.rect.x += x
        self.rect.y += y
    def set_coords(self, x:int = None ,y:int = None):
        if x is None:
            x = self.rect.x
        if y is None:
            y = self.rect.y
        self.rect.x = x
        self.rect.y = y