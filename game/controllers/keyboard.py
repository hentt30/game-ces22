import pygame
from game.subscriber.events import *

class Keyboard(object):
    """ Trata dos inputs do teclado
    """
    def __init__(self, event_manager) -> None:
        self.event_manager = event_manager
        self.event_manager.subscribe_listener(self)

    def notify(self, event) -> None:
        """ Notifica o teclado se o usuário pressionar alguma tecla
        """
        if (isinstance(event, TickEvent)):
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    self.event_manager.post(QuitEvent())

