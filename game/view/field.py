import pygame
from game.config.constants import *


class Field(object):
    def __init__(self) -> None:
        """ Instanciar variáveis para descrever um campo
        """
        self.height = HEIGHT
        self.width = WIDTH
        self.white = WHITE
        self.black = BLACK
        self.goal_width = GOAL_WIDTH
        self.goal_yleft = GOAL_Y_LEFT
        self.goal_yright = GOAL_Y_RIGHT
        self.background_color = BACKGROUND_COLOR

    def draw_center_circle(self, screen) -> None:
        """ Desenha o círculo central
        """
        pygame.draw.circle(screen, self.white,
                           (int(self.width / 2), int(self.height / 2)), 70, 5)

    def draw_rectangle_field(self, screen) -> None:
        """Desenha o retângulo principal do campo
        """
        pygame.draw.rect(screen, self.white, (0, 0, self.width, self.height),
                         5)

    def draw_defense_areas(self, screen) -> None:
        """ Desenha as áreas de defesa
        """
        pygame.draw.rect(screen, self.white,
                         (0, int(self.height / 2) - 150, 150, 300), 5)
        pygame.draw.rect(
            screen, self.white,
            (self.width - 150, int(self.height / 2) - 150, 150, 300), 5)

    def draw_goals(self, screen) -> None:
        """ Desenha os gols
        """
        pygame.draw.rect(screen, self.black,
                         (0, self.goal_yleft, 5, self.goal_width))
        pygame.draw.rect(screen, self.black,
                         (self.width - 5, self.goal_yright, 5, self.goal_width))

    def draw_field_divider(self, screen) -> None:
        """ Desenha o divisor do campo
        """
        pygame.draw.rect(screen, self.white,
                         (self.width / 2, 0, 3, self.height))

    def render(self, screen) -> None:
        """ Desenha o campo de futebol
        """
        screen.fill(self.background_color)
        self.draw_center_circle(screen)
        self.draw_rectangle_field(screen)
        self.draw_defense_areas(screen)
        self.draw_field_divider(screen)
        self.draw_goals(screen)