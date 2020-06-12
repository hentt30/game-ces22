from game.subscriber.events import *
from game.model.paddle import Paddle
from game.model.puck import Puck
from game.model.scoreboard import Placar
from game.model.round import Round
from game.config.constants import *
import pygame

class State(object):
    def __init__(self, event_manager) -> None:
        self.event_manager = event_manager
        self.paddle_right = Paddle(PADDLE_RIGHT_X, PADDLE_RIGHT_Y, RIGHT)
        self.paddle_left = Paddle(PADDLE_LEFT_X, PADDLE_LEFT_Y, LEFT)
        self.puck = Puck()
        self.placar= Placar(event_manager)
        self.round= Round(event_manager)

    def get_state(self) -> None:
        state = {
            "paddle_right": self.paddle_right.get_pos(),
            "paddle_left": self.paddle_left.get_pos(),
            "puck": self.puck.get_pos(),
            "placar": self.placar.get_placar(),
            "round": self.round.get_round()
        }
        return state

    def update(self) -> None:
        """ Muda o estado do jogo e avisa a tela
        """
        self.paddle_left.update()
        self.paddle_right.update()
        self.puck.update(self.paddle_left, self.paddle_right)
        self.placar.update(self)
        self.round.update(self)
        self.event_manager.post(ChangeStateEvent(self.get_state()))
