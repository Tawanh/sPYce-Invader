import pygame

class Projectile:
    
    def __init__(self,degat, direction,coords,type, ecran) -> None:
        self._damage = degat
        self._sens = direction
        self.x = coords[0]
        self.y = coords[1]
        self.type_ennemis = type
        self.screen = ecran
    def draw(self):
        projecitle = pygame.image.load('balle.png')
        projecitle= pygame.transform.scale(projecitle, (64,64))
        balle = projecitle.get_rect()
        
        projecitlent = pygame.Rect((self.x, self.y), (30,30))
        pygame.draw.rect(self.screen, (0,255,0), balle)

        