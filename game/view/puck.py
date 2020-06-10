import pygame
from game.config.constants import *


class PuckView(object):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.radius = PUCK_SIZE
        self.white = WHITE

    def update(self, position) -> None:
        self.x = position[0]
        self.y = position[1]

    def render(self, screen) -> None:
        pygame.draw.circle(screen, self.white, (int(self.x), int(self.y)),
                           self.radius)
