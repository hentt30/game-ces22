import pygame
from game.config.constants import *


class Puck(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = PUCK_SIZE
        self.white = WHITE

    def render(self, screen):
        pygame.draw.circle(screen, self.white, (int(self.x), int(self.y)),
                           self.radius)
