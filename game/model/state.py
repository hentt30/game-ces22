from game.subscriber.events import *
from game.model.paddle import Paddle
from game.config.constants import *


class State(object):
    def __init__(self, event_manager) -> None:
        self.event_manager = event_manager
        self.paddle_right = Paddle(PADDLE_RIGHT_X, PADDLE_RIGHT_Y, RIGHT)
        self.paddle_left = Paddle(PADDLE_LEFT_X, PADDLE_LEFT_Y, LEFT)

    def get_state(self) -> None:
        state = {
            "paddle_right": self.paddle_right.get_pos(),
            "paddle_left": self.paddle_left.get_pos()
        }
        return state

    def update(self) -> None:
        """ Muda o estado do jogo e avisa a tela
        """
        self.paddle_left.update()
        self.paddle_right.update()
        self.event_manager.post(ChangeStateEvent(self.get_state()))