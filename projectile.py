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
            self.projectile = pygame.image.load('balle.png')
        elif sens == +1:
            self.projectile = pygame.image.load('balle2.png')
        self.projectile = pygame.transform.scale(self.projectile, (32,32))
        self.rect = self.projectile.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]
    
    def afficher(self):
            self.add_coords(y = self._sens*5)
            self.screen.blit(self.projectile, (self.rect.x, self.rect.y))
            
    def is_collide(self, y,objet= None, ):
        if isinstance(objet, list):
            for l in objet:
                for i, e in enumerate(l):
                    if e != None:
                        eposx, eposy = e.getCoord(8, 11)
                        if self.rect.y <= eposy and eposx + 32 >= self.rect.x >= eposx - e.lenght:
                            l[i] = None
                            return True
            return False
        elif objet !=None and self.rect.colliderect(objet.rect):
            objet.kill()
            return True
        elif self.rect.y >=  0  and self.rect.y <= y - 32:
            del self
            return False
        return True
    
    def get_coords(self):
        return (self.rect.x, self.rect.y)
    def add_coords(self, x:int = 0, y:int = 0):
        self.rect.x += x
        self.rect.y += y
    def set_coords(self, x:int = None ,y:int = None):
        if x == None:
            x = self.rect.x
        if y == None:
            y = self.rect.y
        self.rect.x = x
        self.rect.y = y
        
    def get_damage(self):
        return self._damage
    def set_damage(self, damage):
        self._damage = damage
    def add_damage(self,damage):
        self._damage += damage
        

        


        