import pygame
from game.config.constants import *

class ScoreboardView():
    def __init__(self) -> None:
        self.score1 = 0
        self.score2 = 0
    
    def render(self, screen) -> None:
        """ Define a forma do placar e aciona na tela"""
        small_font = pygame.font.SysFont("comicsans", 35)
        text1 = small_font.render("{0} : {1}".format("Player 1",str(self.score1)), True, BLACK)
        text2 = small_font.render("{0} : {1}".format("Player 2", str(self.score2)), True, BLACK)
    
        screen.blit(text1, [40, 0])
        screen.blit(text2, [WIDTH - 150, 0])
    
    def update(self, new_state):
        self.score1 = new_state[0]
        self.score2 = new_state[1]