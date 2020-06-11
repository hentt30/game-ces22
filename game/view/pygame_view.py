import pygame
from game.view.field import Field
from game.view.puck import PuckView
from game.view.paddle import PaddleView
from game.subscriber.events import *
from game.config.constants import *
from game.model.state import Placar, Round


class PyGameView(object):
    def __init__(self, event_manager) -> None:
        self.event_manager = event_manager
        self.event_manager.subscribe_listener(self)
        self.is_initialized = False
        self.screen = None
        self.clock = None
        self.small_font = None
        self.fps = FPS
        self.field = Field()
        self.paddle_right = PaddleView(PADDLE_RIGHT_X, PADDLE_RIGHT_Y,
                                   PADDLE_RIGHT_COLOR)
        self.paddle_left = PaddleView(PADDLE_LEFT_X, PADDLE_LEFT_Y,
                                  PADDLE_LEFT_COLOR)
        self.puck = PuckView(WIDTH / 2, HEIGHT / 2)
        self.placar= Placar(event_manager)
        self.round= Round(event_manager)

    def notify(self, event) -> None:
        """ Notifica a tela dos eventos possíveis
        """
        if (isinstance(event, InitializeEvent)):
            self.initialize()
        elif (isinstance(event, QuitEvent)):
            self.is_initialized = False
            pygame.quit()
        elif (isinstance(event, ChangeStateEvent)):
            if (not self.is_initialized):
                return
            self.update(event.state)
        elif (isinstance(event, TickEvent)):
            if (not self.is_initialized):
                return
            self.render_play()

    def render_play(self) -> None:
        """ Renderiza o jogo
        """
        self.clock.tick(self.fps)
        self.screen.fill((0, 0, 0))
        self.field.render(self.screen)
        self.paddle_right.render(self.screen)
        self.paddle_left.render(self.screen)
        self.puck.render(self.screen)
        self.placar.get_placar()
        self.round.get_round()
        pygame.display.flip()

    def update(self, new_state) -> None:
        """ Atualiza a posição dos objetos
        """
        self.paddle_right.update(new_state[PADDLE_RIGHT])
        self.paddle_left.update(new_state[PADDLE_LEFT])
        self.puck.update(new_state[PUCK])
        self.placar.update_placar(0,new_state[PLACAR])
        self.round.update_round(0,new_state[ROUND])

    def initialize(self) -> None:
        """Inicializa o jogo
        """
        result = pygame.init()
        pygame.font.init()
        pygame.display.set_caption('air hockey')
        self.screen = pygame.display.set_mode((1200, 600))
        self.clock = pygame.time.Clock()
        self.small_font = pygame.font.Font(None, 40)
        self.is_initialized = True
