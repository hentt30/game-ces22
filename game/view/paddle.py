import pygame

from game.config.constants import *


class Paddle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.radius = PADDLE_SIZE
        self.color = color

    def update(self, position) -> None:
        self.x = position[0]
        self.y = position[1]

    def render(self, screen):
        position = (int(self.x), int(self.y))

        pygame.draw.circle(screen, self.color, position, self.radius, 0)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius, 2)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius - 5, 2)
        pygame.draw.circle(screen, (0, 0, 0), position, self.radius - 10, 2)
