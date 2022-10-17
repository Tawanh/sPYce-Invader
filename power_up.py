

from random import randint
from turtle import position
import pygame


class Power_up:
    def __init__(self, position, screen) -> None:
        self._pos = position
        self._power_up_type = randint(1,4)
    def draw(self):
        if self._power_up_type == 1:
            pygame.draw.rect(screen)
        
