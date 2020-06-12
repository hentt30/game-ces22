import pygame
from game.config.constants import *

class RoundView():
    def __init__(self) -> None:
        self.round_no = 0
        self.round_p1 = 0
        self.round_p2 = 0
        
    def print_text(self, text, center, screen) -> None:
        """ Definir posição e formato do texto pro round """
        font = pygame.font.SysFont("comicsans", 45)
        text_surf = font.render(text, True, SCOREBOARD_COLOR)
        text_rect = text_surf.get_rect()
        text_rect.center = center
        screen.blit(text_surf, text_rect)

    def render(self, screen) -> None:
        """ Imprime  o round do jogo """
        self.print_text("Round " + str(self.round_no), (WIDTH/2, 20), screen)
        self.print_text(str(self.round_p1) + " : " + str(self.round_p2), (WIDTH / 2, 50), screen)
    
    def update(self, new_state) -> None:
        self.round_no = new_state[0]
        self.round_p1 = new_state[1]
        self.round_p2 = new_state[2]
