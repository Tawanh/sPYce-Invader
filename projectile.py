import pygame

class Projectile:
    
    def __init__(self,degat, coords:tuple = (0,0),sens:int = 0, ecran = 0) -> None:
        self._damage = degat
        self._sens = sens
        self.screen = ecran
        
    #   Affichage balle
        self.projectile = pygame.image.load('balle.png')
        self.projectile = pygame.transform.scale(self.projectile, (32,32))
        self.rect = self.projectile.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]
    
    def afficher(self):
            self.rect.y += self._sens * 5
            self.screen.blit(self.projectile, (self.rect.x, self.rect.y))
            
    def is_collide(self):
        if self.rect.y >=  0  and self.rect.y <= pygame.display.get_window_size()[1] - 32:
            return False
        return True
    
    def get_coords(self):
        return (self.rect.x, self.rect.y)
    def set_coords(self, x:int = None ,y:int = None):
        if x == None:
            x = self.rect.x
        if y == None:
            y = self.rect.y
        self.rect.x = x
        self.rect.y = y
    
    def add_coords(self, x:int = 0, y:int = 0):
        self.rect.x += x
        self.rect.y += y
        
    def get_damage(self):
        return self._damage
    def set_damage(self, damage):
        self._damage = damage
    def add_damage(self,damage):
        self._damage += damage
        

        


        