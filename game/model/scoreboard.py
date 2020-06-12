from game.config.constants import *
from game.subscriber.events import Goal, ResetGame
import pygame

class Placar:
    def __init__(self, event_manager) ->None:
        self.event_manager = event_manager
        self.score1 = 0
        self.score2 = 0

    def get_placar(self):   
        return self.score1, self.score2

    def set_placar(self,scores):
        self.score1= scores[0]
        self.score2= scores[1]

    def update(self,state)->None:
        """ Verifica o retorno de check_goal e atualiza o placar"""
        if state is not None:
            goal = Goal()
            reset = ResetGame()
            if goal.check_goal(LEFT,state.puck):
                self.score2 += 1
                reset.reset_conditions(state.puck,state.paddle_left,
                state.paddle_right, 2,2)
            if goal.check_goal(RIGHT,state.puck):
                self.score1 += 1
                reset.reset_conditions(state.puck,state.paddle_left,
                state.paddle_right, 1,2)