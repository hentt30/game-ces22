import pygame
from game.subscriber.events import *


class PyGameView(object):
    def __init__(self, event_manager, model) -> None:
        self.event_manager = event_manager
        self.model = model
        # Subscribe event
        self.event_manager.subscribe_listener(self)
        self.is_initialized = False
        self.screen = None
        self.clock = None
        self.small_font = None

    def notify(self, event) -> None:
        """ Notifica a tela dos eventos possíveis
        """
        if (isinstance(event, InitializeEvent)):
            self.initialize()
        elif (isinstance(event, QuitEvent)):
            self.is_initialized = False
            pygame.quit()
        elif (isinstance(event, TickEvent)):
            if (not self.is_initialized):
                return
            self.render_play()
            self.clock.tick(30)

    def render_play(self) -> None:
        """ Renderiza o jogo
        """
        self.screen.fill((0, 0, 0))
        somewords = self.small_font.render(
            'You are Playing the game. F1 for help.', True, (0, 255, 0))
        self.screen.blit(somewords, (0, 0))
        pygame.display.flip()

    def initialize(self) -> None:
        """
        Inicializa o jogo
        """
        result = pygame.init()
        pygame.font.init()
        pygame.display.set_caption('demo game')
        self.screen = pygame.display.set_mode((600, 60))
        self.clock = pygame.time.Clock()
        self.small_font = pygame.font.Font(None, 40)
        self.is_initialized = True
